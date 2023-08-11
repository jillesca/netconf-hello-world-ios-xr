import logging
import xmltodict
from ncclient import manager
from ncclient.operations.errors import TimeoutExpiredError
from ncclient.transport.errors import SSHError, AuthenticationError


PORT = 830
TIMEOUT = 60
USERNAME = "admin"
PASSWORD = "C1sco12345"
LOOK_FOR_KEYS = False
HOSTKEY_VERIFY = False
DEVICE = "sandbox-iosxr-1.cisco.com"

logging.basicConfig(
    level=logging.INFO,
)

hostname_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
        <system xmlns="http://openconfig.net/yang/system">
            <config>
                <hostname />
            </config>
        </system>
    </filter>
"""


def connect() -> str:
    with manager.connect(
        host=DEVICE,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=HOSTKEY_VERIFY,
        look_for_keys=LOOK_FOR_KEYS,
        manager_params={"timeout": TIMEOUT},
    ) as m:
        return get_hostname(m)


def get_hostname(m: manager) -> str:
    return m.get_config(source="running", filter=hostname_filter)


def print_results(config: str) -> None:
    parsed_cfg = parse_xml_to_dict(config)
    hostname = parsed_cfg["rpc-reply"]["data"]["system"]["config"]["hostname"]
    msg = f"!!! Successfully retrieve data from {hostname} !!!"
    logging.info(msg)
    print(msg)


def parse_xml_to_dict(xml: str) -> dict:
    return xmltodict.parse(xml.xml)


def main():
    try:
        print_results(connect())
    except AuthenticationError as err:
        print(f"Authentication Failed: {err=}")

    except SSHError as err:
        print(f"SSH Connection Failed: {err=}")

    except TimeoutExpiredError as err:
        print(f"Timeout Expired: {err=}")

    except Exception as err:
        print(f"Unexpected {err=}")
    exit()


if __name__ == "__main__":
    main()

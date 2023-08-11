from ncclient import manager
from ncclient.operations.errors import TimeoutExpiredError
from ncclient.transport.errors import SSHError, AuthenticationError


PORT = 830
TIMEOUT = 60
USERNAME = "admin"
PASSWORD = "C1sco12345"
HOSTKEY_VERIFY = False
DEVICE = "sandbox-iosxr-1.cisco.com"
LOOK_FOR_KEYS = False


def connect() -> None:
    with manager.connect(
        host=DEVICE,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=HOSTKEY_VERIFY,
        look_for_keys=LOOK_FOR_KEYS,
        manager_params={"timeout": TIMEOUT},
    ) as m:
        test_connection(m)


def test_connection(m: manager) -> None:
    host = m._session.host
    connected = m._session._connected
    authenticated = m._session.transport.authenticated
    assert connected
    assert authenticated
    print(f"Session {host=}, {connected=}, {authenticated=}")


def main():
    try:
        connect()
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

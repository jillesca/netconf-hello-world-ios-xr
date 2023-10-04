# XR Netconf Test Connection

Simple hello world in netconf to test connectivity to IOS-XR

Restrives hostname using [openconfig-system.yang](https://github.com/openconfig/public/blob/master/release/models/system/openconfig-system.yang) using the `ncclient` library.

```xml
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <system xmlns="http://openconfig.net/yang/system">
        <config>
            <hostname />
        </config>
    </system>
</filter>
```

This script can be useful to monitor continously the status of XR. The goal was to create a keep alive connection, while keeping it at a minimum and verifying is working.

For real use, consider using environment variables rather than hardcoding credentials for your XR instance or device.

For demo purposes, the script connects to the [XR always-On sandbox](https://developer.cisco.com/site/sandbox/), so you can test it right away.

### How to use it

Install dependencies

```bash
pip install -r requirements.txt
```

Run the script

```bash
python hello_world.py
```

Output printed. [Change logger level](hello_world.py#L8) if the output is too much.

```bash
❯ python hello_world.py
INFO:ncclient.transport.ssh:Connected (version 2.0, client Cisco-2.0)
INFO:ncclient.transport.ssh:Authentication (password) successful!
INFO:ncclient.transport.ssh:[host sandbox-iosxr-1.cisco.com session 0x10da0a7a0] Sending:
b'<?xml version="1.0" encoding="UTF-8"?><nc:hello xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:capabilities><nc:capability>urn:ietf:params:netconf:base:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:base:1.1</nc:capability><nc:capability>urn:ietf:params:netconf:capability:writable-running:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:candidate:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:confirmed-commit:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:rollback-on-error:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:startup:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:url:1.0?scheme=http,ftp,file,https,sftp</nc:capability><nc:capability>urn:ietf:params:netconf:capability:validate:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:xpath:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:notification:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:interleave:1.0</nc:capability><nc:capability>urn:ietf:params:netconf:capability:with-defaults:1.0</nc:capability></nc:capabilities></nc:hello>]]>]]>'
INFO:ncclient.transport.ssh:[host sandbox-iosxr-1.cisco.com session 0x10da0a7a0] Received message from host
INFO:ncclient.transport.ssh:[host sandbox-iosxr-1.cisco.com session-id 4088117853] initialized: session-id=4088117853 | server_capabilities=<dict_keyiterator object at 0x10eb65f80>
INFO:ncclient.operations.rpc:[host sandbox-iosxr-1.cisco.com session-id 4088117853] Requesting 'GetConfig'
INFO:ncclient.transport.ssh:[host sandbox-iosxr-1.cisco.com session-id 4088117853] Sending:
b'\n#409\n<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:8f5d39d9-4daf-47b0-b869-44472c96c322"><nc:get-config><nc:source><nc:running/></nc:source><nc:filter> \n        <system xmlns="http://openconfig.net/yang/system">\n            <config>\n                <hostname/>\n            </config>\n        </system>\n    </nc:filter></nc:get-config></nc:rpc>\n##\n'
INFO:ncclient.transport.ssh:[host sandbox-iosxr-1.cisco.com session-id 4088117853] Received message from host
INFO:ncclient.operations.rpc:[host sandbox-iosxr-1.cisco.com session-id 4088117853] Requesting 'CloseSession'
INFO:ncclient.transport.ssh:[host sandbox-iosxr-1.cisco.com session-id 4088117853] Sending:
b'\n#184\n<?xml version="1.0" encoding="UTF-8"?><nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:f1803e08-a68f-44aa-80f8-75226a007917"><nc:close-session/></nc:rpc>\n##\n'
INFO:ncclient.transport.ssh:[host sandbox-iosxr-1.cisco.com session-id 4088117853] Received message from host
INFO:root:!!! Successfully retrieved hostname from R1 !!!
!!! Successfully retrieved hostname from R1 !!!
```

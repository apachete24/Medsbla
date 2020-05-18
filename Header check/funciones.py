import json
import requests
from ncclient import manager
import xml.dom.minidom
from netmiko import ConnectHandler

# enviar un comando por ssh
def ssh_command (command):


    ssh_client = ConnectHandler(

        device_type = 'cisco_ios',
        host = '64.103.37.51',
        port = '8181',
        username = 'developer',
        password = 'C1sco12345',
    )

    output = ssh_client.send_command(command)
    return output






# nueva interfaz con netconf
def new_if (name, ip, mask, description):


    m = manager.connect(
        host = "64.103.37.51",
        port = "10000",
        username = "developer",
        password = "C1sco12345",
        hostkey_verify = None
    )

    new_if = """
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <Loopback>
                        <name>{}</name>
                        <description>{}</description>
                        <ip>
                            <address>
                                <primary>
                                    <address>{}</address>
                                    <mask>{}</mask>
                                </primary>
                            </address>
                        </ip>
                    </Loopback>
                </interface>
            </native>
        </config>
        """.format(name, description, ip, mask)
    try:
        netconf_reply = m.edit_config(target="running", config=new_if)
    except:
        print("Check your input")
        exit()
    print("Interface added successfully")
    return netconf_reply





# eliminar interfaz con ssh
def remove_if (if_name):


    ssh_client = ConnectHandler(

        device_type = 'cisco_ios',
        host = '64.103.37.51',
        port = '8181',
        username = 'developer',
        password = 'C1sco12345',
    )

    config_commands = ["no int {}".format(if_name)]

    out_config = ssh_client.send_config_set(config_commands)
    print("Configuracion realizada en el dispositivo:\n{}".format(out_config))
    output_command = ssh_client.send_command("sh ip int br")
    print("\n\n Interfaces:\n{}".format(output_command))

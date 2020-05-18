from ncclient import manager
import xml.dom.minidom
import xmltodict
import json
import pprint
import treetojson


pp = pprint.PrettyPrinter(indent=4, compact=False)

m = manager.connect(
        host = "64.103.37.51",
        port = "10000",
        username = "developer",
        password = "C1sco12345",
        hostkey_verify = None
    )

conf = m.get_config(source="running")
conf_xml = xml.dom.minidom.parseString(conf.xml).toprettyxml()
conf_json = xmltodict.parse(conf_xml)


from funciones import *
import json
import requests
import urllib3
import pprint


urllib3.disable_warnings()

url = "https://medsblalabs.com/"
headers = {
    "Accept": "*/*",
    "Accepts Encoding": "gzip,deflate,br",
    "Connection": "keep-alive"

}

resp = requests.get(url, headers=headers, verify=False)
headers = resp.headers

warnings = evaluate_warn(headers)
print("\n{} security headers are incorrect".format(warnings))


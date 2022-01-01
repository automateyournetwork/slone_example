import requests
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
sl1_template = env.get_template('SLOneDevice.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

sl1 = "student01.sciencelogic.com"

# -------------------------
# Allowed Protocols
# -------------------------

device = requests.request("GET", f"https://{ sl1 }/api/device/1", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
deviceJSON = device.json()

logs = requests.request("GET", f"https://{ sl1 }/{ deviceJSON['logs']['URI']}", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
logsJSON = logs.json()

apps = requests.request("GET", f"https://{ sl1 }/{ deviceJSON['applications']['URI']}", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
appsJSON = apps.json()

performance_data = requests.request("GET", f"https://{ sl1 }/{ deviceJSON['performance_data']['URI']}", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
performance_dataJSON = performance_data.json()

config_data = requests.request("GET", f"https://{ sl1 }/{ deviceJSON['config_data']['URI']}", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
config_dataJSON = config_data.json()

vitals = requests.request("GET", f"https://{ sl1 }/{ deviceJSON['vitals']['URI']}", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
vitalsJSON = vitals.json()

interfaces = requests.request("GET", f"https://{ sl1 }/{ deviceJSON['interfaces']['URI']}", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
interfacesJSON = interfaces.json()

thresholds = requests.request("GET", f"https://{ sl1 }/{ deviceJSON['thresholds']['URI']}", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
thresholdsJSON = thresholds.json()

details = requests.request("GET", f"https://{ sl1 }/{ deviceJSON['details']['URI']}", headers=headers, auth=('student', 'CHANGEPASSWORD'), verify=False)
detailsJSON = details.json()

parsed_output = sl1_template.render(
    sl1 = sl1,
    device = deviceJSON,
    logs = logsJSON['result_set'],
    apps = appsJSON['result_set'],
    perf = performance_dataJSON['result_set'],
    conf = config_dataJSON['result_set'],
    vitals = vitalsJSON,
    interfaces = interfacesJSON['result_set'],
    thresholds = thresholdsJSON,
    details = detailsJSON
    )

with open("SLOne_Device.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()
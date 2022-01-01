import requests
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
brainfreeze_template = env.get_template('SLOneDevice.j2')

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

device = requests.request("GET", f"https://{ sl1 }/api/device/1", headers=headers, auth=('student', ''), verify=False)
deviceJSON = device.json()

parsed_output = brainfreeze_template.render(
    sl1 = sl1,
    device = deviceJSON
    )

with open("SLOne_Device.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()
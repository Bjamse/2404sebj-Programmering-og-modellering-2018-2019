import requests
import re

username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.get(url, auth=(username, password))

content = r.text
print(content)
# print("\n\nthe password for next level = ", re.findall("11:(.*)", content)[0])

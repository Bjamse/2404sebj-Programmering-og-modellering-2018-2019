import requests
import re

username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.get(url, auth=(username,password))

content = r.text

print("the password for next level = ", str(re.findall("<!--The password for natas2 is (.*) -->", content)))

import requests
import re

username = "natas0"
password = username

url = 'http://natas0.natas.labs.overthewire.org'
r = requests.get(url, auth=(username,password))

content = r.text

print("the password for next level = ", str(re.findall("<!--The password for natas1 is (.*) -->", content)))

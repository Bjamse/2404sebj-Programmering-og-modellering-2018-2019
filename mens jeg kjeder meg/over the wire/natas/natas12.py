import requests
import re

username = "natas12"
password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.post(url, auth=(username, password))

content = r.text
print(content)
#print("\n\nthe password for next level = ", re.findall("12 is (.*)", content)[0])

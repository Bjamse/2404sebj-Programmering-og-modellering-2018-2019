import requests
import re

username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

secret = "oubWYf2kBq"

""" 
secret was obtained by reversing the source-code:

bin2hex(strrev(base64_encode($secret))) --> base64_decode(strrev(hex2bin($secret)));
"""


url = 'http://{}.natas.labs.overthewire.org'.format(username)
r = requests.post(url, auth=(username, password), data={"submit": "", "secret": secret})


print("\n\nthe password for next level = ", re.findall("natas9 is (.*)", r.text)[0])

import requests


r = requests.get("http://hdwhite.org/puzzle/newfolder/solitaire.htm")

print(r.text)
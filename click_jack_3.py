#/usr/bin/python3

import requests

print("     ***   Click Jack ING   ***      ")
print("Please, an url! (http://www.example.com)")
url = input("Url: ")
request = requests.get(url)
print(request)
header = str(request.headers)
if "X-Frame-Options" in header:
        print("Let's search an other target!")
else:
        print("Framing is possible!")


import requests

print(requests.__version__)

print(requests.get("https://raw.githubusercontent.com/tpan49/cmput404_lab1/master/find_version.py").text)

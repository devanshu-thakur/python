import requests
import re
url = "https://iiitbhopal.ac.in/Document/ss/CSE-1001.html"
response=requests.get(url)
html=response.text
print(html)

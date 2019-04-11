import urllib.request
import requests
response = urllib.request.urlopen('http://www.baidu.com/')
html = response.read().decode("utf-8")
print(html)

print(response.status)
print(response.getheaders())
print(response.getheader("Server"))
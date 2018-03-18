import urllib.request
url = "http://ip.sxisa.com"
web = urllib.request.urlopen(url)
print(web.read())
import urllib.request
url = "http://www.myip.cn/"
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")
a = html.find('您的IP地址:')+8
b = html.find('<',a)
c = html.find('来自:')+4
d = html.find('.',c)
print("您的IP地址：",html[a:b])
print("地区：",html[c:d][0:6])
print("运营商：",html[c:d][7:9])


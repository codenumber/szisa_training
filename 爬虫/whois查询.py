import urllib.request
from  bs4  import  BeautifulSoup
import re
import  urllib.parse
def get_url(content):
    url = "http://whois.chinaz.com/?DomainName="+content
    headers = {}
    headers[
        'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    headers =urllib.parse.urlencode(headers).encode("utf-8")
    request = urllib.request.Request(url, headers)

    req = urllib.request.urlopen(url)
    html = req.read().decode("utf-8")
    return html

def show():
    html = get_url(content)
    soup = BeautifulSoup(html,"html.parser")


    show = soup.find("ul",id = "sh_info")
    show_1 = show.get_text("\n",strip = True)
    show_2 = re.sub("(\[whois(\s){0,1}反查\])",'',show_1)
    show_3 = re.sub("-*站长之家\sWhois查询\D+",'',show_2)
    print(show_3)

if __name__ == "__main__":
    content = input("请输入您想要查询的网址：")
    show()
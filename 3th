import bs4
import requests
from bs4 import BeautifulSoup

def getHYMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

def fillDimondList(dlist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:#查找
        if isinstance(tr,bs4.element.Tag):#解析
            tds = tr('td')
            dlist.append([tds[0].string,tds[1].string,tds[2].string])

def printDimondlist(dlist,num):
    print("{:^10}\t{:^6}".format("价格""商品名称"))
    for i in range(num):
        d=dlist[i]
        print("{:^10}\t{:^6}".format(d[0],d[1]))
    print("suo"+str(num))

def main():
    dinfo = []
    url = 'http://s.taobao.com/search?q=%E9%92%BB%E6%88%92&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191005&ie=utf8'
    html = getHYMLText(url)
    fillDimondList(dinfo,html)
    printDimondlist(dinfo,20)#此处且列20个

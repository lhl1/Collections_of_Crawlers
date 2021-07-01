import webbrowser
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep, time
from lxml import etree
import os
import re
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
}

url = 'https://www.bilibili.com/v/popular/rank/all'
print("                     LHL's bilibili Top 100")
source = requests.get(url=url, headers=headers).text
tree = etree.HTML(source)
card_list = tree.xpath('//*[@id="app"]/div[2]/div[2]/ul/li')
cnt = 1
for i in card_list:
    try:
        title = i.xpath('./div[2]/div[2]/a//text()')[0]
        bofangliang = i.xpath('./div[2]/div[2]/div[1]/span[1]/text()')[0]
        bofangliang = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", bofangliang)

        danmushuliang = i.xpath('./div[2]/div[2]/div[1]/span[2]/text()')[0]
        danmushuliang = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", danmushuliang)
        Up = i.xpath('./div[2]/div[2]/div[1]/a/span/text()')[0]
        Up = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", Up)

        url = 'https:' + i.xpath('./div[2]/div[2]/a/@href')[0]
        print(str(cnt)+'. '+title)
        print('     UP：' + Up)
        print('     播放量：' + bofangliang)
        print('     弹幕量：' + danmushuliang)

        print('     地址：' + url)
        print()
        print()
        cnt=cnt+1
    except:
        continue
os.system('pause')

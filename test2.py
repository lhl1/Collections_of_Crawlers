import tkinter as tk
import requests
import re
from lxml import etree
import subprocess
import _thread
import time
import json


flag = ''
delay_time=62

def zhihu2( ):
    global flag
    flag = 'bilibili'
    while flag == 'bilibili':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
        }
        # t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                   LHL's 虎嗅文章      ") + time.strftime("%H:%M:%S", time.localtime()) + "\n\n"
        url = 'https://it.ithome.com/'
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding  # 使用自动检测的编码
        source = response.text
        print(source)
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="list"]/div[1]/ul/li')
        cnthuxiu = 1
        for i in card_list:  # lhlhlhlhl罗宏亮
            try:
                str1 = str1 + "  " + str(cnthuxiu) + ".   " + i.xpath('./div/div[1]/text()')[0] + '\n'
                str1 = str1 + "       " + i.xpath('./div/h2/a/@title')[0] + '\n'
                str1 = str1 + "       " + i.xpath('./a/@href')[0] + '\n'
                cnthuxiu = cnthuxiu + 1

            except:
                continue
        # t.insert(1.0, str1)

        time.sleep(delay_time)



def huxiu(threadName, delay):
    global flag
    flag='huxiu'
    while flag=='huxiu':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'cookies':'huxiu_analyzer_wcy_id=3ufl2f5cnp5wdfyvwszx; Hm_lvt_502e601588875750790bbe57346e972b=1700101345; hx_object_visit_referer_1_2393353=+'
        }
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                   LHL's 虎嗅文章      ") +time.strftime("%H:%M:%S", time.localtime())+ "\n\n"
        url = 'https://it.ithome.com/'
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding  # 使用自动检测的编码
        source = response.text
        print("start")
        print(source)
        tree = etree.HTML(source)
        card_list = tree.xpath('/html/body/div[7]/div[2]/div[1]/ul[1]/li')
        cnthuxiu = 1
        for i in card_list:  # lhlhlhlhl罗宏亮
            try:
                str1 = str1 + "  " + str(cnthuxiu) + ".   " + i.xpath('./div[2]/div[1]/a')[0] + '\n'
                str1 = str1 + "  " + str(cnthuxiu) + ".   " + i.xpath('./div[2]/div[2]/text()')[0] + '\n'

                str1 = str1 + "       " + i.xpath('./div[2]/div[1]/a/@href')[0] + '\n\n'
                cnthuxiu = cnthuxiu + 1

            except:
                continue
        t.insert(1.0, str1)
        time.sleep(delay_time)





zhihu2()
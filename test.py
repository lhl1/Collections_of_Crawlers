import requests
import time
import xlrd
import xlwt
import csv
import os
import re
from lxml import etree


def weibo():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    }
    # lhlhlhlhl罗宏亮
    url = 'https://s.weibo.com/top/summary'
    lists = requests.get(url=url, headers=headers).text
    tree = etree.HTML(lists)
    cnt = 1
    titles = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
    print('                     微博Top50')# lhlhlhlhl罗宏亮
    # lhlhlhlhl罗宏亮
    for i in titles:
        title = i.xpath('./td[2]/a/text()')[0]
        url = 'https://s.weibo.com' + i.xpath('./td[2]/a/@href')[0]
        print(str(cnt) + '.' + title)

        print()
        cnt = cnt + 1
    os.system('pause')
# lhlhlhlhl罗宏亮

def zhihutop():
    # lhlhlhlhl罗宏亮
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'cookie': 'q_c1=86516ea434074823a7d4d5b6829e693f|1621914360000|1621914360000; _zap=1d126649-a8a6-44dc-9008-d3845083bb73; d_c0="AHBfx5bDIxOPTqfKDjf2ZtkKki6ktkAnAnM=|1621597597"; captcha_session_v2="2|1:0|10:1621608362|18:captcha_session_v2|88:T2ZBRlpCRm5TWXpxZ3J2d0hCbXNWUktVUWE2L0pvUWgvVzVGL2hTdk9CMS9icmw1ZDA2bHVheTNyYTRNUTRQNw==|41476ca8e6e774ad041bbccf216d137adf322da91599b652ea8c4e1c43638213"; __snaker__id=XPEdiJ6e5OFYgo6C; _9755xjdesxxd_=32; gdxidpyhxdE=eXYXNfQLVtKBHavjJeq6xOe1aTJCupvj%2BzC3WwYRp%2BXv%2FleMji6Eaz0VyNKDEjljJ9VKxDgMa3b67C9nbsgy%5CHkLqxGmESb1%2Ft4tYTdgOlDGyvINHZbSgg2h6Wvj%2BBMidqULtBWBhgiG5V91K6lZL6JmKwciPzcILvOoagBEZopQQUqc%3A1621609264235; YD00517437729195%3AWM_NI=7WLs7hQNYLQJccjYHVyKq1h59LuoJ5jUxKIEcUIUSzFluXz1%2BPglgsROVxcRHVD6WsNaSICVweqBUNHaXWPViIOa7dV8xETrVJU6QG%2FUkoZnfNDA7zOUaKsyVKYiUqK%2FaGo%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eebafb68bbafb8baaa5fa6b48aa3d55a868b9a85f164f889e187d57eedb8b889d52af0fea7c3b92af5898494b664939297add442a1bda6bacb5ebb95bfd2eb3ffb94bb90c93faa8bb8accc4fa18b87b6d27286b4bbb9f93be990a98de67992919a99e25a8c8a8cd7d6798ebf9daac25eb5bbbfa3d8468cbf98b8d35eab978182b67096e8b8a6d77a96969bd7d44ded8ba590d966a6928ca2b6728d8bafacf2739695978ad87b89f1afa8ee37e2a3; YD00517437729195%3AWM_TID=TjFmoEn%2FiIpAVQVUEBMug4XqLF%2B%2BhgkB; captcha_ticket_v2="2|1:0|10:1621608369|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfeExoMmpzRzV0WUxBckNCeFdvaUZrOWI4X0phSDR2b3prZm5oNXlsd3pxT2Q5MmNTc1ltSWotblFadjVuTUFMTkEyeTRRZmxqeDJkU21vMGtNdG55UElzNW5VOExWTE5TdENNRzVuazRlUWNzSzBIN3FkNldtTGplSFp5UTB6TWFmVG9wLjgycEl1cTgtTVVBRFJaWDdMaGpJalNCbkZ0X09ZLkVvYnVBYk9uSDBaSlpMWVpPRVIyNzBpOWl3QmJJdUguSlM0ZVMxZG9DcDdrczFxbWFjcWJqSmJLUzVVUjdVNXQuQUE3eEZFU2xmOTJBTERrV0RhMG1GbEVVNlVjMk9ySU1fVHJORm84LjQuaWdwSUQ5Vm5FNFBpd1U0dHpTSDJieHhSck5BUzAuRGwxbDhhRjh4Q1RmOXVQTVE4VmRMWEl3bDRXU3lEZmp6eG1tTGdRdDlwN2l2NlF4aUxDR0hrWXZtSVZfY01nYXN0dDFRcGZvLm9CNzhZMWt0QW5zYWIxWTk0OUxvaU02R1EyMU92U3Z5bFljLjBCZDhUby5jQlVScXlBVjlsMTVKOXFNOG9FTHpuN2JvMUo1cHRkV3lNbFZoaHlUV05tWUtIeWtMQlBvdnh2bG8tOG1CbklNMGFhcHp2Rld6dHdJWnY1V05IZklILThWeEZOMyJ9|3c90701add76c0b9ffba272c5477c46631c21283963ec97ffac2e52d0d292779"; z_c0="2|1:0|10:1621608370|4:z_c0|92:Mi4xZDhRY0FnQUFBQUFBY0ZfSGxzTWpFeVlBQUFCZ0FsVk5zaFdWWVFBX2N4Y2toSUNnRlpHVHdRdnAxWVE2M0ZKMll3|d3983d430eaa78411e81e1bc559b0847c8786876d1f3e6dca11f8338bd7589d8"; _xsrf=mvJrLLiq4vq61EVfTwFSsMCwze83B9rA; tshl=; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1623856533,1623915379,1623915623,1624110755; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1624110755; SESSIONID=BbFdUlyFveD5a6Tv0sUjCxHM8SMJQXhAQG4UrU1pCwM; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1624110755|1624108499; JOID=VVgRBEpkxHFEbLBFWWRF70_wc2dJIaI0Jj_bOBwUpjFyC4AWK8Q1uSRts0JcSvCkbw9vs_LF0a1YlB298D2pR5U=; osd=UFkdA0xhxX1DarVEVWND6k78dGFMIK4zIDraNBsSozB-DIYTKsgyvyFsv0VaT_GoaAlqsv7C16hZmBq79TylQJM='
    }
    url = 'https://www.zhihu.com/hot'
    lists = requests.get(url=url, headers=headers).text
    tree = etree.HTML(lists)  # lhlhlhlhl罗宏亮
    cnt = 1
    print('                                 知乎Top')
    print()  # lhlhlhlhl罗宏亮
    titles = tree.xpath('//*[@id="TopstoryContent"]/div/div/div[2]/section')
    for i in titles:
        title = i.xpath('./div[2]/a/h2/text()')[0]
        url = i.xpath('./div[2]/a/@href')[0]
        # lhlhlhlhl罗宏亮
        # lhlhlhlhl罗宏亮
        print(str(cnt) + '.' + title)
        print('         ' + url)
        print()
        cnt = cnt + 1
    os.system('pause')

def bilibili():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }

    url = 'https://www.bilibili.com/v/popular/rank/all'
    print("                     LHL's bilibili Top 100")
    source = requests.get(url=url, headers=headers).text
    tree = etree.HTML(source)
    card_list = tree.xpath('//*[@id="app"]/div[2]/div[2]/ul/li')
    cnt = 1# lhlhlhlhl罗宏亮
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
            print(str(cnt) + '. ' + title)
            print('     UP：' + Up)
            print('     播放量：' + bofangliang)
            print('     弹幕量：' + danmushuliang)

            print('     地址：' + url)
            print()
            print()
            cnt = cnt + 1
        except:# lhlhlhlhl罗宏亮
            continue
    os.system('pause')


def huxiu():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    print("                   LHL's 虎嗅文章")
    url = 'https://www.huxiu.com/article/'
    source = requests.get(url=url, headers=headers).text
    tree = etree.HTML(source)
    card_list = tree.xpath('//*[@id="top"]/div')
    cnt = 1
    for i in card_list:# lhlhlhlhl罗宏亮
        try:
            title = i.xpath('./div/div/a/div[1]/img/@alt')[0]
            url_tail = 'https://www.huxiu.com' + i.xpath('./div/div/a/@href')[0]
            print(str(cnt) + '.' + title)
            print('         ', url_tail)
            print()
            print()
            cnt = cnt + 1
        except:
            continue
    os.system('pause')
def game_list():

    cnt = 1
    count = 0
    flag = 1
    print("                     LHL' Game List")

    url_head = 'https://bbs.3dmgame.com/'
    while True:
        url = 'https://bbs.3dmgame.com/forum-game0day-{}.html'.format(cnt)
        source = requests.get(url=url).text
        tree = etree.HTML(source)
        title = tree.xpath("//a[@style='font-weight: bold;color: #EE1B2E;']")

        for i in title:
            title_m = i.xpath('./text()')[0]
            url_m = url_head + i.xpath('./@href')[0]
            if (title_m[0] == '【') & (ord(title_m[1]) >= 48) & (ord(title_m[1]) <= 57):
                print(title_m)
                print(url_m)

                count = count + 1
                if count >= int(10):
                    flag = 0
                    break# lhlhlhlhl罗宏亮
        cnt = cnt + 1
        if flag == 0:
            break

    # with open('./1.html','w',encoding='utf-8') as fp:
    #     fp.write(source)

def douban_movies():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    print("                   LHL's Latest Movie")# lhlhlhlhl罗宏亮
    url = 'https://movie.douban.com/'
    source = requests.get(url=url, headers=headers).text
    tree = etree.HTML(source)
    title_list = tree.xpath('//*[@id="screening"]/div[2]/ul/li')
    for i in title_list:
        try:
            title = i.xpath("./@data-title")[0]
            pingfen = i.xpath('./ul/li[3]/span[2]//text()')[0]# lhlhlhlhl罗宏亮
            place = i.xpath("./@data-region")[0]
            shichang = i.xpath("./@data-duration")[0]
            director = i.xpath("./@data-director")[0]
            actors = i.xpath("./@data-actors")[0]
            url = i.xpath('./ul/li[2]/a/@href')[0]
            print(title)
            print('    评分:', pingfen)
            print('    导演:', director)
            print('    主演:', actors)
            print('    国家地区:', place)
            print('    时长:', shichang)# lhlhlhlhl罗宏亮
            print('    地址:', url)
            print()
            print()
        except:
            continue

    os.system("pause")


# lhlhlhlhl罗宏亮
if __name__ == "__main__":
    while True:# lhlhlhlhl罗宏亮
        print("                     LHL's Collections of Crawlers")
        print("         0.   退出")
        print("         1.   微博热搜")# lhlhlhlhl罗宏亮
        print("         2.   知乎热榜")
        print("         3.   Bilibili TOP")
        print("         4.   虎嗅最新文章")
        print("         5.   Game List")
        print("         6.   豆瓣最新电影")
        choose = input("请输入：\n")
        if choose == '0':
            break
        if choose == '1':
            weibo()
            print("微博热搜爬取完毕！")
        if choose == '2':
            zhihutop()
            print("知乎热榜爬取完毕！")
        if choose == '3':
            bilibili()# lhlhlhlhl罗宏亮
            print("Bilibili TOP爬取完毕！")
        if choose == '4':
            huxiu()
            print("虎嗅最新文章爬取完毕！")
        if choose == '5':
            game_list()
            print("Game List爬取完毕！")
        if choose == '6':
            douban_movies()# lhlhlhlhl罗宏亮
            print("豆瓣最新电影爬取完毕！")



import tkinter as tk
import requests
import re
from lxml import etree
import subprocess
import _thread
import time
import pyautogui
import webbrowser
# 获取屏幕宽度和高度
screen_width, screen_height = pyautogui.size()

cmd = 'your command'
res = subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
window = tk.Tk()


window.title("LHL's Information")
window.iconbitmap('favicon.ico')
new_window = tk.Toplevel(window)




#根据当前屏幕分辨率计算窗口大小
set_w=int(screen_width/1.6)
set_h=int(screen_height/1.5)
str_set_w_h=str(set_w)+"x"+str(set_h)
window.geometry(f"{str_set_w_h}+{int(screen_width/6)}+{int(screen_height/6)}")

global to_url
to_url=''
flag = ''
delay_time=62


def bring_to_front(event):
    # 将窗口移到最前面

    window.lift()
    new_window.deiconify()
    new_window.lift()

def on_restore(event):
    # 当复原主窗口时，复原所有窗口
    try:

        window.deiconify()
        new_window.deiconify()
        new_window.lift()
        bring_to_front()
    except:
        pass

def update_position(event=None):
        try:
            new_window.geometry(f"{200}x{window.winfo_height() + 60}")
            x_offset = window.winfo_x() - new_window.winfo_width() + 12
            y_offset = window.winfo_y()
            new_window.geometry(f"+{x_offset}+{y_offset}")
        except:
            pass




def on_minimize(event):
    # 当最小化主窗口时，最小化所有窗口
    try:
        window.iconify()
        new_window.geometry(f"{0}x{0}")
        new_window.iconify()


    except:
        pass

def new_window_add_button():
    newWindow_uncloseMin()
    # 初次设置位置
    # update_position()

    # 监听主窗口的移动事件

    button1 = tk.Button(new_window, text="微博热榜", command=start_weibo)
    button2 = tk.Button(new_window, text="百度热榜", command=start_baidu_time)
    button3 = tk.Button(new_window, text="知乎热榜", command=start_zhihu2)
    button4 = tk.Button(new_window, text="哔哩哔哩", command=start_bilibili)
    button5 = tk.Button(new_window, text="虎嗅热文", command=start_huxiu)
    button6 = tk.Button(new_window, text="豆瓣热门电影", command=start_douban_movies)
    button7 = tk.Button(new_window, text="游戏下载", command=start_game_list)
    button8 = tk.Button(new_window, text="游民星空资讯", command=start_gamesky)
    button9 = tk.Button(new_window, text="IT之家资讯", command=start_itZHome)
    button1.pack(fill=tk.X)
    button2.pack(fill=tk.X)
    button3.pack(fill=tk.X)
    button4.pack(fill=tk.X)
    button5.pack(fill=tk.X)
    button6.pack(fill=tk.X)
    button7.pack(fill=tk.X)
    button8.pack(fill=tk.X)
    button9.pack(fill=tk.X)

    # 绑定最小化事件

def newWindow_uncloseMin():
    try:
        # 隐藏标题栏和边框
        new_window.overrideredirect(1)
        # 隐藏最小化和最大 化按钮
        new_window.attributes("-toolwindow", 1)
        new_window.geometry(f"{60}x{window.winfo_height()}")

    except:
        pass

def delete_text():
    global str1
    t.delete(1.0, 'end')
    str1 = ''


def open_url(event):
    print(to_url)
    webbrowser.open(to_url)




def weibo(threadName, delay):
    global flag
    flag='weibo'
    while flag=='weibo':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'SINAGLOBAL=6741639331961.842.1636351443105; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5merwV-edKPy4zi1nWB2WF; UOR=,,tophub.today; SUB=_2AkMWxpZdf8NxqwJRmfsUyWzjb49-wgHEieKgmmeGJRMxHRl-yT8XqmAktRB6PUa4sKj9bCE81uS9DWuk-pvHv3CkQsSr; _s_tentry=tophub.today; Apache=9191740774784.104.1637667572390; ULV=1637667572470:9:9:2:9191740774784.104.1637667572390:1637636253119'
        }
        # lhlhlhlhl罗宏亮
        url = 'https://s.weibo.com/top/summary'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)
        cnt = 1
        titles = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
        str1 = ''
        t.delete(1.0, 'end')
        t.insert("end",'                     微博Top50' + "       " + time.strftime("%H:%M:%S", time.localtime())+'\n\n')

        # lhlhlhlhl罗宏亮
        for i in titles:
            title = i.xpath('./td[2]/a/text()')[0]
            num = i.xpath('./td[1]/text()')
            if (len(num) > 0):
                num_print = num[0]
            else:
                num_print = '置顶'
            url = 'https://s.weibo.com' + i.xpath('./td[2]/a/@href')[0]
            url = 'https://s.weibo.com' + i.xpath('./td[2]/a/@href')[0]
            t.insert("end", "  "+num_print + '.   ' + title + '\n\n')

            cnt = cnt + 1

        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_weibo():

    try:
        _thread.start_new_thread(weibo, ("weibo", 0))
    except:
        print("Error: 无法启动线程")

def zhihu2(threadName, delay):
    global flag
    flag='zhihu2'
    while flag=='zhihu2':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': '_zap=9db88ca6-1a56-499a-8714-322f8b14e23c; d_c0=AJBTSVh4kBePTpHEdwKkZ7L_1BjVC_Ice9c=|1697612215; __snaker__id=He0SicnrqSWD2It9; YD00517437729195%3AWM_NI=R6%2BlnP8yDhj4p1im4u1J205SPpLPrN8TDApy%2Fu5Xbfxjs2v9ONRlfo5%2BmisjXdcUQH9QpReCfBH2yAb1DwbgUutcDqosiy6JR2Axsmil%2FEG5Vp6L9ILH6eHpxw014YO4cFQ%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed5f34a92af8dd5ae39fbb08aa2c44f879e9ab1d139af8b8dd1eb3990f0a092d02af0fea7c3b92a92eae58ded5cfca78c89e940b4efa78eb77ff396fed1b85994b084b1f146fc8c8ca2f373edabfbb9e16ebcb6bdd3f5338d929e8de565f7f5a38af2629cbcadb6d444fb8fc0b3e849a69e88d3fc4ba2ef8c98e16d97abbc84c77badada79ab54292ee8f99f267abb4e1a6c63f96b0faadbc439098fa86cb7cbca900d2b7538decada7d437e2a3; YD00517437729195%3AWM_TID=w3FE8Nfu1xxERVRVAVOQ2yBCwgyOhKrM; q_c1=2f480dd8f7c94280b4282f0f5e8d1a7f|1697612222000|1697612222000; z_c0=2|1:0|10:1700401607|4:z_c0|80:MS4xZDhRY0FnQUFBQUFtQUFBQVlBSlZUY2RmUjJZWGhVN0VRWWZ6Uk51ZHRyQVdrOWVQNEtjSHFnPT0=|d360175f34ebc738f25d54a3f69b1186e41cb602f5460f7bd156c28e37d22158; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1699764468,1699875669,1700401608,1700740933; tst=h; _xsrf=7decaf0f-4bf3-4440-b5bd-3e1f09fef6ca; KLBRSID=fe78dd346df712f9c4f126150949b853|1702088288|1702088284; SESSIONID=hDPHgdBm9xL2rAIcpU6zigMzPJXxxWbmUR7oswgF7Id'}
        # lhlhlhlhl罗宏亮
        url = 'https://www.zhihu.com/hot'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)
        cnt = 1

        '//*[@id="TopstoryContent"]/div/div[2]/div[1]/section[4]'
        '//*[@id="TopstoryContent"]/div/div[2]/div[1]/section[8]'
        '//*[@id="TopstoryContent"]/div/div[2]/div[1]/section[5]/div[2]/a/h2'
        '//*[@id="TopstoryContent"]/div/div[2]/div[1]/section[4]/div[1]/div[1]'

        '//*[@id="TopstoryContent"]/div/div[2]/div[1]/section[4]/a'
        titles = tree.xpath('//*[@id="TopstoryContent"]/div/div[2]/div[1]/section')
        str1 = ''
        t.delete(1.0, 'end')
        t.insert("end",'                     知乎热榜' + "       " + time.strftime("%H:%M:%S", time.localtime())+'\n\n')
        #
        # # lhlhlhlhl罗宏亮
        for i in titles:
             title = i.xpath('./div[2]/a/h2/text()')[0]
             num = i.xpath('./div[1]/div[1]/text()')
             if (len(num) > 0):
                 num_print = num[0]
             else:
                 num_print = '置顶'
             url = i.xpath('./a/@href')[0]

             t.insert("end", "  "+num_print + '.   ' + title + '\n')
             t.insert("end", '            ' + url + '\n\n')
             cnt = cnt + 1

        t.insert(1.0, str1)
        time.sleep(delay_time)
def start_zhihu2():
    try:
        _thread.start_new_thread(zhihu2, ("zhihu2", 0))
    except:
        print("Error: 无法启动线程")

def M_Team_torrents(threadName, delay):
    global flag
    flag = 'M_Team_torrents'
    while flag == 'M_Team_torrents':
        url = 'https://kp.m-team.cc/torrents.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'tp=ODEyYTRiMDZkOTJlNzI1NWM5YWYyYzc4OWUwZTA4YTMwMTA0M2RmMg%3D%3D; cf_clearance=Afo0uinFmvVjdXVNykSqVJB8ssUhT1zEIqp.D0s_r50-1649045406-0-150'
        }
        t.delete(1.0, 'end')
        t.insert("end",'                     M_Team_torrents' + "       " + time.strftime("%H:%M:%S", time.localtime()) + '\n\n')
        lists = requests.get(url=url, headers=headers).text


        lists_json1 = re.compile(
            '<td class="torrenttr".*?<a title="(.*?)" href="(.*?)">.*?><br />(.*?)<',
            re.S)
        lists_json2 = re.compile(
            '<span title=".*?">(.*?)<br />(.*?)</span></td><td class="rowfollow">(.*?)<br />(.*?)</td>',
            re.S)
        json_get1 = re.findall(lists_json1, lists)
        json_get2 = re.findall(lists_json2, lists)

        cnt = 1
        for i in range(0, len(json_get1)):
            title = json_get1[i][0]
            urlthis = url + json_get1[i][1]
            title1 = json_get1[i][2]

            size = json_get2[i][2] + json_get2[i][3]

            t.insert("end","  " + str(cnt) + ".  " + title + "      " + size+'\n')
            t.insert("end","          " + title1+ '\n\n')
            t.insert("end","                         " + urlthis+ '\n\n\n')
            cnt = cnt + 1
        t.insert(1.0, '')
        time.sleep(delay_time*5)

def start_M_Team_torrents():

    try:
        _thread.start_new_thread(M_Team_torrents, ("M_Team_torrents", 0))
    except:
        print("Error: 无法启动线程")






def M_Team_offers(threadName, delay):
    global flag
    flag = 'M_Team_offers'
    while flag == 'M_Team_offers':
        url = 'https://kp.m-team.cc/offers.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'tp=ODEyYTRiMDZkOTJlNzI1NWM5YWYyYzc4OWUwZTA4YTMwMTA0M2RmMg%3D%3D; cf_clearance=Afo0uinFmvVjdXVNykSqVJB8ssUhT1zEIqp.D0s_r50-1649045406-0-150'
        }
        t.delete(1.0, 'end')
        t.insert("end",'                     M_Team_offers' + "       " + time.strftime("%H:%M:%S", time.localtime()) + '\n\n')
        lists = requests.get(url=url, headers=headers).text


        lists_json1 = re.compile(
            '<td class="torrenttr".*?<a title="(.*?)" href="(.*?)">.*?><br />(.*?)<',
            re.S)
        lists_json2 = re.compile(
            '<span title=".*?">(.*?)<br />(.*?)</span></td><td class="rowfollow">(.*?)<br />(.*?)</td>',
            re.S)

        json_get1 = re.findall(lists_json1, lists)
        json_get2 = re.findall(lists_json2, lists)

        cnt = 1
        for i in range(0, len(json_get1)):
            title = json_get1[i][0]
            urlthis = url + json_get1[i][1]
            title1 = json_get1[i][2]
            size = json_get2[i][2] + json_get2[i][3]
            t.insert("end","  " + str(cnt) + ".  " + title + "      " + size+'\n')
            t.insert("end","          " + title1+ '\n')
            t.insert("end","         "  +urlthis+ '\n\n')
            cnt = cnt + 1
        t.insert(1.0, '')
        time.sleep(delay_time*5)

def start_M_Team_offers():

    try:
        _thread.start_new_thread(M_Team_offers, ("M_Team_offers", 0))
    except:
        print("Error: 无法启动线程")


def M_Team_upload(threadName, delay):
    global flag
    flag = 'M_Team_upload'
    url = 'https://kp.m-team.cc/getusertorrentlistajax.php?userid=266830&type=uploaded'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'Cookie': 'tp=ODEyYTRiMDZkOTJlNzI1NWM5YWYyYzc4OWUwZTA4YTMwMTA0M2RmMg%3D%3D; cf_clearance=Afo0uinFmvVjdXVNykSqVJB8ssUhT1zEIqp.D0s_r50-1649045406-0-150'
    }

    t.delete(1.0, 'end')
    t.insert("end",'                     M_team_Upload' + "       " + time.strftime("%H:%M:%S", time.localtime()) + '\n\n')



    lists = requests.get(url=url, headers=headers).text
    lists_json = re.compile(
        '<img class=.*?title="50%".*?<br />(.*?)</td><td class="rowfollow" align="center">(.*?)<br />(.*?)</td>',
        re.S)
    json_get = re.findall(lists_json, lists)

    cnt = 1
    for i in range(0, len(json_get)):
        title = json_get[i][0]
        size = json_get[i][1] + json_get[i][2]
        t.insert("end", "  " + str(cnt) + ".  " + title+ '\n\n')
        t.insert("end", "         " + size+ '\n\n')
        cnt = cnt + 1
    t.insert("end", "\n\n\n\n\n\n\n\n\n\n\n\n")
    t.insert("end", lists)
def start_M_Team_upload():

    try:
        _thread.start_new_thread(M_Team_upload, ("M_Team_upload", 0))
    except:
        print("Error: 无法启动线程")



















def PT_attendance(threadName, delay):
    global flag
    flag = 'PT_attendance'
    while flag == 'PT_attendance':
        t.delete(1.0, 'end')
        t.insert("end",'                     PT_Attendance' + "       " + time.strftime("%H:%M:%S", time.localtime()) + '\n\n')


        cnt_pt=1
        url = 'https://www.hdarea.co/sign_in.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'UM_distinctid=17df1af452e33f-0380a8d5751151-4c607a68-384000-17df1af452fea5; _ga=GA1.2.1053357565.1640437336; c_secure_uid=MTAyMDMx; c_secure_pass=5a4e1d6ebee979a2f966b1665c7642e4; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; _gid=GA1.2.1253809751.1646633893; CNZZDATA1275308543=290554859-1646347614-%7C1648652280; _gat_gtag_UA_129091596_1=1; Hm_lvt_04584756b6df0223a0a33332be422d74=1648556191,1648608971,1648651657,1648656152; __cf_bm=5x63eLQGaFmUEmRhpwHf5gOJ2qvRIfsP7rqi7kCd2AY-1648656154-0-AcIsvRSK/KgZHYzQzygDNTBiOTJWi7GvgrVYEkPXH/msktH8H9UExnasrhIaYCl/w8z+zdVjwo7GJH04DzX6WYnw5QFyhVjunHuj5Vh5uKtzUuj//GTVkp200GCSo4jDfQ==; Hm_lpvt_04584756b6df0223a0a33332be422d74=1648656181'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://www.hddolby.com/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'cf_clearance=0PXogWo.l7ndl4d3BRix757XbLa4cqUKexAHtUUmJxo-1647133980-0-150; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_uid=MzAwNjM%3D; c_secure_pass=53bff4df712881013affe4765ce8502d; c_secure_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'}
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1



        url = 'https://hdatmos.club/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'cf_clearance=GdNreTMvI._uu0QifajhYBEsKdHTAW7NoM5LQWW_IFU-1644546332-0-150; c_secure_uid=MzcyODg%3D; c_secure_pass=fabe55e7a9244f0cce95b5903f878e23; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'}
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://pt.btschool.club/index.php?action=addbonus'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=OTQ3NjI%3D; c_secure_pass=aee2a65efbdf756f707e6a9309e06d82; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; cf_clearance=tWHEtfEdiblLVgXGdr3JWazDLjVph0FWQRLA.b8stCk-1648656123-0-150'}
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://1ptba.com/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'UM_distinctid=17e27e6f6739b1-0cf8aec71c851d-4c607a68-384000-17e27e6f674c09; c_secure_uid=OTU3NzM%3D; c_secure_pass=8b48d752b988bedba6b1afb80872c377; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; CNZZDATA1278559446=458820218-1641346204-%7C1647161520'}
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://ptchina.org/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=MTA2OTg%3D; c_secure_pass=b3cd25fbcf53c448a792729f15dc4b25; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'}
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://pt.asf.ink/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=NjQ3; c_secure_pass=654d02f0a3d6d690bc87a88a2b5264ee; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'}
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://audiences.me/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=MTU0NjI%3D; c_secure_pass=4c3370a2d83dee22b55d4e242b410aeb; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://pt.hdupt.com/added.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': '_ga=GA1.2.924309875.1648172142; _gid=GA1.2.1989836656.1648815758; c_secure_uid=MzkyNzM%3D; c_secure_pass=9017031fb6be4145530461480bc6e03d; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D; _gat_gtag_UA_76982802_1=1'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://hdfans.org/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=Mjg4NjE%3D; c_secure_pass=17ddbe6ee6b1aa43d718bb83f1c14420; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; __cf_bm=FdN4MDunu2VHQtTNKQdqEKZ_arJIkJLbcMi2ivj_bOI-1648917351-0-AczONuDYjyI85+LuFepPA8XZN1oVna/5hiyZU0edUB5mIGNoA4ivP5jHS2s+io0vsb3c+G6eFrAyb2TOl/NREhT4zKJnRYFSQ4JPvQ250++YaXZhk4LFMQMs4P8S+tggcw=='
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://bitbr.cc/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=NDA5MA%3D%3D; c_secure_pass=d793fc61759c7bad7d3eb0d955f620ac; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://hdcity.city/sign'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_pass=6257f76363a7b4ae065a1ab3aa1d6625; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D; c_secure_uid=MTAxMDQwNjk%3D; c_lang_folder=chs'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'http://hdmayi.com/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'UM_distinctid=17dd23accb13f0-0c04a8e86a2d98-4c607a68-384000-17dd23accb2a4e; c_secure_uid=NzQ3OQ%3D%3D; c_secure_pass=37afa2f0c94ced71d714edde668a5adf; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D; CNZZDATA1278631341=399419274-1639902662-%7C1648909129'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://gainbound.net/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=NTk4; c_secure_pass=dd1e041045c14740a3606213248441e5; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=eWVhaA%3D%3D'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1

        url = 'https://hdtime.org/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=NzM3NTA%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_pass=1a744d16a89d58a7383dc8cc458dcafd; c_secure_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'}
        lists = requests.get(url=url, headers=headers).text
        t.insert("end", "           " + str(cnt_pt) + ".  " + url + '\n\n')
        cnt_pt = cnt_pt + 1

        url = 'https://pterclub.com/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=MTczNTA%3D; c_secure_pass=6357d3893b484b4b12ff737bda6bda12; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; PHPSESSID=aabjt02l7qvduhts1q5m8e7h4f'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end", "           " + str(cnt_pt) + ".  " + url + '\n\n')
        cnt_pt = cnt_pt + 1

        url = 'https://www.nicept.net/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=MTE1MDUz; c_secure_pass=d5d51500269ef91472810be4da4d6584; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end", "           " + str(cnt_pt) + ".  " + url + '\n\n')
        cnt_pt = cnt_pt + 1

        url = 'https://pt.soulvoice.club/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=MTIzMzYz; c_secure_pass=d02fa31f0277bec8c0c9937edbb595da; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end", "           " + str(cnt_pt) + ".  " + url + '\n\n')
        cnt_pt = cnt_pt + 1

        url = 'https://pt.napqaq.top/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D; c_secure_pass=c84b7ff64fac1691f58df143570bbcdd; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_uid=MTAwNzI%3D'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end", "           " + str(cnt_pt) + ".  " + url + '\n\n')
        cnt_pt = cnt_pt + 1

        url = 'https://hdhome.org/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=MTIyMTI5; c_secure_pass=4de78d9e4c01257a4502faf0058c6025; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D; c_secure_uid=MTIyMTI5; c_secure_pass=4de78d9e4c01257a4502faf0058c6025; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D; cf_clearance=2YKzn4vRp_mFEfJ8kTm36YfPoovXeAl_ArTRYEREjzM-1651493056-0-150'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end", "           " + str(cnt_pt) + ".  " + url + '\n\n')
        cnt_pt = cnt_pt + 1

        url = 'https://ourbits.club/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'ourbits_jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPVVJCSVRTIiwiYXVkIjo1MjUwNywiaWF0IjoxNjUxMzgzNjI2LCJqdGkiOiJ5a2hKRE5EakJ4WDg1cWNaa0J3dHYyN2lQcTlNSTFjeVZ5ZUJlWEtlcHBpWWlrWTciLCJleHAiOjE2NTM5NzU2MjYsInNzbCI6dHJ1ZX0.RZMNU95cilOzKQsSH298nr73FL2ntR7y555hp05pHBI'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end", "           " + str(cnt_pt) + ".  " + url + '\n\n')
        cnt_pt = cnt_pt + 1

        url = 'https://lemonhd.org/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=NDQ0MjM%3D; c_secure_pass=857e3414e6bcb029764fdf609adcdf39; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end", "           " + str(cnt_pt) + ".  " + url + '\n\n')
        cnt_pt = cnt_pt + 1





        url = 'https://www.pttime.org/attendance.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'c_secure_uid=Mzc1MTI%3D; c_secure_pass=5470352b431283388f0abd5fceffa609; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
        lists = requests.get(url=url, headers=headers).text
        t.insert("end","           "+str(cnt_pt)+".  "+url+ '\n\n')
        cnt_pt=cnt_pt+1
        time.sleep(delay_time*20)
def start_PT_attendance():

    try:
        _thread.start_new_thread(PT_attendance, ("PT_attendance", 0))
    except:
        print("Error: 无法启动线程")









def gcores(threadName, delay):
    global flag
    flag = 'gcores'
    while flag == 'gcores':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'SINAGLOBAL=6741639331961.842.1636351443105; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5merwV-edKPy4zi1nWB2WF; UOR=,,tophub.today; SUB=_2AkMWxpZdf8NxqwJRmfsUyWzjb49-wgHEieKgmmeGJRMxHRl-yT8XqmAktRB6PUa4sKj9bCE81uS9DWuk-pvHv3CkQsSr; _s_tentry=tophub.today; Apache=9191740774784.104.1637667572390; ULV=1637667572470:9:9:2:9191740774784.104.1637667572390:1637636253119'
        }
        # lhlhlhlhl罗宏亮
        url = 'https://www.gcores.com/articles'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)
        t.delete(1.0, 'end')
        t.insert("end","                         机核文章"+'\n\n')
        cnt = 1
        titles = tree.xpath("""//*[@id="app_inner"]/div[3]/div/div[3]/div/div/div[1]/div/div[1]/div""")
        for i in  titles:
            title = i.xpath('./div/div[2]/a/h3/text()')[0]
            url = "https://www.gcores.com" + i.xpath('./div/div[2]/a/@href')[0]
            timeone = i.xpath('./div/div[2]/div[2]/a/div/div/text()')[0]
            t.insert("end","     "+ str(cnt)+'.  '+  title+"          "+timeone+'\n\n')
            t.insert("end", "                  "+str(url)+'\n\n')
            cnt=cnt+1
        t.insert(1.0, '')
        time.sleep(delay_time)
    # str1 = ''

def start_gcores():

    try:
        _thread.start_new_thread(gcores, ("gcores", 0))
    except:
        print("Error: 无法启动线程")

















def PT_Invite_code(threadName, delay):
    global flag
    flag = 'PT_Invite_code'
    while flag == 'PT_Invite_code':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'SINAGLOBAL=6741639331961.842.1636351443105; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5merwV-edKPy4zi1nWB2WF; UOR=,,tophub.today; SUB=_2AkMWxpZdf8NxqwJRmfsUyWzjb49-wgHEieKgmmeGJRMxHRl-yT8XqmAktRB6PUa4sKj9bCE81uS9DWuk-pvHv3CkQsSr; _s_tentry=tophub.today; Apache=9191740774784.104.1637667572390; ULV=1637667572470:9:9:2:9191740774784.104.1637667572390:1637636253119'
        }
        # lhlhlhlhl罗宏亮
        url = 'http://www.ptyqm.com/category/kfyqzc/'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)
        t.delete(1.0, 'end')
        t.insert("end","                         PT邀请码"+'\n\n')
        print()
        cnt = 1
        # titles = tree.xpath("""//article[contains(@id, "post")]""")
        titles=tree.xpath('/html/body/div[1]/div[2]/section/main/article')
        for i in  titles:
            title = i.xpath('./header/h2/a/text()')[0]
            url = i.xpath('./header/h2/a/@href')[0]
            timeone =""
            try:
                if  i.xpath('./div/span[3]/span[2]/text()'):
                    timeone =  i.xpath('./div/span[3]/span[2]/text()')[0]
                else:
                    timeone = i.xpath('./div/span[2]/span[2]/text()')[0]

            except:
                pass

            t.insert("end","     "+ str(cnt)+'.  '+  title+"          "+timeone+'\n\n')

            t.insert("end", "                  "+str(url)+'\n\n')
            print()
            cnt=cnt+1
        t.insert(1.0, '')
        time.sleep(delay_time)
    # str1 = ''

def start_PT_Invite_code():

    try:
        _thread.start_new_thread(PT_Invite_code, ("PT_Invite_code", 0))
    except:
        print("Error: 无法启动线程")
def baidu_time(threadName, delay):
    global flag
    flag='baidu_time'
    while flag=='baidu_time':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
        }

        url = 'https://top.baidu.com/board?tab=realtime'
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                     LHL's Baidu Top            ") +  time.strftime("%H:%M:%S", time.localtime())+'\n\n'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        titles = tree.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div')
        cnt = 1

        for i in titles:

            title = i.xpath('./div[2]/a/div[1]/text()')

            if (len(title) > 1):
                str1 = str1 + ("  "+str(cnt) + ".  " + "    直播中：" + title[1]) + '\n\n'
            else:
                str1 = str1 + ("  "+str(cnt) + ".  " + title[0]) + '\n\n'
            # print(str(cnt)+".  "+title)
            # print()

            cnt = cnt + 1
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_baidu_time():
    try:
        _thread.start_new_thread(baidu_time, ("baidu_time", 0))
    except:
        print("Error: 无法启动线程")



def zhihutop(threadName, delay):
    # lhlhlhlhl罗宏亮
    global flag
    flag='zhihutop'
    while flag=='zhihutop':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'cookie': '_zap=dad143a7-35e4-46c6-8825-919a78caa1f0; _xsrf=6v5ElWESwWsSsCI20UDgqqhHEhYxGoDn; d_c0="AFBQ5xef_xOPTi60j67vxkMWNkhm2SZf5cg=|1636351980"; captcha_session_v2="2|1:0|10:1636351981|18:captcha_session_v2|88:UzJwRkoxeFNNYngvdFVIUDN1Ykx2YWpkMkV4K1gwWkJaMGtBd245RnJ4Sm9IVGd2a3g5QjEwSXQzaUJ6TWdSdg==|5e740995cbb85969429ac01ba047fee68cf4c43558fa792b4988844ad50bc8ce"; __snaker__id=NjmbuhyUPcomkN0R; gdxidpyhxdE=T22%2BW%2Fh0bcM31kzrBWcICTOoKniKT4HXdI%5CMQw1e6pPK57HE5ZR7S1eeXxzU92E9IXaMkEmLD%2Bj%2FXyJsK8A%5CAm8xiKDqz4rNYSyWD%2BsbLlzASss%2BcKS5IamYtZB1Ak2kg5zXJ%2BmKZtghgVBhHwjiB%2BH4JNokD6nPbWLk4TI168dTwyfI%3A1636352882192; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=UqijRSCLTbkPImSIXu%2BIU40xafBLwh0srev6gFbrf7RVJEn84JFgL%2BlCawKr5syYGyLsjRPocMwVP1EyRHdDy0Ex9pR89y6%2B7AA6CNlmNgCR3GqtQBMiXxg8JJaWLKt1bG4%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee88e17ab69b84adee7ff3b08bb6c15a978e8b85f1808daafba5ce41a3ad8da3ae2af0fea7c3b92a97afa78bd15981949c83ea5c8bb39daadb7fe9979bd5b374a3ba8eadf664f4adbe86f53ea59aae93e53d928a86a6ed34f8968a88cf21b09daf98ca7af7adb7bac67390ada6b3d365a193b9b7d33b87a79ea9e750bbf08b99bc7c92e8f79ab521f59f8fd7c246b0b38288c25af199bf95d44a8fb79899e6348a96afb8cf41b8efaea8b737e2a3; YD00517437729195%3AWM_TID=O44%2FxDTeZYNFVRQQURJr8PFTUo%2FtY4CW; captcha_ticket_v2="2|1:0|10:1636351987|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfWUl1VUYwNGZLekdWeGpaMTdsc0kxN29qQWxFQ2pjUVE2YjdfLkpYbUQ3OTRlQTRuOUJQSktqLVA4TmR6em5NMENlNHRMLjVxSkRWenRMSEU5bmpWbzFPWk1uaDRKWTRnOWxxLTRGN3p4TUM2U0dHWldSU3B6UEdmcHhWa0FlZmFWR0d1ejdmMmZQa3R0MDdiOGJKYTlQaGdHQl9MV2dXU1ZyemQ3cHdzLjJpRUVSLVFJVE9SU0E3Xy5ES0R4TlQySlktQnI2d09SSk1lNm9YLU10MTAtME9YeGpkVVF4cEFKbjA2TklhLTFveTkxejhLS1VuZldqbWtDaDQ2RWtBTmpiMERQelJabFg4ZVBXLU5kN0xLei1wT2xtSko0LmdndlBHU2lKaWpDckxoTlFtamtyR3Y2WmNROGs1em91NVBUQ2IxTzhDLm94bG81c2xmcWJPS2ZDT0ZZeDZCYXFtbGtVNXpHektZd24wOUlnXzFONVZZZFRQTGxkNmpPMVUtRVVPa000Z19QLjZvZ1RhZ1V6dmk5MXY4dHM2SUM5UkJ3cC1BU0MuQ1RWX25mLnlRcVRfYkEwT3BFS1pabG1mWWlQMEMxUlBQVlB5YmFaWDR3VWFMbGs0NktUVjZjSGNGeDhmUDdQNm96NTA2TXR0WURRNWZGSGV1U0JpMyJ9|895d8c8b5d6e65a175fac0f9ed228f0dbd8622422530dda8a231e32b24ad0c42"; z_c0="2|1:0|10:1636351988|4:z_c0|92:Mi4xZDhRY0FnQUFBQUFBVUZEbkY1X19FeVlBQUFCZ0FsVk45QTEyWWdESjdzRElsdXlianl6TUtJcEtrVWxpaTl6RUF3|3c00a7a1b959bbcf72388a3bd105548581af65ff8b6f6263c2a47c2701658619"; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1637591904,1637632938,1637648317,1637668159; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1637668159; KLBRSID=b33d76655747159914ef8c32323d16fd|1637668159|1637668153'

        }
        url = 'https://www.zhihu.com/hot'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)  # lhlhlhlhl罗宏亮
        cnt = 1
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ('                                 知乎Top        ') +time.strftime("%H:%M:%S", time.localtime())+ '\n\n'

        titles = tree.xpath('//*[@id="TopstoryContent"]/div/div/div[1]/section')
        for i in titles:
            title = i.xpath('./div[2]/a/h2/text()')[0]
            url = i.xpath('./div[2]/a/@href')[0]
            # lhlhlhlhl罗宏亮
            # lhlhlhlhl罗宏亮
            str1 = str1 + ("  "+str(cnt) + '.   ' + title) + '\n'
            str1 = str1 + ('            ' + url) + '\n\n'

            cnt = cnt + 1
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_zhihutop():
    try:
        _thread.start_new_thread(zhihutop, ("zhihutop", 0))
    except:
        print("Error: 无法启动线程")

def bilibili(threadName, delay):
    global flag
    flag='bilibili'
    while flag=='bilibili':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'cookie': "buvid3=CF05ED78-D338-2638-5540-9C9F590EC64B72451infoc; b_nut=1699418572; _uuid=4363F10C8-22106-BBDC-10CA3-106E10BDB8F10FA73626infoc; buvid4=5AD05BCA-78C4-5365-3310-2497D6E4642373920-023110812-WEPh3cauru%2FrXrOOyfa4Dq4dtirVUFac; DedeUserID=244138015; DedeUserID__ckMd5=0eb0b23188817111; rpdid=0zbfVGnUMM|15fhaaTfi|1n|3w1R0Azy; hit-dyn-v2=1; enable_web_push=DISABLE; header_theme_version=CLOSE; buvid_fp_plain=undefined; LIVE_BUVID=AUTO4916997098433841; PVID=5; CURRENT_QUALITY=80; fingerprint=bee76d86a3583e3bff1a15d79d56935c; SESSDATA=c37ac5e9%2C1717313303%2C491dd%2Ac1CjABT2soT2b5UJxLgTeETXjBq3pxbYyhRpaNvj1Bf5aE3J361xyx6Z4Zm2fjUJusE6ESVkJMemQtOTZjU2VyQ0hZRHRxTUVJbjI0bk13QlBHYk80eVo2QmFZZm0wRTZlVVY4SGMyWENkV2xpUktKWUFocXVPbFdLaTJGZnFfN01ya014X2hJR0RnIIEC; bili_jct=14d731c2bec00afbf10e4f2b0de5bd10; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDIwODIwMDMsImlhdCI6MTcwMTgyMjc0MywicGx0IjotMX0.3Br6Pn5TR1HrMtsHIoNj7GH5fBl3jJCoLARDd9N3Q3k; bili_ticket_expires=1702081943; buvid_fp=bee76d86a3583e3bff1a15d79d56935c; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; home_feed_column=4; bp_video_offset_244138015=872572363645911065; sid=7rtr60pi; b_lsid=3DA8710E3_18C481FB562; innersign=0; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; browser_resolution=686-942"
        }

        url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                     LHL's bilibili Top 100      ") +time.strftime("%H:%M:%S", time.localtime())+ '\n\n'
        source = requests.get(url=url, headers=headers).json()
        card_list = source['data']['list']
        cnt = 1  # lhlhlhlhl罗宏亮

        for i in card_list:

                str1 = str1 + ("  " + str(cnt) + '. ' + i['title']) + '\n'
                str1 = str1 + ('     UP：' + i['owner']['name']) + '\n'
                str1 = str1 + ('     播放量：' + str(i['stat']['view']//10000)) + ' 万\n'
                str1 = str1 + ('     地址：' + i['short_link_v2']) + '\n\n'
                cnt = cnt + 1

                # title = i.xpath('./div/div[2]/a/text()')[0]
                # bofangliang = i.xpath('./div/div[2]/div/div/span[1]/text()')[0]
                # bofangliang = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", bofangliang)
                # #
                # danmushuliang = i.xpath('./div/div[2]/div/div/span[2]/text()')[0]
                # danmushuliang = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", danmushuliang)
                # Up = i.xpath('./div/div[2]/div/a/span/text()')[0]
                # Up = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", Up)
                # #
                # url = 'https:' + i.xpath('./div/div[1]/a/@href')[0]
                # str1 = str1 + ("  "+str(cnt) + '. ' + title) + '\n'
                # str1 = str1 + ('     UP：' + Up) + '\n'
                # str1 = str1 + ('     播放量：' + bofangliang) + '\n'
                # str1 = str1 + ('     弹幕量：' + danmushuliang) + '\n'
                #
                # str1 = str1 + ('     地址：' + url) + '\n\n'

                cnt = cnt + 1

        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_bilibili( ):
    try:
        _thread.start_new_thread(bilibili, ("bilibili", 0))
    except:
        print("Error: 无法启动线程")

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
        url = 'https://www.huxiu.com/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="app"]/div/div/div/section[2]/section[8]/section/div[2]/div')
        cnthuxiu = 1


        for i in card_list:  # lhlhlhlhl罗宏亮
            str1 = str1 + "  " + str(cnthuxiu) + ".   " + i.xpath('./a/div/img/@alt')[0] + '\n'
            str1 = str1 + "           " + 'https://www.huxiu.com' + i.xpath('./a/@href')[0] + '\n\n'
            cnthuxiu=cnthuxiu+1

            # print(to_url)
            # t.insert(tk.END, to_url, "hyperlink")
            # # 设置超链接的样式
            # t.tag_config("hyperlink", foreground="blue", underline=True)
            # # 绑定点击事件
            # t.tag_bind("hyperlink", "<Button-1>", open_url)


        t.insert(1.0, str1)
        time.sleep(delay_time)



def start_huxiu( ):
    try:
        _thread.start_new_thread(huxiu, ("huxiu", 0))
    except:
        print("Error: 无法启动线程")


def itZHome(threadName, delay):
    global flag
    flag='itZHome'
    while flag=='itZHome':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'cookies':'huxiu_analyzer_wcy_id=3ufl2f5cnp5wdfyvwszx; Hm_lvt_502e601588875750790bbe57346e972b=1700101345; hx_object_visit_referer_1_2393353=+'
        }
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                    IT之家资讯      ") +time.strftime("%H:%M:%S", time.localtime())+ "\n\n"
        url = 'https://it.ithome.com/'
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding  # 使用自动检测的编码
        source = response.text

        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="list"]/div[1]/ul/li')
        cnthuxiu = 1


        for i in card_list:  # lhlhlhlhl罗宏亮
            str1 = str1 + "  " + str(cnthuxiu) + ".   " + i.xpath('./div/h2/a/@title')[0] + '\n\n'
            str1 = str1 + "       " + i.xpath('./div/div[1]/text()')[0] + '\n'
            str1 = str1 + "       " + i.xpath('./a/@href')[0] + '\n\n\n'
            cnthuxiu=cnthuxiu+1
            # print(to_url)
            # t.insert(tk.END, to_url, "hyperlink")
            # # 设置超链接的样式
            # t.tag_config("hyperlink", foreground="blue", underline=True)
            # # 绑定点击事件
            # t.tag_bind("hyperlink", "<Button-1>", open_url)


        t.insert(1.0, str1)
        time.sleep(delay_time)



def start_itZHome( ):
    try:
        _thread.start_new_thread(itZHome, ("itZHome", 0))
    except:
        print("Error: 无法启动线程")
def gamesky(threadName, delay):
    global flag
    flag='gamesky'
    while flag=='gamesky':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'cookies':'huxiu_analyzer_wcy_id=3ufl2f5cnp5wdfyvwszx; Hm_lvt_502e601588875750790bbe57346e972b=1700101345; hx_object_visit_referer_1_2393353=+'
        }
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                   LHL's 游民星空文章      ") +time.strftime("%H:%M:%S", time.localtime())+ "\n\n"
        url = 'https://www.gamersky.com/pcgame/'
        #//*[@id="TopstoryContent"]/div/div/div[1]/section
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding  # 使用自动检测的编码
        source = response.text

        tree = etree.HTML(source)

        # card_list = tree.xpath('/html/body/div[3]/div[2]/div[1]/ul[1]/li')
        card_list = tree.xpath('//*[@class="con"]')

        cnthuxiu = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            try:
                # str1 = str1 + ("  " + str(cnt) + '. ' + i['title']) + '\n'
                # str1 = str1 + ('     UP：' + i['owner']['name']) + '\n'
                # str1 = str1 + ('     播放量：' + str(i['stat']['view'] // 10000)) + ' 万\n'
                # str1 = str1 + ('     地址：' + i['short_link_v2']) + '\n\n'
                str1 = str1 + "  " + str(cnthuxiu) + '. ' + i.xpath('./div[1]/a/@title')[0] + '\n\n'
                str1 = str1 + "  " + "      " + i.xpath('./div[2]/text()')[0] + '\n'
                str1 = str1 + "  " + "          " + i.xpath('./div[1]/a/@href')[0] + '\n\n\n'

                cnthuxiu = cnthuxiu + 1

            except:
                continue
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_gamesky( ):
    try:
        _thread.start_new_thread(gamesky, ("gamesky", 0))
    except:
        print("Error: 无法启动线程")



def game_list(threadName, delay):
    global  flag
    flag='game_list'
    while flag=='game_list':
        cnt = 1
        count = 0
        flag = 1
        cnt11 = 1
        t.delete(1.0, 'end')
        str1 = ''
        t.insert("end", "                     LHL' Game List     " +time.strftime("%H:%M:%S", time.localtime())+  '\n\n')

        url_head = 'https://bbs.3dmgame.com/'
        while True:
            url = 'https://bbs.3dmgame.com/forum-game0day-{}.html'.format(cnt)
            source = requests.get(url=url).text
            tree = etree.HTML(source)
            title = tree.xpath("//a[@style='font-weight: bold;color: #EE1B2E;']")

            for i in title:
                title_m = i.xpath('./text()')[0]
                url_m = "        " + url_head + i.xpath('./@href')[0]
                if (title_m[0] == '【') & (ord(title_m[1]) >= 48) & (ord(title_m[1]) <= 57):
                    t.insert("end", "  "+str(cnt11) + ".    " + title_m + '\n')
                    t.insert("end", url_m + '\n\n')
                    cnt11 = cnt11 + 1
                    count = count + 1
                    if count >= int(10):
                        flag = 0
                        break  # lhlhlhlhl罗宏亮
            cnt = cnt + 1
            if flag == 0:
                break
            t.insert(1.0, str1)
    time.sleep(delay_time)


def start_game_list( ):
    try:
        _thread.start_new_thread(game_list, ("game_list", 0))
    except:
        print("Error: 无法启动线程")



def douban_movies(threadName, delay):
    global flag
    flag='douban_movies'
    while flag=='douban_movies':

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
        }
        cntdouban = 1
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                   LHL's Latest Movie    ") +time.strftime("%H:%M:%S", time.localtime())+ "\n\n"
        url = 'https://movie.douban.com/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        title_list = tree.xpath('//*[@id="screening"]/div[2]/ul/li')
        for i in title_list:
            try:
                title = i.xpath("./@data-title")[0]
                pingfen = i.xpath('./ul/li[3]/span[2]//text()')[0]  # lhlhlhlhl罗宏亮
                place = i.xpath("./@data-region")[0]
                shichang = i.xpath("./@data-duration")[0]
                director = i.xpath("./@data-director")[0]
                actors = i.xpath("./@data-actors")[0]
                url = i.xpath('./ul/li[2]/a/@href')[0]
                t.insert("end", "  "+str(cntdouban) + ". " + title + '\n')
                t.insert("end", '    评分:' + pingfen + '\n')
                t.insert("end", '    导演:' + director + '\n')
                t.insert("end", '    主演:' + actors + '\n')
                t.insert("end", '    国家地区:' + place + '\n')
                t.insert("end", '    时长:' + shichang + '\n')  # lhlhlhlhl罗宏亮
                t.insert("end", '    地址:' + url + '\n' + '\n')
                cntdouban = cntdouban + 1
            except:
                continue
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_douban_movies( ):
    try:
        _thread.start_new_thread(douban_movies, ("douban_movies", 0))
    except:
        print("Error: 无法启动线程")


def steamcracked(threadName, delay):
    global flag
    flag = 'steamcracked'
    while flag == 'steamcracked':


        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
        }
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                   SteamCracked       ") +time.strftime("%H:%M:%S", time.localtime())+ '\n\n'
        url = 'https://steamcrackedgames.com/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div')
        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            try:
                title = i.xpath('./div/div/a/text()')[0]
                url_tail = i.xpath('./div/div/div/small/span[1]/text()')[0]
                t.insert("end","  "+ str(cnt) + '. ' + title + "\n")
                t.insert("end", '     状态:   ' + url_tail + "\n" + "\n")

                cnt = cnt + 1
            except:
                continue
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_steamcracked( ):
    try:
        _thread.start_new_thread(steamcracked, ("steamcracked", 0))
    except:
        print("Error: 无法启动线程")

def skidrowcodex(threadName, delay):
    global flag
    flag = 'skidrowcodex'
    while flag == 'skidrowcodex':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
        }
        t.delete(1.0, 'end')

        t.insert("end", "                   Skidrowcodex      " +time.strftime("%H:%M:%S", time.localtime())+'\n\n')
        url = 'https://www.skidrowcodex.net/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="main_wrapper"]/div[6]/div/div[1]/div')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            try:
                title = i.xpath('./div[1]/div[2]/h2/a/text()')[0]
                url_tail = i.xpath('./div[1]/div[2]/h2/a/@href')[0]
                t.insert("end", "  "+str(cnt) + '. ' + title + '\n')
                t.insert("end", '     地址: ' + url_tail + '\n' + '\n')

                cnt = cnt + 1

            except:
                continue

        time.sleep(delay_time)


def start_skidrowcodex():
    try:
        _thread.start_new_thread(skidrowcodex, ("skidrowcodex", 0))
    except:
        print("Error: 无法启动线程")


def pdoro(threadName, delay):
    global flag
    flag = 'pdoro'
    while flag == 'pdoro':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'cookie': 'bbs_sid=31e211fd2aa2aef7; UM_distinctid=17d18bf7845241-0a04ae99cfc603-561a1053-384000-17d18bf7846e0; bbs_lastday=1638285770; bbs_lastonlineupdate=1638357242; timeoffset=%2B08; CNZZDATA1260924983=591798974-1636794189-%7C1638349746; __tins__17773989=%7B%22sid%22%3A%201638357241795%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201638359041795%7D; __51cke__=; __51laig__=1'
        }
        t.delete(1.0, 'end')
        t.insert("end", "                   pdoro      " +time.strftime("%H:%M:%S", time.localtime())+ "\n" + "\n")
        url = 'http://www.pdoro.com/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="post-item-pobu"]/div[2]/ul/li')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./div/div[2]/h2/a/text()')[0]
            urll = i.xpath('./div/div[2]/h2/a/@href')[0]

            t.insert("end", "  "+str(cnt) + ". " + title + "\n")
            t.insert("end", "     " + urll + "\n" + "\n")
            cnt = cnt + 1
            continue
        time.sleep(delay_time)

def start_pdoro( ):
    try:
        _thread.start_new_thread(pdoro, ("pdoro", 0))
    except:
        print("Error: 无法启动线程")

def pianku(threadName, delay):
    global flag
    flag = 'pianku'
    while flag == 'pianku':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        }
        url = 'https://www.pianku.li/'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)
        t.delete(1.0, 'end')
        t.insert("end", "                 pianku     " +time.strftime("%H:%M:%S", time.localtime())+ '\n')
        t.insert("end", "电影：" + '\n')
        cnt = 1
        dianying = tree.xpath('/html/body/main/div[2]/ul/li')
        for i in dianying:
            title = i.xpath('./div[2]/h3/a/text()')[0]
            pingfen = i.xpath('./div[2]/h3/span/text()')[0]
            xiangxi = i.xpath('./div[2]/div/text()')[0]
            url_tail = 'https://www.pianku.li' + i.xpath('./div[1]/a/@href')[0]
            t.insert("end", '    ' + str(cnt) + '.' + title + '\n')
            t.insert("end", '         ' + pingfen + '分' + '\n')
            t.insert("end", '          ' + xiangxi + '\n')
            t.insert("end", '            ' + url_tail + '\n' + '\n')

            cnt = cnt + 1
        t.insert("end", '剧集:' + '\n')
        cnt = 1
        juji = tree.xpath('/html/body/main/div[3]/ul/li')
        for i in juji:
            title = i.xpath('./div[2]/h3/a/text()')[0]
            pingfen = i.xpath('./div[2]/h3/span/text()')[0]
            xiangxi = i.xpath('./div[2]/div/text()')[0]
            url_tail = 'https://www.pianku.li' + i.xpath('./div[1]/a/@href')[0]
            t.insert("end", '    ' + str(cnt) + '.' + title + '\n')
            t.insert("end", '         ' + pingfen + '分' + '\n')
            t.insert("end", '          ' + xiangxi + '\n')
            t.insert("end", '            ' + url_tail + '\n' + '\n')

            cnt = cnt + 1
        t.insert("end", '动漫:' + '\n')
        cnt = 1
        dongman = tree.xpath('/html/body/main/div[4]/ul/li')
        for i in dongman:
            title = i.xpath('./div[2]/h3/a/text()')[0]
            pingfen = i.xpath('./div[2]/h3/span/text()')[0]
            xiangxi = i.xpath('./div[2]/div/text()')[0]
            url_tail = 'https://www.pianku.li' + i.xpath('./div[1]/a/@href')[0]
            t.insert("end", '    ' + str(cnt) + '.' + title + '\n')
            t.insert("end", '         ' + pingfen + '分' + '\n')
            t.insert("end", '          ' + xiangxi + '\n')
            t.insert("end", '            ' + url_tail + '\n' + '\n')

            cnt = cnt + 1
        time.sleep(delay_time)


def start_pianku( ):
    try:
        _thread.start_new_thread(pianku, ("pianku", 0))
    except:
        print("Error: 无法启动线程")

def Pirate_Bay(threadName, delay):
    global flag
    flag = 'Pirate_Bay'
    while flag == 'Pirate_Bay':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'cookie': 'gaDts48g=q8h5pp9t; gaDts48g=q8h5pp9t; use_alt_cdn=1; aby=2; skt=qrpze70pbv; skt=qrpze70pbv; tcc'
        }
        print("                   bt")
        url = 'https://tpb.party/top/200'
        source = requests.get(url=url, headers=headers).text

        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@class="detName"]')
        t.delete(1.0, 'end')
        t.insert('end', "                        Pirate Bay      " +time.strftime("%H:%M:%S", time.localtime())+ '\n' + '\n')
        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./a/text()')[0]
            urll = i.xpath('./a/@href')[0]

            t.insert('end', "  "+str(cnt) + ". " + title + '\n')
            t.insert('end', "       " + urll + '\n' + '\n')
            cnt = cnt + 1

            continue
        time.sleep(delay_time)
def start_Pirate_Bay( ):
    try:
        _thread.start_new_thread(Pirate_Bay, ("Pirate_Bay", 0))
    except:
        print("Error: 无法启动线程")

def RARGB(threadName, delay):
    global flag
    flag = 'RARGB'
    while flag == 'RARGB':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'cookie': 'gaDts48g=q8h5pp9t; gaDts48g=q8h5pp9t; use_alt_cdn=1; aby=2; skt=autywde7kx; skt=autywde7kx; sk=09ajfqwdc8; expla=1; tcc'


        }
        t.delete(1.0, 'end')
        t.insert('end', "                  RARGB         " +time.strftime("%H:%M:%S", time.localtime())+ '\n' + '\n')
        url = 'https://rarbgprx.org/top100.php?category[]=14&category[]=15&category[]=16&category[]=17&category[]=21&category[]=22&category[]=42&category[]=44&category[]=45&category[]=46&category[]=47&category[]=48'
        source = requests.get(url=url, headers=headers).text

        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@class="lista2"]')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./td[2]/a[1]/text()')[0]
            size = i.xpath('./td[4]/text()')[0]
            urll = i.xpath('./td[2]/a[2]/@href')[0]
            score = i.xpath('./td[2]/span/text()')[0]
            t.insert('end',"  "+ str(cnt) + ". " + title + '\n')
            if (len(score.split('IMDB: ')) > 1):
                t.insert('end', "      " + score.split('IMDB: ')[1][0:3] + "分" + '\n')
            t.insert('end', "       " + size + '\n')
            t.insert('end', "         " + "https://rarbgprx.org" + urll + '\n' + '\n')
            cnt = cnt + 1

            continue
        time.sleep(delay_time)


def start_RARGB( ):
    try:
        _thread.start_new_thread(RARGB, ("RARGB", 0))
    except:
        print("Error: 无法启动线程")


def hd_ai(threadName, delay):
    global flag
    flag = 'hd_ai'
    while flag == 'hd_ai':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'cookie': 'c_secure_uid=4938; c_secure_pass=7cacb523faeba010505abe93d675adde; c_secure_ssl=nope; c_secure_tracker_ssl=nope; c_secure_login=nope; PHPSESSID=964ja96rnvaeg4pkmcpp38vfg1'}
        t.delete(1.0, 'end')
        t.insert('end', "                   hd_ai     " +time.strftime("%H:%M:%S", time.localtime())+'\n' + '\n')
        url = 'https://www.hd.ai/Torrents.tableList'
        source = requests.get(url=url, headers=headers).json()
        card_list = source['data']['items']

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i['small_descr']
            url = i['details']
            if (title == ''):
                continue
            t.insert('end',"  "+ str(cnt) + ".  " + title + '\n')
            t.insert('end', "       " + "https://www.hd.ai" + url + '\n' + '\n')
            cnt = cnt + 1
        time.sleep(delay_time)
def start_hd_ai( ):
    try:
        _thread.start_new_thread(hd_ai, ("hd_ai", 0))
    except:
        print("Error: 无法启动线程")
def youtube(threadName, delay):
    global flag
    flag = 'youtube'
    while flag == 'youtube':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'cookie': 'VISITOR_INFO1_LIVE=A3bSAIfUGDs; LOGIN_INFO=AFmmF2swRQIhAMySgN7wyUcmshqsJciBm75tV8-sreSVlgGclpobfuSKAiBaRBm-Lt6jB11mYzmCqH6MZqvU91xf5vimrOdqpYHqwg:QUQ3MjNmd0tYM2Y3aXFJcXY1dU9pN2hxaWV6NEtvbWpnWEVFa1pROW90THZjMlFLVUxtclRsdUVZak5jUHFod3l0dXd1Z0s2OWJ3Z1RqN25tcERxdjJLbV9wb2RmOUwzZUx1ZG5GSFFJUzVNWXZnMmpLOVRxbjV2clFOWnkzYTlrODJ4RnM0a3FodUU2VG4wZkVBeHU5LTg4SmE4d1I1UGxn; SID=Dghp0vBsy91HgkL6qoFj1j06olowRQaMs4olF7e6MKAs65UVCgMhY1Dw8ldK_YcwS66KYQ.; __Secure-1PSID=Dghp0vBsy91HgkL6qoFj1j06olowRQaMs4olF7e6MKAs65UVdxho_TAKkUaKC-qoGBYp0A.; __Secure-3PSID=Dghp0vBsy91HgkL6qoFj1j06olowRQaMs4olF7e6MKAs65UVXP6uhw1vSSau8ZR4jLZOcA.; HSID=A3Al_FPXLpbFQjoHt; SSID=ASCJ0cz7_MIFZld58; APISID=xlsWGWXCqsZsbDTE/A0sIYHSSNWjTSmvYr; SAPISID=3EupqtVNYod0L-aA/AyUBuaRH-XVS0Ylcv; __Secure-1PAPISID=3EupqtVNYod0L-aA/AyUBuaRH-XVS0Ylcv; __Secure-3PAPISID=3EupqtVNYod0L-aA/AyUBuaRH-XVS0Ylcv; _ga=GA1.2.1268668925.1636788103; _gcl_au=1.1.629964360.1637035019; PREF=f4=4000000&tz=Asia.Shanghai&f6=40000000&f5=30000&volume=100&library_tab_browse_id=FEmusic_liked_playlists; YSC=ks3CXdBqz_A; SIDCC=AJi4QfFCmgttS3x9wwry_HrVa09RIWtzF_zB9e_pcHdJ0XaynUl286un1JCmSD8P9niJ8hF3ynM; __Secure-3PSIDCC=AJi4QfE2mzmbe0dX90RCtTWR0cqUNIZUzjumEi0TnETLalo1QROO6yRrFx5ZxpJq_a_Ul34mCw'
        }

        url = 'https://www.youtube.com/feed/trending'
        t.delete(1.0, 'end')
        t.insert('end', "                     Youtube流行" + '\n' + '\n')
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        # pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)

        youtube_json = re.compile('responseContext".*?"serviceTrackingParams(.*?)function serverContract()', re.S)
        json_get = (str)(re.findall(youtube_json, source)[0])

        # youtube_title1 = re.compile('"title".*?"text":"(.*?)".*?"accessibility"',re.S)
        # youtube_title = re.compile(',"accessibility":.*?"accessibilityData":.*?"label":"(.*?) 来自(.*?) (.*?)天前 (.*?) (.*?)".*?转到频道', re.S)
        youtube_title = re.compile(
            ',"title":{"runs":.{"text":"(.*?)"}.,.*?publishedTimeText":{"simpleText":"(.*?)"},.*?accessibilityData":{"label":"(.*?)"}},.*?viewCountText":{"simpleText":"(.*?)"},"navigationEndpoint.*?webCommandMetadata.*?url":"(.*?)".*?ownerText.*?text":"(.*?)","navigationEndpoint.*?操作菜单',
            re.S)
        cnt = 1
        names = re.findall(youtube_title, json_get)
        for i in names:
            title = i[0]
            Later_time = i[1]
            time_long = i[2]
            Watch_num = i[3]
            url = 'https://www.youtube.com' + i[4]
            youtuber = i[5]

            t.insert('end',"  "+ str(cnt) + ". " + title + '\n')
            t.insert('end', "       Youtuber： " + youtuber + '\n')
            t.insert('end', "       发布时间:   " + Later_time + '\n')
            t.insert('end', "       时长:      " + time_long + '\n')
            t.insert('end', "       观看数量:   " + Watch_num + '\n')
            t.insert('end', "       地址:      " + url + '\n' + '\n')

            cnt = cnt + 1
        time.sleep(delay_time)
def start_youtube ( ):
    try:
        _thread.start_new_thread(youtube, ("youtube", 0))
    except:
        print("Error: 无法启动线程")


def BT_HOME(threadName, delay):
    global flag
    flag = 'BT_HOME'
    while flag == 'BT_HOME':

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'SINAGLOBAL=6741639331961.842.1636351443105; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5merwV-edKPy4zi1nWB2WF; UOR=,,tophub.today; SUB=_2AkMWxpZdf8NxqwJRmfsUyWzjb49-wgHEieKgmmeGJRMxHRl-yT8XqmAktRB6PUa4sKj9bCE81uS9DWuk-pvHv3CkQsSr; _s_tentry=tophub.today; Apache=9191740774784.104.1637667572390; ULV=1637667572470:9:9:2:9191740774784.104.1637667572390:1637636253119'
        }
        # lhlhlhlhl罗宏亮
        url = 'https://btbtt20.com/'
        t.delete(1.0, 'end')
        t.insert('end', "                     BT_HOME       " +time.strftime("%H:%M:%S", time.localtime())+ '\n' + '\n')
        lists = requests.get(url=url, headers=headers).text
        lists_json = re.compile(
            '</a>\t.*?\n.*?<a href="(.*?)" class="subject_link thread-new"  target="_blank" title="(.*?)" >.*?<span class',
            re.S)
        json_get = re.findall(lists_json, lists)
        cnt = 1
        for i in range(1, len(json_get)):
            title = json_get[i][1].split("<")[0]
            url = "https://btbtt20.com/" + json_get[i][0].split("<")[0]
            t.insert('end',"  "+ str(cnt) + ".  " + title + '\n')
            t.insert('end', "            " + url + '\n' + '\n')
            cnt = cnt + 1
        time.sleep(delay_time)

def start_BT_HOME ( ):
    try:
        _thread.start_new_thread(BT_HOME, ("BT_HOME", 0))
    except:
        print("Error: 无法启动线程")


def Epic_freeGames(threadName, delay):
    global flag
    flag = 'Epic_freeGames'
    while flag == 'Epic_freeGames':

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
        }

        url = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=US&allowCountries=US'


        t.delete(1.0, 'end')
        t.insert('end', "                     Epic_freeGames    " +time.strftime("%H:%M:%S", time.localtime())+ '\n\n')
        source = requests.get(url=url, headers=headers).json()

        # titles = tree.xpath('https://www.epicgames.com/store/zh-CN/free-games')
        cnt = 1
        list=source['data']['Catalog']['searchStore']['elements']
        shuzhu_Epic=[]
        Epic_lenn=len(list)-1
        for i in list:
            shuzhu_Epic.append(i['title'])
        while(Epic_lenn>=0):
            t.insert('end', str(Epic_lenn+1)+".  "+shuzhu_Epic[Epic_lenn]+'\n'+'\n')
            Epic_lenn=Epic_lenn-1
        time.sleep(delay_time)

def start_Epic_freeGames ( ):
    try:
        _thread.start_new_thread(Epic_freeGames, ("Epic_freeGames", 0))
    except:
        print("Error: 无法启动线程")

def steam_HOT(threadName, delay):
    global flag
    flag = 'douban_movies'
    while flag == 'douban_movies':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        }


        url = 'https://store.steampowered.com/search/?filter=topsellers'
        source = requests.get(url=url, headers=headers).text
        t.delete(1.0, 'end')
        t.insert('end', "                    Steam Hot    " +time.strftime("%H:%M:%S", time.localtime())+ '\n\n')
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="search_resultsRows"]/a')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./div[2]/div[1]/span/text()')[0]
            hao_pings=i.xpath('./div[2]/div[3]/span/@data-tooltip-html')
            if (len(hao_pings) > 0):
                hao_ping = str(hao_pings[0])
                hao_ping = hao_ping.split('<br>')[1]

                hao_ping_num_peo = hao_ping.split('用户的游戏评测中有')
                if (len(hao_ping_num_peo) >= 2):
                    hao_ping_people = hao_ping_num_peo[0]
                    hao_ping_num = hao_ping_num_peo[1].replace("。", '')
                else:
                    hao_ping_people = ''
                    hao_ping_num = 0
            else:
                hao_ping_people = ''
                hao_ping_num = 0
            zhekoou=i.xpath('./div[2]/div[4]/div[1]/span/text()')

            release_time=i.xpath('./div[2]/div[2]/text()')


            url_game=i.xpath('./@href')[0]
            values_game_origion = i.xpath('./div[2]/div[4]/div[2]/text()')
            values_game_origion_origion=i.xpath('./div[2]/div[4]/div[2]/span/strike/text()')

            if(len(values_game_origion)>=2):
                values_game_zhe=i.xpath('./div[2]/div[4]/div[2]/text()')[1]
            else:
                values_game_zhe = str(i.xpath('./div[2]/div[4]/div[2]/text()')[0])
                values_game_zhe=values_game_zhe.replace("\r\n                        ",'')
            t.insert('end',"  "+ str(cnt)+".    "+  title+'\n')
            if len(hao_ping_people) > 0:
                t.insert('end', "            评价: "+ hao_ping_num+"    "+hao_ping_people+'\n')
            if(len(zhekoou)>0):
                t.insert('end', "            折扣:  "+zhekoou[0]+'\n')
                t.insert('end', "            原价:  "+values_game_origion_origion[0]+'\n')
            else:
                t.insert('end', "            折扣:  无"  +'\n')
            t.insert('end', "            价格:  "+values_game_zhe+'\n')
            if (len(release_time) >= 1):
                t.insert('end', "            时间:  " + release_time[0]+'\n')
            else:
                t.insert('end', "            时间:  无信息"  +'\n')
            t.insert('end', "            地址:  "+str(url_game).split('/?')[0]+'\n'+'\n')

            cnt = cnt + 1
        time.sleep(delay_time)

def start_steam_HOT ( ):
    try:
        _thread.start_new_thread(steam_HOT, ("steam_HOT", 0))
    except:
        print("Error: 无法启动线程")

def steam_new(threadName, delay):
    global flag
    flag = 'steam_new'
    while flag == 'steam_new':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        }


        url = 'https://store.steampowered.com/search/?filter=popularnew&sort_by=Released_DESC'
        source = requests.get(url=url, headers=headers).text
        t.delete(1.0, 'end')
        t.insert('end', "                    Steam Hot    " +time.strftime("%H:%M:%S", time.localtime())+ '\n\n')
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="search_resultsRows"]/a')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./div[2]/div[1]/span/text()')[0]
            hao_pings=i.xpath('./div[2]/div[3]/span/@data-tooltip-html')
            if(len(hao_pings)>0):
                hao_ping=str(hao_pings[0])
                hao_ping=hao_ping.split('<br>')[1]

                hao_ping_num_peo=hao_ping.split('用户的游戏评测中有')
                if(len(hao_ping_num_peo)>=2):
                    hao_ping_people = hao_ping_num_peo[0]
                    hao_ping_num= hao_ping_num_peo[1].replace("。",'')
            zhekoou=i.xpath('./div[2]/div[4]/div[1]/span/text()')

            release_time=i.xpath('./div[2]/div[2]/text()')


            url_game=i.xpath('./@href')[0]
            values_game_origion = i.xpath('./div[2]/div[4]/div[2]/text()')
            values_game_origion_origion=i.xpath('./div[2]/div[4]/div[2]/span/strike/text()')

            if(len(values_game_origion)>=2):
                values_game_zhe=i.xpath('./div[2]/div[4]/div[2]/text()')[1]
            else:
                values_game_zhe = str(i.xpath('./div[2]/div[4]/div[2]/text()')[0])
                values_game_zhe=values_game_zhe.replace("\r\n                        ",'')
            t.insert('end',"  "+ str(cnt)+".    "+  title+'\n')
            t.insert('end', "            评价: "+ hao_ping_num+"    "+hao_ping_people+'\n')
            if(len(zhekoou)>0):
                t.insert('end', "            折扣:  "+zhekoou[0]+'\n')
                t.insert('end', "            原价:  "+values_game_origion_origion[0]+'\n')
            else:
                t.insert('end', "            折扣:  无"  +'\n')
            t.insert('end', "            价格:  "+values_game_zhe+'\n')
            if (len(release_time) >= 1):
                t.insert('end', "            时间:  " + release_time[0]+'\n')
            else:
                t.insert('end', "            时间:  无信息"  +'\n')
            t.insert('end', "            地址:  "+str(url_game).split('/?')[0]+'\n'+'\n')

            cnt = cnt + 1
        time.sleep(delay_time)

def start_steam_new ( ):
    try:
        _thread.start_new_thread(steam_new, ("steam_new", 0))
    except:
        print("Error: 无法启动线程")


def PT_Time(threadName, delay):
    global flag
    flag = 'PT_Time'
    while flag == 'PT_Time':

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'cookie': 'c_secure_uid=MzIwNDY%3D; c_secure_pass=ad5dc1d4c2b7ff2c09e9b3097f6a4ab8; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
        t.delete(1.0, 'end')
        t.insert('end', "                    PT_Time    " + time.strftime("%H:%M:%S", time.localtime()) + '\n\n')
        url = 'https://www.pttime.org/torrents.php'

        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)

        cnt=1
        youtube_json = re.compile('<tr>.*?<td class="rowfollow nowrap" valign="middle">.*?<b class="title">(.*?)<.*?</span></td><td class="rowfollow">(.*?)<br />(.*?)</td>.*?</tr>', re.S)
        json_get = (re.findall(youtube_json, source))
        print(json_get)
        # youtube_title1 = re.compile('"title".*?"text":"(.*?)".*?"accessibility"',re.S)
        # youtube_title = re.compile(',"accessibility":.*?"accessibilityData":.*?"label":"(.*?) 来自(.*?) (.*?)天前 (.*?) (.*?)".*?转到频道', re.S)
        # youtube_title = re.compile(
        #     ',"title":{"runs":.{"text":"(.*?)"}.,.*?publishedTimeText":{"simpleText":"(.*?)"},.*?accessibilityData":{"label":"(.*?)"}},.*?viewCountText":{"simpleText":"(.*?)"},"navigationEndpoint.*?webCommandMetadata.*?url":"(.*?)".*?ownerText.*?text":"(.*?)","navigationEndpoint.*?操作菜单',
        #     re.S)
        # cnt = 1
        # names = re.findall(youtube_title, json_get)
        for i in json_get:
            title = i[0]
            size=i[1]+i[2]
            t.insert('end', "  "+str(cnt)+".     "+title+'\n')
            t.insert('end', "              "+size+'\n'+'\n')


            cnt = cnt + 1
        time.sleep(delay_time)
def start_PT_Time ( ):
    try:
        _thread.start_new_thread(PT_Time, ("PT_Time", 0))
    except:
        print("Error: 无法启动线程")


def hao4k_4k_uhd(threadName, delay):
    global flag
    flag = 'hao4k_4k_uhd'
    while flag == 'hao4k_4k_uhd':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'SINAGLOBAL=6741639331961.842.1636351443105; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5merwV-edKPy4zi1nWB2WF; UOR=,,tophub.today; SUB=_2AkMWxpZdf8NxqwJRmfsUyWzjb49-wgHEieKgmmeGJRMxHRl-yT8XqmAktRB6PUa4sKj9bCE81uS9DWuk-pvHv3CkQsSr; _s_tentry=tophub.today; Apache=9191740774784.104.1637667572390; ULV=1637667572470:9:9:2:9191740774784.104.1637667572390:1637636253119'
        }
        # lhlhlhlhl罗宏亮
        url = 'https://www.hao4k.cn/zt/4kuhd.html'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)
        cnt = 1
        titles = tree.xpath('//*[@id="portal_block_7324_content"]/div/dl')
        str1 = ''
        t.delete(1.0, 'end')
        t.insert("end",'                     Hao4k_UHD' + "       " + time.strftime("%H:%M:%S", time.localtime()) + '\n\n')
        cnt=1
        # lhlhlhlhl罗宏亮
        for i in titles:
            title = i.xpath('./font/b/a/text()')[0]
            url = i.xpath('./font/b/a/@href')[0]
            t.insert("end",  "  "+str(cnt)+". "+title + '\n')
            t.insert("end", "         "+url + '\n\n')
            cnt=cnt+1
        t.insert(1.0, str1)
        time.sleep(delay_time)
def start_hao4k_4k_uhd ( ):
    try:
        _thread.start_new_thread(hao4k_4k_uhd, ("hao4k_4k_uhd", 0))
    except:
        print("Error: 无法启动线程")

scroll = tk.Scrollbar(width=20)
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar, tearoff=1)
#
#
# menubar.add_cascade(label="Information", menu=filemenu)
# filemenu.add_command(label="微博热榜", command=start_weibo)
# filemenu.add_command(label="百度热榜", command=start_baidu_time)
# filemenu.add_command(label="知乎热榜", command=start_zhihu2)
# filemenu.add_command(label="哔哩哔哩", command=start_bilibili)
# filemenu.add_command(label="虎嗅热文", command=start_huxiu)
# filemenu.add_command(label="豆瓣热门电影", command=start_douban_movies)
# filemenu.add_command(label="游戏下载", command=start_game_list)
# filemenu.add_command(label="游民星空资讯", command=start_gamesky)
# filemenu.add_command(label="IT之家资讯", command=start_itZHome)
# #filemenu.add_command(label="Zhihu", command=start_zhihutop)
# filemenu.add_command(label="M_Team_upload", command=start_M_Team_upload)
# filemenu.add_command(label="M_Team_offers", command=start_M_Team_offers)
# filemenu.add_command(label="M_Team_torrents", command=start_M_Team_torrents)
# filemenu.add_command(label="Youtube", command=start_youtube)
# filemenu.add_command(label="Steamcracked", command=start_steamcracked)
# filemenu.add_command(label="Skidrowcodex", command=start_skidrowcodex)
# filemenu.add_command(label="pdoro", command=start_pdoro)
# filemenu.add_command(label="Pianku", command=start_pianku)
# filemenu.add_command(label="Pirate Bay", command=start_Pirate_Bay)
# filemenu.add_command(label="RARGB", command=start_RARGB)
# filemenu.add_command(label="HD_ai", command=start_hd_ai)
# filemenu.add_command(label="BT_HOME", command=start_BT_HOME)
# filemenu.add_command(label="Epic_freeGames", command=start_Epic_freeGames)
# filemenu.add_command(label="Steam_HOT", command=start_steam_HOT)
# filemenu.add_command(label="Steam_NEW", command=start_steam_new)
# filemenu.add_command(label="PT_Time", command=start_PT_Time)
# filemenu.add_command(label="hao4k_4k_uhd", command=start_hao4k_4k_uhd)
# filemenu.add_command(label="PT_Invite_code", command=start_PT_Invite_code)
# filemenu.add_command(label="机核", command=start_gcores)
# filemenu.add_command(label="PT_attendance", command=start_PT_attendance)
#
#
# filemenu.add_command(label="Delete", command=delete_text)
#

#
# window.config(menu=filemenu)


new_window_add_button()




# pyinstaller --onefile --icon=favicon.ico  test.py -w
# b1=tk.Button(window,text="Baidu",command=baidu_time)
# b2=tk.Button(window,text="Weibo",command=weibo)
# b3=tk.Button(window,text="Zhihu",command=zhihutop)
# b4=tk.Button(window,text="Bilibili",command=bilibili)
# b5=tk.Button(window,text="huxiu",command=huxiu)
# b6=tk.Button(window,text="GameList",command=game_list)
# b7=tk.Button(window,text="Douban",command=douban_movies)
# b8=tk.Button(window,text="Steamcracked",command=steamcracked)
# b9=tk.Button(window,text="Skidrowcodex",command=skidrowcodex)
# b10=tk.Button(window,text="pdoro",command=pdoro)
# b11=tk.Button(window,text="Pianku",command=pianku)
# b3=tk.Button(window,text="Delete",command=delete_text)


t = tk.Text(window, width=3840, height=2160, font=('Consolas', 15, "bold"))

scroll.pack(side=tk.RIGHT, fill=tk.Y)
scroll.config(command=t.yview)

t.pack(side='top', fill="both")
# 绑定最小化事件
window.bind("<Unmap>", on_minimize)

# 绑定复原事件
window.bind("<Map>", on_restore)
# 绑定鼠标点击事件，点击窗口时将其移到最前面
window.bind("<Button-1>", bring_to_front)
window.bind("<FocusIn>", bring_to_front)
window.bind("<Configure>", update_position)
window.lift()

# window.config(menu=menubar)
window.mainloop()

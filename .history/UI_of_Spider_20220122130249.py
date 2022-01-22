# a new GUI
from calendar import c
import sys
import os
import linecache
from PySide2.QtCore import QUrl, QThread
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QTextCursor, QGuiApplication, QDesktopServices
from sphinx import path
import spider_UI_layout
import re
import json
import time
import traceback
import requests
import logging
import random
from lxml import etree
import urllib.parse as parse
from urllib.request import urlretrieve
from multiprocessing import Pool
import numpy as np


# hyper parameters
novel_save_path = './Novels'  # default novel saved path
WAIT_TIME = 5
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='spider_without_UI.log',
                    filemode='a',
                    level=logging.INFO)
user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
HOSTS = ['https://www.mayiwxw.com/', 'https://www.changyeyuhuo.com']
header = {"User-Agent": random.choice(user_agent)}


def rank_info_qidian_url(ui_test=False, dialog=None):
    # get the rank information
    request_content = requests.get(
        url='https://www.qidian.com/rank', headers=header, timeout=5)
    request_content.encoding = 'utf-8'

    data = etree.HTML(request_content.text)
    rank_list = data.xpath('//ul[@class="list_type_detective"]//@href')
    name_list = data.xpath('//ul[@class="list_type_detective"]//a/text()')
    for link_temp in rank_list:
        link_final = 'http:' + link_temp
        rank_list[rank_list.index(link_temp)] = link_final

    if not ui_test:
        print('Data loaded successfully ! ')
        print(name_list)

    else:
        dialog.rank_label.setText(dialog.tr('Data loaded successfully ! '))
        dialog.rank_book_name_list.clear()
        dialog.rank_author_list.clear()
        dialog.rank_genre_list.clear()
        dialog.rank_status_list.clear()
        dialog.rank_intro_list.clear()
        dialog.rank_newest_chapter_list.clear()

        dialog.rank_book_name_list.addItems(name_list)
        dialog.rank_label.setText(dialog.tr('waiting selection ! '))
    return name_list, rank_list


def qidian_content_rank(rank_list, ui_test=False, dialog=None):

    if not ui_test:
        num = input('input the index: ')
        num = int(num)
        response_temp = requests.get(
            url=rank_list[num], headers=header, timeout=5)
    else:
        response_temp = requests.get(
            url=dialog.rank_url, headers=header, timeout=5)

    response_temp.encoding = 'utf-8'
    data = etree.HTML(response_temp.text)
    info_book_name_list = data.xpath(
        '//div[@class="book-img-text"]//div[@class="book-mid-info"]/h2//text()')
    info_book_url_list = data.xpath(
        '//div[@class="book-img-text"]//div[@class="book-mid-info"]/h2//@href')
    info_book_content_list = data.xpath('//p[@class="intro"]//text()')
    info_author = data.xpath('//p[@class="author"]//a[@class="name"]//text()')
    info_status = data.xpath('//p[@class="author"]//span//text()')
    info_genre = data.xpath('//p[@class="author"]//a//text()')
    info_update_chapter_name = data.xpath('//p[@class="update"]/a/text()')
    info_update_url = data.xpath('//p[@class="update"]/a/@href')
    info_author_url = data.xpath(
        '//p[@class="author"]//a[@class="name"]/@href')
    info_genre_urls = data.xpath('//p[@class="author"]/a/@href')

    # info showing from spider
    print(f'info_book_name_list: {info_book_name_list[0]}')
    print(f'info_book_url_list: {info_book_url_list[0]}')
    print(f'info_book_content_list: {info_book_content_list[0]}')
    print(f'info_author: {info_author[0]}')
    print(f'info_status: {info_status[0]}')
    print(f'info_update_chapter_name: {info_update_chapter_name[0]}')
    print(f'info_update_url: {info_update_url[0]}')
    print(f'info_author_url: {info_author_url[0]}')
    print(f'info_genre_urls: {info_genre_urls[0]}')

    # clean data
    info_genre_url_list, info_genre_list = [], []
    for i in range(len(info_genre_urls)):
        if i % 3 == 1:
            info_genre_url_list.append(info_genre_urls[i])
            info_genre_list.append(info_genre[i])

    for i in range(len(info_author)):
        info_update_url[i] = 'https:' + info_update_url[i]
        info_genre_url_list[i] = 'https:' + info_genre_url_list[i]
        info_book_url_list[i] = 'https:' + info_book_url_list[i]
        info_author_url[i] = 'https:' + info_author_url[i]

    dic_info = {
        'book_name': info_book_name_list,
        'url': info_book_url_list,
        'intro': info_book_content_list,
        'author': info_author,
        'genre': info_genre_list,
        'status': info_status,
        'update_chapter': info_update_chapter_name,
        'update_url': info_update_url,
        'author_url': info_author_url,
        'genre_url': info_genre_url_list
    }

    if not ui_test:
        # print(info_author_url)
        print(dic_info)
        pass
    else:
        dialog.rank_book_name_list.clear()
        dialog.rank_book_name_list.addItems(info_book_name_list)
        dialog.rank_author_list.clear()
        dialog.rank_author_list.addItems(info_author)
        dialog.rank_genre_list.clear()
        dialog.rank_genre_list.addItems(info_genre_list)
        dialog.rank_status_list.clear()
        dialog.rank_status_list.addItems(info_status)
        dialog.rank_intro_list.clear()
        dialog.rank_intro_list.addItems(info_book_content_list)
        dialog.rank_newest_chapter_list.clear()
        dialog.rank_newest_chapter_list.addItems(info_update_chapter_name)
    return dic_info


def qq_music_search(ui_test=False, dialog=None, key_word=None):
    # setting log config
    logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='spider_main.log',
                        filemode='a',
                        level=logging.INFO)

    # encoding input content into url form
    if not ui_test:
        w_coding = parse.urlencode({'w': input('输入歌名:')})
    else:
        w_coding = parse.urlencode({'w': str(key_word)})
        dialog.status_music_label.setText(
            dialog.tr('finding content list ...'))
        dialog.music_listWidget.clear()

    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace' \
          '=txt.yqq.song&searchid=63229658163010696&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&{}' \
          '&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=' \
          'utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(w_coding)

    content = requests.get(url=url, headers=header)
    str_1 = content.text
    dict_1 = json.loads(str_1)
    song_list = dict_1['data']['song']['list']

    str_3 = '''https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey5559460738919986&g_tk=5381&loginUin=0&hostUin=0
    &format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0
    &data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch",
    "param":{"guid":"1825194589","calltype":0,"userip":""}},
    "req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey",
    "param":{"guid":"1825194589","songmid":["%s"],"songtype":[0],"uin":"0",
    "loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'''

    url_list = []
    music_name = []

    for i in range(len(song_list)):
        music_name.append(song_list[i]['name'] +
                          '-' + song_list[i]['singer'][0]['name'])
        url_list.append(str_3 % (song_list[i]['mid']))

        if not ui_test:
            print('{}.{}-{}'.format(i + 1,
                  song_list[i]['name'], song_list[i]['singer'][0]['name']))
        else:
            dialog.music_listWidget.addItem(
                '{}-{}'.format(song_list[i]['name'], song_list[i]['singer'][0]['name']))

    return url_list, music_name


def qq_music_download(music_name, url_list, ui_test=False, dialog=None):
    if not ui_test:
        song_index = int(input('请输入你想下载的音乐序号:'))
        song_index -= 1
    else:
        song_index = dialog.music_listWidget.currentRow()
    content_json = requests.get(url=url_list[song_index])
    dict_2 = json.loads(content_json.text)
    url_ip = dict_2['req']['data']['freeflowsip'][1]
    purl = dict_2['req_0']['data']['midurlinfo'][0]['purl']

    download_url = url_ip + purl

    save_dic_path = './QQMusic'
    if not os.path.exists(save_dic_path):
        os.mkdir(save_dic_path)

    if not ui_test:
        try:
            print('开始下载...')
            urlretrieve(
                url=download_url, filename='./QQMusic/{}.mp3'.format(music_name[song_index]))
            print('{}.mp3下载完成！'.format(music_name[song_index]))
        except Exception as e:
            print(e, '对不起，你没有该歌曲的版权！')
            logging.warning(traceback.format_exc())

    else:
        try:
            dialog.status_music_label.setText(dialog.tr('start downloading !'))
            urlretrieve(
                url=download_url, filename='./QQMusic/{}.mp3'.format(music_name[song_index]))
            dialog.status_music_label.setText(
                dialog.tr('{}.mp3 download successfully！'.format(music_name[song_index])))
        except Exception as e:
            dialog.status_music_label.setText(
                dialog.tr('cannot download for the permission'))
            print(e, '对不起，你没有该歌曲的版权！')
            logging.warning(traceback.format_exc())


class novel_spider:

    def __init__(self, bookname, source, dialog):
        self.novel_save_path = 'Novels'
        self.book_name_search = bookname
        self.source = source
        self.dialog = dialog
        self.user_agent = user_agent
        self.header = {"User-Agent": random.choice(self.user_agent)}
        self.HOSTS = ['https://www.mayiwxw.com/', 'https://www.changyeyuhuo.com']
        self.no_result = False

        # init None parameters
        self.host, self.book_search_url = None, None
        self.data_form, self.result_url_search_analyze = None, None
        self.search_url, self.result_url_search, self.result_title_search = None, None, None
        self.chapter_links, self.bookname = None, None
        self.result_title_search_analyze = None
        self.bookname_analyze, self.chapter_links_analyze = None, None
        self.single_novel_folder, self.menu_save_path = None, None
        self.exit_content, self.next_chapter_links = [], []
        self.chapter_title_analyze, self.chapter_content_analyze = None, None
        self.page_analyze = None
        self.next_chapter_analyze = None
        self.downloaded_links = []

        # initial parameters
        self.init_parameter()

    def init_parameter(self):
        if self.source == 'biquge':
            self.host = self.HOSTS[0]
            self.search_url = 'https://www.mayiwxw.com/modules/article/search.php'
            self.data_form = {'searchkey': self.book_name_search, 'searchtype': 'articlename'}
            self.result_url_search_analyze = '//*[@class="odd"]//a/@href'
            self.result_title_search_analyze = '//*[@class="odd"]//a/text()'
            self.bookname_analyze = '//*[@id="info"]/h1/text()'
            self.chapter_links_analyze = '//*//dd//a/@href'
            self.chapter_title_analyze = '//*[@class="bookname"]/h1/text()'
            self.chapter_content_analyze = '//div[@id="content"]/text()'

        elif self.source == 'changyeyuhuo':
            self.host = self.HOSTS[1]
            self.search_url = 'https://www.changyeyuhuo.com/search/'
            self.data_form = {'searchkey': self.book_name_search}
            self.result_url_search_analyze = '//ul[@class="txt-list txt-list-row5"]//span[@class="s2"]//a/@href'
            self.result_title_search_analyze = '//ul[@class="txt-list txt-list-row5"]//span[@class="s2"]//a/text()'
            self.bookname_analyze = "//div[@class='top']//h1/text()"
            self.page_analyze = "//div[@class='listpage']//option//@value"
            self.chapter_links_analyze = "//div[@class='section-box']//li//a/@href"
            self.chapter_title_analyze = '//*[@class="reader-main"]/h1/text()'
            self.chapter_content_analyze = '//div[@id="content"]/p/text()'
            self.next_chapter_analyze = '//*[@id="next_url"]//@href'

        elif self.source == 'luoxia':
            self.host = 'luoxia'
            self.search_url = 'https://www.luoxiabook.com/e/search/index.php'
            self.data_form = {'keyboard': self.book_name_search,
                              'tbname': 'bookname',
                              'show': 'title,writer',
                              'tempid': '1'}
            self.result_url_search_analyze = '//td[@class="col-md-2 col-sm-8 col-xs-8"]//a/@href'
            self.result_title_search_analyze = '//td[@class="col-md-2 col-sm-8 col-xs-8"]//a/text()'
            self.bookname_analyze = '//div[@class="panel-heading"]/h1/text()'
            self.chapter_links_analyze = ['//li[@class="list-group-item col-md-4 vv-book"]//a/@href',
                                          '//li[@class="list-group-item col-md-12 vv-book"]//a/@href']
            self.chapter_title_analyze = '//div[@class="panel-footer col-md-12"]/h1/text()'
            self.chapter_content_analyze = '//div[@id="content"]//text()'

    def spider_running(self):
        self.novel_chapters_loading()
        self.novel_download()

    def search_novel(self):
        try:
            res_search = requests.post(url=self.search_url, data=self.data_form, headers=self.header, timeout=5)
            res_search.encoding = 'utf-8'
            temp1 = etree.HTML(res_search.text)
            print(res_search.text)
            self.result_url_search = temp1.xpath(self.result_url_search_analyze)
            self.result_title_search = temp1.xpath(self.result_title_search_analyze)

            # improve the book_search_url form
            if self.source == 'biquge':
                for result in self.result_url_search:
                    temp = self.host + result
                    self.result_url_search[self.result_url_search.index(result)] = temp
            elif self.source == 'changyeyuhuo':
                for result in self.result_url_search:
                    temp = self.host + result
                    self.result_url_search[self.result_url_search.index(result)] = temp

            if not self.result_url_search:
                self.no_result = True
                print('no result')
                return self.no_result

        except Exception as e:
            print('\n')
            print(e)
            logging.warning(traceback.format_exc())

    # get name and chapter_links
    def novel_chapters_loading(self):
        print('novel_chapters_loading is executed .')
        try:
            response = requests.get(
                self.book_search_url, headers=self.header, timeout=WAIT_TIME)
            response.encoding = 'utf-8'
            data_response = etree.HTML(response.text)
            self.bookname = data_response.xpath(self.bookname_analyze)[0]

            # luoxia - list  biquge - [9:]
            if isinstance(self.chapter_links_analyze, list):
                self.chapter_links = data_response.xpath(self.chapter_links_analyze[0])
                chapter_links_back = data_response.xpath(self.chapter_links_analyze[1])
                self.chapter_links = chapter_links_back + self.chapter_links
            elif self.source == 'biquge':
                self.chapter_links = data_response.xpath(
                    self.chapter_links_analyze)
                chapter_links = []
                for link in self.chapter_links[9:]:
                    chapter_links.append(self.host + link)
                self.chapter_links = chapter_links
            elif self.source == 'changyeyuhuo':
                whole_book_page = data_response.xpath(self.page_analyze)
                chapter_links = []
                for index_page in whole_book_page:
                    response = requests.get(
                        url=index_page, headers=self.header, timeout=5)
                    response.encoding = 'utf-8'
                    data_response = etree.HTML(response.text)
                    for link in data_response.xpath(self.chapter_links_analyze)[12:]:
                        chapter_links.append(self.host + link)
                self.chapter_links = chapter_links

            # clean the space string
            self.bookname = self.bookname.split(' ')[0]

            # prepare for a initial json file
            self.json_data = {
                'book_name': f'{self.bookname}',
                'author': '',
                'status': 'downloading',
                'chapter_names': [],
                'chapter_links': self.chapter_links,
                'downloaded_links': [],
                'source': self.source
            }

        except Exception as e:
            print('\n')
            print('Error Message in download spider')
            print(e)
            logging.warning(traceback.format_exc())
            print('save the error message into log file.')

    def novel_download(self):
        print('novel_download is executed.')
        # setting the sub path
        self.single_novel_folder = os.path.join(novel_save_path, self.bookname)
        if not os.path.exists(self.single_novel_folder):
            self.dialog.state_label.setText(
                self.dialog.tr('Creating the download folder!'))
            os.mkdir(self.single_novel_folder)
        else:
            self.dialog.state_label.setText(
                self.dialog.tr('Loading the exit folder!'))

        # json file (to indicate the statue of novels)
        self.status_novel_json_path = os.path.join(
            self.single_novel_folder, f'{self.bookname}_status.json')
        # loading datas from json file
        if os.path.exists(self.status_novel_json_path):
            with open(f'{self.status_novel_json_path}', 'r') as f:
                self.json_data = json.load(f)
                self.downloaded_links = self.json_data['downloaded_links']

        print('Download started!')
        start_time = time.time()
        self.dialog.check_novel_status()
        contents_list = os.listdir(dialog.novel_save_path)
        index_item = contents_list.index('{}'.format(self.bookname))
        self.dialog.status_list[index_item] = 'downloading'
        self.dialog.novel_status_list.clear()
        self.dialog.novel_status_list.addItems(self.dialog.status_list)

        # acceleration
        # print('acceleration')
        for chapter_link in self.chapter_links:
            if not len(self.downloaded_links):
                self.get_content_chapters(chapter_link=chapter_link)
            else: 
                if chapter_link not in self.downloaded_links:
                    self.get_content_chapters(chapter_link=chapter_link)
        
        # if not len(self.downloaded_links):
        #     self.chapter_links = list(set(self.chapter_links) - set(self.downloaded_links))
        # if len(self.chapter_links):
        #     with Pool(4) as pool:
        #         pool.starmap(self.get_content_chapters, zip(self.chapter_links))

        # save data status in the json file
        self.json_data['status'] = 'finished'
        with open(f'{self.status_novel_json_path}', 'w') as f:
            json.dump(self.json_data, f)
        # downloaded status setting
        self.dialog.state_label.setText(self.dialog.tr('Download successfully'))
        self.dialog.check_novel_status()

        end_time = time.time()
        print(f'Time: {np.round((end_time - start_time), 2)}s')

    def get_content_chapters(self, chapter_link):
        print('get_content_chapters function is executed.')
        # if chapter_link in self.exit_content:
        res = requests.get(chapter_link, headers=self.header, timeout=WAIT_TIME)
        res.encoding = 'utf-8'

        result = etree.HTML(res.text)
        title = result.xpath(self.chapter_title_analyze)[0]
        contents = result.xpath(self.chapter_content_analyze)
        # clear the contents
        for content in contents:
            re.sub('\xa0\xa0\xa0\xa0', ' ', content)

        # next page url
        if self.source == 'changyeyuhuo':
            contents_next_url = result.xpath(self.next_chapter_analyze)[0]
            contents_next_url = self.host + contents_next_url
            self.next_chapter_links.append(contents_next_url)

        title_path = os.path.join(self.single_novel_folder, f'{title}.txt')
        if not os.path.exists(title_path):
            f = open(title_path, 'w')
            f.close()

        # download the contents for each chapter
        with open(title_path, 'a+', encoding="utf-8") as f:
            f.write('\n\n' + title + '\n\n')
            f.flush()
            for content in contents:
                f.write('\n\t' + content + '\n')
                f.flush()

        # save data status in the json file
        self.json_data['downloaded_links'].append(chapter_link)
        self.json_data['chapter_names'].append(title)
        with open(f'{self.status_novel_json_path}', 'w') as f:
            json.dump(self.json_data, f)

        # update the Qprogressbar
        exit_number = len(os.listdir(self.single_novel_folder))
        self.dialog.progressbar.setValue(100 * (exit_number-1) / len(self.chapter_links))
        self.dialog.state_label.setText(self.dialog.tr(
            f'\r{self.bookname}\t{np.round(100*(exit_number-1)/len(self.chapter_links))}%\t{title}'))


class LayoutDialog(QMainWindow, spider_UI_layout.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_event()
        self.init_setting()

        # define parameters
        self.spider = None
        self.rank_url, self.book_update_url = "", ''
        self.rank_list, self.name_list, self.book_urls, self.status_list = [], [], [], []
        self.clipboard, self.url_list, self.music_name = None, None, None
        self.genre_urls, self.author_urls, self.novel_name_list = None, None, None
        self.title_list, self.index_content = [], []
        self.current_chapter_index = 0
        self.current_path = None

    def init_setting(self):
        # initial UI setting
        self.novel_save_path = novel_save_path
        self.display_rank_widget()
        self.check_novel_status()
        self.listWidget_menu.setVisible(False)

    def init_event(self):
        # define the slot and signal
        # novel spiders
        self.exit_novel_list.clicked.connect(lambda: self.copy_name(self.exit_novel_list))
        self.rank_book_name_list.clicked.connect(lambda: self.copy_name(self.rank_book_name_list))
        self.rank_genre_list.clicked.connect(lambda: self.copy_name(self.rank_genre_list))
        self.rank_author_list.clicked.connect(lambda: self.copy_name(self.rank_author_list))
        self.search_push_button.clicked.connect(self.search_spider)
        self.exit_novel_list.doubleClicked.connect(self.continue_download)
        self.rank_button.clicked.connect(self.rank_spider)
        self.rank_book_name_list.doubleClicked.connect(self.get_rank_page_info)
        self.novel_status_list.doubleClicked.connect(self.reader_file)
        self.rank_author_list.doubleClicked.connect(lambda: self.get_homepage_rank(self.rank_author_list, self.genre_urls))
        self.rank_genre_list.doubleClicked.connect(lambda: self.get_homepage_rank(self.rank_genre_list, self.author_urls))
        self.rank_newest_chapter_list.doubleClicked.connect(lambda: self.get_homepage_rank(self.rank_newest_chapter_list, self.book_update_url))
        self.rank_intro_list.doubleClicked.connect(self.get_detail_info_rank)
        self.actionclose.triggered.connect(self.app_close)
        self.actionname.triggered.connect(self.display_rank_widget)
        self.actiongenre.triggered.connect(self.display_rank_widget)
        self.actionauthor.triggered.connect(self.display_rank_widget)
        self.actionstatus.triggered.connect(self.display_rank_widget)
        self.actionupdate_chapter.triggered.connect(self.display_rank_widget)
        self.actionintro.triggered.connect(self.display_rank_widget)
        self.Menu_button.clicked.connect(self.reader_button_menu)
        self.Next_button.clicked.connect(lambda: self.reader_button_changed_page('next'))
        self.preview_button.clicked.connect(lambda: self.reader_button_changed_page('back'))
        # self.book_list.doubleClicked.connect(self.get_url_click)
        self.listWidget_menu.clicked.connect(self.reader_menu_click)

        # music spider
        self.pushButton_music.clicked.connect(self.music_spider_search)
        self.music_listWidget.doubleClicked.connect(self.music_spider_download)

    # music signals and slots
    def music_spider_search(self):
        self.status_music_label.setText(self.tr('checking ...'))
        if self.comboBox_music.currentText() == 'QQmusic':
            name_music = self.lineEdit_music.text()
            if not name_music:
                QMessageBox.critical(self, self.tr(
                    'Error'), self.tr('no content'))
            else:
                self.url_list, self.music_name = qq_music_search(
                    ui_test=True, dialog=dialog, key_word=name_music)
                self.status_music_label.setText(self.tr('waiting selection '))

    def music_spider_download(self):
        qq_music_download(self.music_name, self.url_list,
                          ui_test=True, dialog=dialog)

    # continue to download novels
    def continue_download(self):
        name = self.exit_novel_list.currentItem().text()
        self.book_name.setText(name)
        self.search_spider()

    # checking status of exited novels
    def check_novel_status(self):
        # loading the downloaded files and status
        if not os.path.exists(self.novel_save_path):
            os.mkdir(self.novel_save_path)
        self.novel_name_list = os.listdir(self.novel_save_path)
        self.exit_novel_list.clear()  # exited novel list ui
        self.exit_novel_list.addItems(self.novel_name_list)
        # status list ui
        self.novel_status_list.clear()
        self.status_list = []
        # check for book status from json file
        for item in self.novel_name_list:
            path = os.path.join(self.novel_save_path, item)
            path = os.path.join(path, f'{item}_status.json')
            if os.path.exists(path):
                with open(f'{path}', 'r') as f:
                    self.status_json = json.load(f)
                status = self.status_json['status']
                self.status_list.append(f'{status}')
            else:
                self.status_list.append('unknown')
        self.novel_status_list.addItems(self.status_list)

    def reader_file(self):
        # reader
        self.listWidget_menu.setVisible(False) # menu UI
        self.textBrowser.setVisible(True)   # text UI
        self.textBrowser.clear()

        index_item = self.novel_status_list.currentRow()
        name = os.listdir(self.novel_save_path)[index_item]
        self.current_path = os.path.join(self.novel_save_path, name)
        # catch the json data
        path_josn_book = os.path.join(self.current_path, f'{name}_status.json')
        with open(f'{path_josn_book}', 'r') as f:
            status_json = json.load(f)

        self.index_content = status_json['chapter_links']
        self.title_list, self.url_list = status_json['chapter_names'], status_json['chapter_links']

        self.current_chapter_index = 0
        chapter_name = self.title_list[self.url_list.index(self.index_content[self.current_chapter_index])]
        current_path = os.path.join(self.current_path, f'{chapter_name}.txt')

        linecache.clearcache()
        contents = linecache.getlines(current_path)
        self.state_label.setText(self.tr('Loading data ...'))
        self.textBrowser.clear()
        for content in contents:
            if content == '\n':
                pass
            else:
                self.textBrowser.append(content)
        self.state_label.setText(self.tr('Data loaded '))
        self.textBrowser.moveCursor(QTextCursor.Start)

    def reader_button_menu(self):
        if not self.index_content:
            QMessageBox.critical(self, self.tr('no book error'), self.tr('choose book please ! '))
        else:
            self.textBrowser.clear()
            print('Loading Menu')
            self.listWidget_menu.clear()
            self.textBrowser.setVisible(False)
            self.listWidget_menu.setVisible(True)

            for link in self.index_content:
                content = self.title_list[self.url_list.index(link)]
                self.listWidget_menu.addItem(content)

    def reader_menu_click(self):
        index_item = self.listWidget_menu.currentRow()
        self.current_chapter_index = index_item
        self.textBrowser.setVisible(True)
        self.listWidget_menu.setVisible(False)
        chapter_name = self.title_list[self.url_list.index(self.index_content[self.current_chapter_index])]
        path = os.path.join(self.current_path, '{}.txt'.format(chapter_name))

        linecache.clearcache()
        contents = linecache.getlines(path)
        self.state_label.setText(self.tr('Loading data ...'))
        self.textBrowser.clear()
        for content in contents:
            if content == '\n':
                pass
            else:
                self.textBrowser.append(content)
        self.state_label.setText(self.tr('Data loaded '))
        self.textBrowser.moveCursor(QTextCursor.Start)

    def reader_button_changed_page(self, order):
        # page change function
        if order == 'next':
            if self.index_content[self.current_chapter_index] == self.index_content[-1]:
                QMessageBox.information(self, self.tr(
                    'chapter'), self.tr('the final chapter'))
            else:
                self.current_chapter_index += 1

        elif order == 'back':
            if self.index_content[self.current_chapter_index] == self.index_content[0]:
                QMessageBox.information(self, self.tr(
                    'chapter'), self.tr('the first chapter'))
            else:
                self.current_chapter_index -= 1

        chapter_name = self.title_list[self.url_list.index(self.index_content[self.current_chapter_index])]
        path = os.path.join(self.current_path, '{}.txt'.format(chapter_name))

        linecache.clearcache()
        contents = linecache.getlines(path)
        self.state_label.setText(self.tr('Loading data ...'))
        self.textBrowser.clear()
        for content in contents:
            if content == '\n':
                pass
            else:
                self.textBrowser.append(content)
        self.state_label.setText(self.tr('Data loaded '))
        self.textBrowser.moveCursor(QTextCursor.Start)

    def get_homepage_rank(self, content_list, lists):
        index_item = content_list.currentRow()
        self.rank_url = lists[index_item]
        QDesktopServices.openUrl(QUrl(self.rank_url))

    def get_detail_info_rank(self):
        info = self.rank_intro_list.currentItem()
        QMessageBox.information(self, self.tr('intro'), info.text())

    def display_rank_widget(self):
        if self.actionname.isChecked():
            self.rank_book_name_list.setVisible(True)
        else:
            self.rank_book_name_list.setVisible(False)

        if self.actiongenre.isChecked():
            self.rank_author_list.setVisible(True)
        else:
            self.rank_author_list.setVisible(False)

        if self.actionauthor.isChecked():
            self.rank_genre_list.setVisible(True)
        else:
            self.rank_genre_list.setVisible(False)

        if self.actionstatus.isChecked():
            self.rank_status_list.setVisible(True)
        else:
            self.rank_status_list.setVisible(False)

        if self.actionintro.isChecked():
            self.rank_intro_list.setVisible(True)
        else:
            self.rank_intro_list.setVisible(False)

        if self.actionupdate_chapter.isChecked():
            self.rank_newest_chapter_list.setVisible(True)
        else:
            self.rank_newest_chapter_list.setVisible(False)

    @staticmethod
    def app_close():
        # close button in GUI
        current_app = QApplication.instance()
        current_app.quit()

    def copy_name(self, object_name):
        # copy function
        self.clipboard = QGuiApplication.clipboard()
        self.clipboard.setText(object_name.currentItem().text())
        self.statusbar.showMessage(self.tr('copied the name'))

    def get_rank_page_info(self):
        # show rank page info
        if self.source_cobox.currentText() == 'qidian':
            if self.rank_label.text() != 'selected successfully ! ':
                index_item = self.rank_book_name_list.currentRow()

                print(f'index_item: {index_item}')
                self.rank_url = self.rank_list[index_item]
                print(f'self.rank_url: {self.rank_url}')

                self.rank_label.setText(self.tr("selected successfully ! "))
                dic_data = qidian_content_rank(
                    self.rank_list, ui_test=True, dialog=dialog)
                self.book_urls = dic_data['url']
                self.book_update_url = dic_data['update_url']
                self.genre_urls = dic_data['genre_url']
                self.author_urls = dic_data['author_url']
            else:
                index_item = self.rank_book_name_list.currentRow()
                self.rank_url = self.book_urls[index_item]
                QDesktopServices.openUrl(QUrl(self.rank_url))
        else:
            self.rank_label.setText(self.tr('error from the rank sources ! '))

    def rank_spider(self):
        # get rank info
        print('rank_spider is executed')
        self.name_list, self.rank_list = rank_info_qidian_url(
            ui_test=True, dialog=dialog)

    # function to run spiders
    def search_spider(self):
        self.state_label.setText(self.tr("checking..."))
        novel_name = self.book_name.text()
        if novel_name:
            # calling program in spider_without_UI,py
            self.spider = novel_spider(novel_name, self.book_source_combobox.currentText(), dialog=dialog)
            if self.book_source_combobox.currentText() == '笔趣阁':
                self.spider.source = 'biquge'

            elif self.book_source_combobox.currentText() == '长夜烽火':
                self.spider.source = 'changyeyuhuo'

            elif self.book_source_combobox.currentText() == '落霞':
                self.spider.source = 'luoxia'
            
            self.spider.init_parameter()
            self.spider.search_novel()
            if not self.spider.no_result:
                self.state_label.setText(self.tr("waiting selection..."))
                self.book_list.clear()
                self.book_list.addItems(self.spider.result_title_search)
            else:
                self.state_label.setText(
                    self.tr(f"No result ...  from {self.book_source_combobox.currentText()}"))
                self.book_list.clear()

        else:
            QMessageBox.critical(self, self.tr("Error"),
                                self.tr('Unvalid bookname'))


class WorkThread(QThread):
    def __init__(self, book_name, book_source_combobox, state_label, book_list, spider):
        QThread.__init__(self)
        self.book_source_combobox = book_source_combobox
        self.book_name = book_name
        self.state_label = state_label
        self.book_list = book_list
        self.search_url = ''
        self.search_title, self.search_urls = [], []
        self.spider = spider

        # signal function
        self.book_list.doubleClicked.connect(self.get_url_click)

    def spider_run(self):
        if self.book_source_combobox.currentText() == '笔趣阁':
            self.spider.source = 'biquge'

        elif self.book_source_combobox.currentText() == '长夜烽火':
            self.spider.source = 'changyeyuhuo'

        elif self.book_source_combobox.currentText() == '落霞':
            self.spider.source = 'luoxia'

        self.spider.init_parameter()
        self.spider.search_novel()
        if not self.spider.no_result:
            self.state_label.setText(self.tr("waiting selection..."))
            self.book_list.clear()
            self.book_list.addItems(self.spider.result_title_search)
        else:
            self.state_label.setText(self.tr("No result ...  from " + self.book_source_combobox.currentText()))
            self.book_list.clear()

    def get_url_click(self):
        index_item = self.book_list.currentRow()
        self.search_url = self.spider.result_url_search[index_item]
        self.spider.book_search_url = self.search_url
        self.state_label.setText(self.tr("selected successfully ! "))
        self.start()

    def run(self):
        self.spider.spider_running()

if __name__ == '__main__':
    app = QApplication()

    dialog = LayoutDialog()
    dialog.show()
    # enter into QT application loop
    sys.exit(app.exec_())

import re
import os
import json
import time
import linecache
import traceback
import requests
import logging
import random
from lxml import etree
import urllib.parse as parse
from urllib.request import urlretrieve
import UI_of_Spider
from multiprocessing import Pool

# hyper parameter
WAIT_TIME = 5
root_dir = 'Novels'


def rank_info_qidian_url(ui_test=False, dialog=None):
    # get the rank information
    request_content = requests.get(url='https://www.qidian.com/rank', headers=header, timeout=5)
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
        response_temp = requests.get(url=rank_list[num], headers=header, timeout=5)
    else:
        response_temp = requests.get(url=dialog.rank_url, headers=header, timeout=5)

    response_temp.encoding = 'utf-8'
    data = etree.HTML(response_temp.text)
    info_book_name_list = data.xpath('//div[@class="book-img-text"]//div[@class="book-mid-info"]/h2//text()')
    info_book_url_list = data.xpath('//div[@class="book-img-text"]//div[@class="book-mid-info"]/h2//@href')
    info_book_content_list = data.xpath('//p[@class="intro"]//text()')
    info_author = data.xpath('//p[@class="author"]//a[@class="name"]//text()')
    info_status = data.xpath('//p[@class="author"]//span//text()')
    info_genre = data.xpath('//p[@class="author"]//a//text()')
    info_update_chapter_name = data.xpath('//p[@class="update"]/a/text()')
    info_update_url = data.xpath('//p[@class="update"]/a/@href')
    info_author_url = data.xpath('//p[@class="author"]//a[@class="name"]/@href')
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
        dialog.status_music_label.setText(dialog.tr('finding content list ...'))
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
        music_name.append(song_list[i]['name'] + '-' + song_list[i]['singer'][0]['name'])
        url_list.append(str_3 % (song_list[i]['mid']))

        if not ui_test:
            print('{}.{}-{}'.format(i + 1, song_list[i]['name'], song_list[i]['singer'][0]['name']))
        else:
            dialog.music_listWidget.addItem('{}-{}'.format(song_list[i]['name'], song_list[i]['singer'][0]['name']))

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
            urlretrieve(url=download_url, filename='./QQMusic/{}.mp3'.format(music_name[song_index]))
            print('{}.mp3下载完成！'.format(music_name[song_index]))
        except Exception as e:
            print(e, '对不起，你没有该歌曲的版权！')
            logging.warning(traceback.format_exc())

    else:
        try:
            dialog.status_music_label.setText(dialog.tr('start downloading !'))
            urlretrieve(url=download_url, filename='./QQMusic/{}.mp3'.format(music_name[song_index]))
            dialog.status_music_label.setText(dialog.tr('{}.mp3 download successfully！'.format(music_name[song_index])))
        except Exception as e:
            dialog.status_music_label.setText(dialog.tr('cannot download for the permission'))
            print(e, '对不起，你没有该歌曲的版权！')
            logging.warning(traceback.format_exc())


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
header = {"User-Agent": random.choice(user_agent)}
HOSTS = ['https://www.mayiwxw.com/', 'https://www.changyeyuhuo.com']


class novel_spider:

    def __init__(self, bookname, source, ui_set=False, dialog=None):
        self.root_dir = 'Novels'
        self.book_name_search = bookname
        self.ui_set = ui_set
        self.dialog = dialog
        self.source = source
        self.user_agent = [
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
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari"
            "/535.24"
        ]
        self.header = {"User-Agent": random.choice(self.user_agent)}
        self.HOSTS = HOSTS
        self.no_result = False

        # init None parameters
        self.host, self.book_search_url = None, None
        self.data_form, self.result_url_search_analyze = None, None
        self.search_url, self.result_url_search, self.result_title_search = None, None, None
        self.chapter_links, self.bookname = None, None
        self.result_title_search_analyze = None
        self.bookname_analyze, self.chapter_links_analyze = None, None
        self.subfolder, self.menu_save_path, self.status_path = None, None, None
        self.exit_content, self.next_chapter_links = [], []
        self.chapter_title_analyze, self.chapter_content_analyze = None, None
        self.page_analyze = None
        self.next_chapter_analyze = None

        # initial parameters
        self.init_parameter()

    def init_parameter(self):
        if self.source == 'biquge':
            self.host = self.HOSTS[0]
            self.search_url = 'https://www.mayiwxw.com/modules/article/search.php'
            self.data_form = {'searchkey': '11', 'searchtype': 'articlename'}
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
        if self.ui_set:
            self.novel_chapters_loading()
            self.novel_download()
        else:
            self.search_novel()
            self.novel_chapters_loading()
            self.novel_download()

    def search_novel(self):
        try:
            res_search = requests.post(url=self.search_url, data=self.data_form, timeout=10)
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
            if not self.ui_set:
                for title in self.result_title_search:
                    print("{}\t{}".format(self.result_title_search.index(title) + 1, title))
                cursor = input('input the index number: ')
                self.book_search_url = self.result_url_search[int(cursor) - 1]

        except Exception as e:
            print('\n')
            print(e)
            logging.warning(traceback.format_exc())
            self.spider_running()

    # get name and chapter_links
    def novel_chapters_loading(self):
        try:
            response = requests.get(self.book_search_url, headers=self.header, timeout=WAIT_TIME)
            response.encoding = 'utf-8'
            data_response = etree.HTML(response.text)
            self.bookname = data_response.xpath(self.bookname_analyze)[0]

            # luoxia - list  biquge - [9:]
            if isinstance(self.chapter_links_analyze, list):
                self.chapter_links = data_response.xpath(self.chapter_links_analyze[0])
                chapter_links_back = data_response.xpath(self.chapter_links_analyze[1])
                self.chapter_links = chapter_links_back + self.chapter_links
            elif self.source == 'biquge':
                self.chapter_links = data_response.xpath(self.chapter_links_analyze)
                chapter_links = []
                for link in self.chapter_links[9:]:
                    chapter_links.append(self.host + link)
                self.chapter_links = chapter_links
            elif self.source == 'changyeyuhuo':
                whole_book_page = data_response.xpath(self.page_analyze)
                chapter_links = []
                for index_page in whole_book_page:
                    response = requests.get(url=index_page, headers=self.header, timeout=5)
                    response.encoding = 'utf-8'
                    data_response = etree.HTML(response.text)
                    for link in data_response.xpath(self.chapter_links_analyze)[12:]:
                        chapter_links.append(self.host + link)
                self.chapter_links = chapter_links

            # clean the space string
            self.bookname = self.bookname.split(' ')[0]

        except Exception as e:
            print('\n')
            print('Error Message in download spider')
            print(e)
            logging.warning(traceback.format_exc())
            print('save the error message into log file.')
            # self.spider_running()

    def novel_download(self):
        try:
            # setting the sub path
            self.subfolder = os.path.join(root_dir, self.bookname)
            self.status_path = os.path.join(self.subfolder, 'wait_for_download')

            if not os.path.exists(self.subfolder):
                os.makedirs(self.subfolder)
                file = open(self.status_path, 'w')
                file.close()
                if not self.ui_set:
                    print('Creating the download folder!')
                else:
                    self.dialog.state_label.setText(self.dialog.tr('Creating the download folder!'))
            else:
                if not self.ui_set:
                    print('Loading the exit folder!')
                else:
                    self.dialog.state_label.setText(self.dialog.tr('Loading the exit folder!'))
            # Menu path
            self.menu_save_path = os.path.join(self.subfolder, 'Menu_{}'.format(self.bookname))

            # checking the exited chapters
            if os.path.exists(self.menu_save_path):
                exit_contents = linecache.getlines(self.menu_save_path)
                self.exit_content = []
                for i in range(len(exit_contents)):
                    if i % 2 == 1:
                        temp = exit_contents[i].split('\n')[0]
                        self.exit_content.append(temp)
                self.exit_content.sort()
            else:
                print('creating the menu file')

            print('Download started!')
            start_time = time.time()
            if self.ui_set:
                self.dialog.check_novel_status()
                contents_list = os.listdir(UI_of_Spider.novel_save_path)
                index_item = contents_list.index('{}'.format(self.bookname))
                self.dialog.status_list[index_item] = 'downloading'
                self.dialog.novel_status_list.clear()
                self.dialog.novel_status_list.addItems(self.dialog.status_list)

            # save index-file
            index_file_path = os.path.join(self.subfolder, 'index_{}'.format(self.bookname))
            with open(index_file_path, 'w') as f:
                for chapter in self.chapter_links:
                    f.write(chapter + '\n')
                    f.flush()

            # acceleration
            # pool = ThreadPoolExecutor(4)
            # self.next_chapter_links = []
            # for chapter_link in self.chapter_links:
            #     if chapter_link not in self.exit_content:
            #         pool.submit(self.get_content_chapters, chapter_link)
            # # for next page
            # for chapter_link in self.next_chapter_links:
            #     if chapter_link not in self.chapter_links:
            #         if chapter_link not in self.exit_content:
            #             pool.submit(self.get_content_chapters, chapter_link)
            # pool.shutdown()

            with Pool(4) as pool:
                pool.starmap(self.get_content_chapters, zip(self.chapter_links))

            if os.path.exists(self.status_path):
                os.remove(self.status_path)
            if self.ui_set:
                self.dialog.state_label.setText(self.dialog.tr('Download successfully'))
                self.dialog.check_novel_status()
            else:
                print('\nDownload successfully ! ')

            end_time = time.time()
            print('Time: {}'.format(end_time - start_time))

        except Exception as e:
            print('\n')
            print(e)
            logging.warning(traceback.format_exc())
            # self.spider_running()

    def get_content_chapters(self, chapter_link):

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

        title_path = os.path.join(self.subfolder, '{}.txt'.format(title))
        if not os.path.exists(title_path):
            f = open(title_path, 'w')
            f.close()

        with open(title_path, 'a+', encoding="utf-8") as f, open(self.menu_save_path, 'a+', encoding='utf-8') as M:
            f.write('\n\n' + title + '\n\n')
            f.flush()

            for content in contents:
                f.write('\n\t' + content + '\n')
                f.flush()
                # record menu of downloaded content
            M.write('\t' + title + '\n' + chapter_link + '\n')
            M.flush()

        exit_number = len(os.listdir(self.subfolder))

        if not self.ui_set:
            print('\r{}\t{}%\t{}'.format(self.bookname,
                                         format(100 * (exit_number - 2) / len(self.chapter_links), '.2f'), title),
                  end='')
        else:
            # self.dialog.progressbar.setValue(100 * exit_number / len(self.chapter_links+self.next_chapter_links))
            self.dialog.state_label.setText(self.dialog.tr('\r{}\t{}%\t{}').format(self.bookname, format(
                100 * (exit_number - 2) / len(self.chapter_links), '.2f'), title))


if __name__ == '__main__':
    book_name = '11'
    first = novel_spider(bookname=book_name, source='biquge')
    first.spider_running()

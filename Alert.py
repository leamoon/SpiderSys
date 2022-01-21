"""
Author : wumaomao
Time : 2021.1.20
Description: checking the update of novels
"""
import time

import requests
import random
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from lxml import etree

user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
]
header = {"User-Agent": random.choice(user_agent)}
HOST = 'http://www.biquges.com'

# email setting parameters
mail_host = "smtp.qq.com"
mail_user = "1060014562"
mail_pass = "dwwsklhrgaoybbjh"
sender = '1060014562@qq.com'
receivers = ['wumaomaolemoon@gmail.com']


def search_novel(book_name):
    try:
        search_url = 'https://www.biquges.com/modules/article/search.php'
        data_form = {'searchkey': book_name, 'searchtype': 'articlename'}
        res_search = requests.post(
            url=search_url, data=data_form, headers=header)
        res_search.encoding = "utf-8"
        temp1 = etree.HTML(res_search.text)

        # index_search is a index to get a result or not
        index_search = temp1.xpath('//div[@id="tips"]//text()')[0]

        result_search_url = temp1.xpath('//td[@class="even"]//a/@href')
        result_search_chapter = temp1.xpath('//td[@class="even"]//a//text()')
        book_name_searched = temp1.xpath('//td[@class="odd"]//text()')

        print('result : {}'.format(book_name_searched[0]))
        if len(result_search_url) == 0:
            print(index_search)
            return 0

        return HOST+result_search_chapter[0], HOST + result_search_url[0]

    except Exception as e:
        print('------------------------------------------')
        print(e)
        print('------------------------------------------')
        return 0


if __name__ == '__main__':
    last_chapter = '0'

    while True:
        # book = input('Book_name：')
        bookname = '夜的命名术'
        chapter_name, chapter_of_url = search_novel(bookname)
        if last_chapter != '0' and chapter_name != last_chapter:
            print(' Novel :{} has updated !'.format(bookname))

            message = MIMEText('Spider_info', 'plain', 'utf-8')
            message['From'] = Header("Robort_Spider", 'utf-8')
            message['To'] = Header("Master", 'utf-8')
            subject = ' Novel :{} has updated !\n chapter_of_url'.format(
                bookname)
            message['Subject'] = Header(subject, 'utf-8')

            smtp = SMTP_SSL(mail_host)
            smtp.ehlo(mail_host)
            smtp.login(mail_user, mail_pass)
            print('sending !')

            smtp.sendmail(sender, receivers, message.as_string())
            smtp.quit()
            last_chapter = chapter_name

        else:
            last_chapter = chapter_name

        # sleep
        time.sleep(10*60)

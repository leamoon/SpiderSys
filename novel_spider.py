import sys
import random
import requests
import re
from lxml import etree
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QGridLayout, QComboBox, QMessageBox, QApplication, \
    QMainWindow, QWidget
from PyQt5 import QtCore, QtGui


class LayoutDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 300
        self.top = 300
        self.width = 800
        self.height = 600
        # init_widgets
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.setWindowTitle(self.tr("Novel_spider"))

        self.book_name = QLabel(self.tr("Bookname:"))
        self.book_name.setFont(font)
        self.book_name_editor = QLineEdit()
        self.book_name_editor.setFont(font)

        self.movie_source_label = QLabel(self.tr("Source:"))
        self.movie_source_label.setFont(font)
        self.movie_source_combobox = QComboBox()
        self.movie_source_combobox.addItem(self.tr('笔趣阁'))
        self.movie_source_combobox.setFont(font)

        self.search_push_button = QPushButton(self.tr("search"))
        self.search_push_button.setFont(font)

        self.state_label = QLabel(self.tr("None..."))
        self.search_content_label = QLabel(self.tr("State:"))
        self.state_label.setGeometry(QtCore.QRect(90, 100, 131, 41))
        self.state_label.setFont(font)
        self.search_content_label.setFont(font)
        
        self.work = WorkThread()
        self.init_layout().init_event()

    def init_layout(self):
        top_layout = QGridLayout()
        top_layout.addWidget(self.book_name, 0, 0)
        top_layout.addWidget(self.book_name_editor, 0, 1)
        top_layout.addWidget(self.movie_source_label, 0, 2)
        top_layout.addWidget(self.movie_source_combobox, 0, 3)
        top_layout.addWidget(self.search_push_button, 0, 4)
        top_layout.addWidget(self.state_label, 3, 1)
        top_layout.addWidget(self.search_content_label, 3, 0)

        main_frame = QWidget()
        self.setCentralWidget(main_frame)
        main_frame.setLayout(top_layout)

        return self

    def init_event(self):
        # noinspection PyUnresolvedReferences
        self.search_push_button.clicked.connect(self.search)

    def search(self):
        self.state_label.setText(self.tr("checking..."))
        novel_name = self.book_name_editor.text()
        if novel_name:
            self.work.render(novel_name, self.movie_source_combobox, self.state_label)
        else:
            self.critical("insert bookname!")

    def critical(self, message):
        """
        when the movieName is None,
        remind users
        """
        QMessageBox.critical(self, self.tr("Error"),
                             self.tr(message))


class WorkThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def render(self, book_name, movie_source_combobox, state_label):
        self.movie_source_combobox = movie_source_combobox
        self.book_name = book_name
        self.state_label = state_label
        self.start()

    def search_novel(self):
        search_url = 'http://www.biquges.com/modules/article/search.php'
        data_form = {'searchkey': self.book_name}
        res_search = requests.post(url=search_url, data=data_form, headers=header)
        res_search.encoding = "utf-8"
        temp1 = etree.HTML(res_search.text)
        result_search = temp1.xpath('//td[@class="odd"]//a/@href')[0]
        book_search_url = HOST + result_search
        return book_search_url

    def run(self):
        search_url = self.search_novel()
        response = requests.get(search_url, headers=header)
        response.encoding = 'utf-8'
        data = etree.HTML(response.text)
        bookname = data.xpath("//*[@id='info']/h1/text()")[0]
        chapter_links = []
        for link in data.xpath("//*//dd//a/@href")[9:]:
            chapter_links.append(HOST + link)
        save_path = '{}.txt'.format(bookname)
        self.state_label.setText(self.tr("start downloading"))

        with open(save_path, 'w+', encoding="utf-8") as f:
            for i in chapter_links:
                res = requests.get(i, headers=header)
                res.encoding = 'utf-8'
                result = etree.HTML(res.text)
                title = result.xpath('//*[@class="bookname"]/h1/text()')[0]
                contents = result.xpath('//div[@id="content"]/text()')
                for content in contents:
                    re.sub('\xa0\xa0\xa0\xa0', ' ', content)

                f.write('\n\n' + title + '\n\n')
                f.flush()
                for content in contents:
                    f.write(content)
                self.state_label.setText(self.tr('\r{}\t{}%\t{}').format(bookname, format(
                    100 * chapter_links.index(i) / len(chapter_links), '.2f'), title))
        self.state_label.setText(self.tr('{}\tcompletely').format(bookname))


user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
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
HOST = 'http://www.biquges.com'
app = QApplication(sys.argv)
dialog = LayoutDialog()
dialog.show()
app.exec_()

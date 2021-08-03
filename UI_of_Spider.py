import sys
import os
import linecache
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import spider_without_UI
import spider_second_UI
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("MySpider")

# hyper parameters
novel_save_path = './Novels'


class LayoutDialog(QMainWindow, spider_second_UI.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_event()
        self.init_setting()

        self.spider = None
        self.work = WorkThread(self.book_name, self.book_source_combobox, self.state_label, self.book_list, self.spider)
        self.rank_url, self.book_update_url = "", ''
        self.rank_list, self.name_list, self.book_urls, self.status_list = [], [], [], []
        self.clipboard, self.url_list, self.music_name = None, None, None
        self.genre_urls, self.author_urls, self.contents_list = None, None, None
        self.title_list, self.index_content = [], []
        self.current_chapter_index = 0
        self.current_path = None

    def init_setting(self):
        # simple UI setting
        self.display_second_widget()
        self.check_novel_status()
        self.listWidget_menu.setVisible(False)

    def init_event(self):
        # noinspection PyUnresolvedReferences
        self.exit_novel_list.clicked.connect(lambda: self.copy_name(self.exit_novel_list))
        self.content_list1.clicked.connect(lambda: self.copy_name(self.content_list1))
        self.content_list3.clicked.connect(lambda: self.copy_name(self.content_list3))
        self.search_push_button.clicked.connect(self.search_spider)
        self.exit_novel_list.doubleClicked.connect(self.continue_download)
        self.rank_button.clicked.connect(self.rank_spider)
        self.content_list1.doubleClicked.connect(self.get_content)
        self.novel_status_list.doubleClicked.connect(self.reader_file)
        self.content_list2.doubleClicked.connect(lambda: self.get_homepage(self.content_list2, self.genre_urls))
        self.content_list3.doubleClicked.connect(lambda: self.get_homepage(self.content_list3, self.author_urls))
        self.content_list6.doubleClicked.connect(lambda: self.get_homepage(self.content_list6, self.book_update_url))
        self.content_list5.doubleClicked.connect(self.get_detail_info)
        self.actionclose.triggered.connect(self.app_close)
        self.actionname.triggered.connect(self.display_second_widget)
        self.actiongenre.triggered.connect(self.display_second_widget)
        self.actionauthor.triggered.connect(self.display_second_widget)
        self.actionstatus.triggered.connect(self.display_second_widget)
        self.actionupdate_chapter.triggered.connect(self.display_second_widget)
        self.actionintro.triggered.connect(self.display_second_widget)
        self.Menu_button.clicked.connect(self.reader_button_menu)
        self.Next_button.clicked.connect(lambda: self.reader_button_changed_page('next'))
        self.preview_button.clicked.connect(lambda: self.reader_button_changed_page('back'))

        # music spider
        self.pushButton_music.clicked.connect(self.music_spider_search)
        self.music_listWidget.doubleClicked.connect(self.music_spider_download)

    # music signals and slots
    def music_spider_search(self):
        self.status_music_label.setText(self.tr('checking ...'))
        if self.comboBox_music.currentText() == 'QQmusic':
            name_music = self.lineEdit_music.text()
            if not name_music:
                QMessageBox.critical(self, self.tr('Error'), self.tr('no content'))
            else:
                self.url_list, self.music_name = spider_without_UI.qq_music_search(ui_test=True,
                                                                                   dialog=dialog, key_word=name_music)
                self.status_music_label.setText(self.tr('waiting selection '))

    def music_spider_download(self):
        spider_without_UI.qq_music_download(self.music_name, self.url_list, ui_test=True, dialog=dialog)

    # novel spider signals
    def continue_download(self):
        name = self.exit_novel_list.currentItem().text()
        self.book_name.setText(name)
        self.search_spider()

    def check_novel_status(self):
        # loading the downloaded files and status
        self.contents_list = os.listdir(novel_save_path)
        self.exit_novel_list.clear()
        self.exit_novel_list.addItems(self.contents_list)
        self.novel_status_list.clear()
        self.status_list = []
        for item in self.contents_list:
            path = os.path.join(novel_save_path, item)
            path = os.path.join(path, 'wait_for_download')
            if os.path.isfile(path):
                self.status_list.append('waiting')
            else:
                self.status_list.append('downloaded')
        self.novel_status_list.addItems(self.status_list)

    def reader_file(self):
        # reader
        self.listWidget_menu.setVisible(False)
        self.textBrowser.setVisible(True)
        self.textBrowser.clear()

        index_item = self.novel_status_list.currentRow()
        name = os.listdir(novel_save_path)[index_item]
        self.current_path = os.path.join(novel_save_path, name)
        path_of_index = os.path.join(self.current_path, 'index_{}'.format(name))
        path_of_menu = os.path.join(self.current_path, 'Menu_{}'.format(name))

        linecache.clearcache()
        menu_content = linecache.getlines(path_of_menu)
        linecache.clearcache()
        self.index_content = linecache.getlines(path_of_index)
        self.title_list, self.url_list = [], []
        for i in range(len(menu_content)):
            if i % 2 == 0:
                temp = menu_content[i].split('\t')[-1]
                temp1 = temp.split('\n')[0]
                self.title_list.append(temp1)
            else:
                self.url_list.append(menu_content[i])

        self.current_chapter_index = 0
        chapter_name = self.title_list[self.url_list.index(self.index_content[self.current_chapter_index])]
        current_path = os.path.join(self.current_path, '{}.txt'.format(chapter_name))

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

    def reader_button_changed_page(self, order):
        if order == 'next':
            if self.index_content[self.current_chapter_index] == self.index_content[-1]:
                QMessageBox.information(self, self.tr('chapter'), self.tr('the final chapter'))
            else:
                self.current_chapter_index += 1

        elif order == 'back':
            if self.index_content[self.current_chapter_index] == self.index_content[0]:
                QMessageBox.information(self, self.tr('chapter'), self.tr('the first chapter'))
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

    def get_homepage(self, content_list, lists):
        index_item = content_list.currentRow()
        self.rank_url = lists[index_item]
        QDesktopServices.openUrl(QUrl(self.rank_url))

    def get_detail_info(self):
        info = self.content_list5.currentItem()
        QMessageBox.information(self, self.tr('intro'), info.text())

    def display_second_widget(self):
        if self.actionname.isChecked():
            self.content_list1.setVisible(True)
        else:
            self.content_list1.setVisible(False)

        if self.actiongenre.isChecked():
            self.content_list2.setVisible(True)
        else:
            self.content_list2.setVisible(False)

        if self.actionauthor.isChecked():
            self.content_list3.setVisible(True)
        else:
            self.content_list3.setVisible(False)

        if self.actionstatus.isChecked():
            self.content_list4.setVisible(True)
        else:
            self.content_list4.setVisible(False)

        if self.actionintro.isChecked():
            self.content_list5.setVisible(True)
        else:
            self.content_list5.setVisible(False)

        if self.actionupdate_chapter.isChecked():
            self.content_list6.setVisible(True)
        else:
            self.content_list6.setVisible(False)

    @staticmethod
    def app_close():
        current_app = QApplication.instance()
        current_app.quit()

    def copy_name(self, object_name):
        self.clipboard = QGuiApplication.clipboard()
        self.clipboard.setText(object_name.currentItem().text())
        self.statusbar.showMessage(self.tr('copied the name'))

    def get_content(self):
        if self.source_cobox.currentText() == 'qidian':
            if self.rank_label.text() != 'selected successfully ! ':
                index_item = self.content_list1.currentRow()
                self.rank_url = self.rank_list[index_item]
                self.rank_label.setText(self.tr("selected successfully ! "))
                dic_data = spider_without_UI.qidian_content_rank(self.rank_list, ui_test=True, dialog=dialog)
                self.book_urls = dic_data['url']
                self.book_update_url = dic_data['update_url']
                self.genre_urls = dic_data['genre_url']
                self.author_urls = dic_data['author_url']
            else:
                index_item = self.content_list1.currentRow()
                self.rank_url = self.book_urls[index_item]
                QDesktopServices.openUrl(QUrl(self.rank_url))
        else:
            self.rank_label.setText(self.tr('error from the rank sources ! '))

    def rank_spider(self):
        self.name_list, self.rank_list = spider_without_UI.rank_info_qidian_url(ui_test=True, dialog=dialog)

    def search_spider(self):
        self.state_label.setText(self.tr("checking..."))
        novel_name = self.book_name.text()
        if novel_name:

            self.spider = spider_without_UI.novel_spider(novel_name, self.book_source_combobox.currentText(),
                                                         ui_set=True, dialog=dialog)
            self.work = WorkThread(novel_name, self.book_source_combobox, self.state_label, self.book_list, self.spider)
            self.work.spider_run()

        else:
            QMessageBox.critical(self, self.tr("Error"), self.tr('NO bookname'))


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
    app = QApplication(sys.argv)
    dialog = LayoutDialog()
    dialog.show()
    sys.exit(app.exec_())

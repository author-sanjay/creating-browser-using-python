import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser= QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))   #getting home page of browser
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #nav bar
        navbar = QToolBar()       #navigation bar
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)   #back button in browser
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forwrd_btn = QAction('Forward', self)   #forwrd button in browser
        forwrd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forwrd_btn)

        home = QAction('Home', self)     #home button in browser
        home.triggered.connect(self.navigate_home)
        navbar.addAction(home)

        reload= QAction('Reload', self)   #reload button in browser
        reload.triggered.connect(self.browser.reload)
        navbar.addAction(reload)

        self.url_bar = QLineEdit()     #adding text area for entering url
        self.url_bar.returnPressed.connect(self.navigate_to_Url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)   #noting url change in text area

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))   #setting home url

    def navigate_to_Url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url2):
        self.url_bar.setText(url2.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Illumina')
window = MainWindow()
app.exec_()


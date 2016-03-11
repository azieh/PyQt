from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import urllib.request

class PyDownloader(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()

        self.url = QLineEdit()
        self.url.setPlaceholderText("URL address")
        self.save_location = QLineEdit()
        self.save_location.setPlaceholderText("File save location")
        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)
        download = QPushButton("Download")

        layout.addWidget(self.url,            0, 0)
        layout.addWidget(self.save_location,  1, 0)
        layout.addWidget(download,            2, 0)
        layout.addWidget(self.progress,            2, 1)

        self.setLayout(layout)
        self.setWindowTitle("PyDownloader")
        self.setFocus()

        download.clicked.connect(self.download)

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:

            QMessageBox.warning(self, "Warning", "Problem is " + str(urllib.request.HTTPError))
            print(urllib.request.HTTPError)
            return
        QMessageBox.information(self, "Information", "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")


    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))

app = QApplication(sys.argv)

dl = PyDownloader()
dl.show()

app.exec_()
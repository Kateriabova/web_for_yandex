import sys
import traceback
from io import BytesIO

from PIL import Image

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import requests
from PyQt5.uic.properties import QtWidgets


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)

sys.excepthook = excepthook

class MainWindow(QMainWindow):
    g_map: QLabel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('untitled.ui', self)
        self.z = 15
        self.x = -0.123402
        self.y = 51.530828
        map_params = {
        "ll": ",".join([str(self.x), str(self.y)]),
        'z': self.z,
        "l": "map",
        'size': '400,400'}

        map_api_server = "http://static-maps.yandex.ru/1.x/"
        # ... и выполняем запрос
        response = requests.get(map_api_server, params=map_params)
        print(response.url)
        Image.open(BytesIO(response.content)).save('map.png')
        pixmap = QPixmap('map.png')
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp: #minus!
            self.z += 1
            print(self.z)
            if self.z > 23:
                self.z = 23
            else:
                map_params = {
                    "ll": ",".join([str(self.x), str(self.y)]),
                    'z': self.z,
                    "l": "map",
                    'size': '400,400'}

                map_api_server = "http://static-maps.yandex.ru/1.x/"
                # ... и выполняем запрос
                response = requests.get(map_api_server, params=map_params)
                print(response.url)
                Image.open(BytesIO(response.content)).save('map.png')
                pixmap = QPixmap('map.png')
                self.label.setPixmap(pixmap)
        if event.key() == Qt.Key_PageDown: #plus!
            self.z -= 1
            print(self.z)
            if self.z < 0:
                self.z = 0
            else:
                map_params = {
                    "ll": ",".join([str(self.x), str(self.y)]),
                    'z': self.z,
                    "l": "map",
                    'size': '400,400'}

                map_api_server = "http://static-maps.yandex.ru/1.x/"
                # ... и выполняем запрос
                response = requests.get(map_api_server, params=map_params)
                print(response.url)
                Image.open(BytesIO(response.content)).save('map.png')
                pixmap = QPixmap('map.png')
                self.label.setPixmap(pixmap)
        if event.key() == Qt.Key_Right: #right
            print('yees')
            if self.z != 0:
                self.x += 1.0
            map_params = {
                "ll": ",".join([str(self.x), str(self.y)]),
                'z': self.z,
                "l": "map",
                'size': '400,400'}

            map_api_server = "http://static-maps.yandex.ru/1.x/"
            # ... и выполняем запрос
            response = requests.get(map_api_server, params=map_params)
            print(response.url)
            Image.open(BytesIO(response.content)).save('map.png')
            pixmap = QPixmap('map.png')
            self.label.setPixmap(pixmap)
        if event.key() == Qt.Key_Left: #left
            self.z -= 1
            print(self.z)
            if self.z < 0:
                self.z = 0
            else:
                map_params = {
                    "ll": ",".join([str(self.x), str(self.y)]),
                    'z': self.z,
                    "l": "map",
                    'size': '400,400'}

                map_api_server = "http://static-maps.yandex.ru/1.x/"
                # ... и выполняем запрос
                response = requests.get(map_api_server, params=map_params)
                print(response.url)
                Image.open(BytesIO(response.content)).save('map.png')
                pixmap = QPixmap('map.png')
                self.label.setPixmap(pixmap)
        if event.key() == Qt.Key_Up: #up
            self.z -= 1
            print(self.z)
            if self.z < 0:
                self.z = 0
            else:
                map_params = {
                    "ll": ",".join([str(self.x), str(self.y)]),
                    'z': self.z,
                    "l": "map",
                    'size': '400,400'}

                map_api_server = "http://static-maps.yandex.ru/1.x/"
                # ... и выполняем запрос
                response = requests.get(map_api_server, params=map_params)
                print(response.url)
                Image.open(BytesIO(response.content)).save('map.png')
                pixmap = QPixmap('map.png')
                self.label.setPixmap(pixmap)
        if event.key() == Qt.Key_Down: #down
            self.z -= 1
            print(self.z)
            if self.z < 0:
                self.z = 0
            else:
                map_params = {
                    "ll": ",".join([str(self.x), str(self.y)]),
                    'z': self.z,
                    "l": "map",
                    'size': '400,400'}

                map_api_server = "http://static-maps.yandex.ru/1.x/"
                # ... и выполняем запрос
                response = requests.get(map_api_server, params=map_params)
                print(response.url)
                Image.open(BytesIO(response.content)).save('map.png')
                pixmap = QPixmap('map.png')
                self.label.setPixmap(pixmap)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())


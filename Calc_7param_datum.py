#!/usr/bin/python3
# coding=utf-8
import random
import string
## Импорт класса основного окна
from in_out_form_7par import Ui_Qt7parWindow

## Отсюда импорт всех инструментов
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

## Эти видимо нахер
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
## __________________________

elips_par={'wgs84':[6378137.0,6356752,314],'Красовского 1942':[6378245.0,6356863.019]}
elips_list=set(elips_par.keys())
import sys, os
class QtMainWindow7Par(QMainWindow, Ui_Qt7parWindow):
#class QtMainWindow7Par(Ui_Qt7parWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		#Тюнинг интерфейса))
		self.comboBox_elips_wgs.addItems(elips_list)
		
		#----------
		self.pushButtonPushme.clicked.connect(self.buttonClicked) #События по нажатию на кнопку
		self.Button_open_wgs.clicked.connect(self.buttonOpenClicked) #События по нажатию на кнопку
		self.buttonBoxOkCancel.accepted.connect(self.buttonClicked) #Вешаем на кнопку ОК действие
		
	def generate_pins(self, size=6, chars=string.digits): #Функция для генерации ключей
		return ''.join(random.choice(chars) for x in range(size))
		
	def buttonClicked(self): # функция которая вешается на кнопку
		self.textEdit.append(self.generate_pins(10))
	def buttonOpenClicked(self):
		DataDir = os.path.dirname(__file__)
		shpfilename = QFileDialog.getOpenFileName(self, 'Выберете файл в эталонной СК', DataDir, filter='*.csv,*.txt')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form=QtMainWindow7Par()
	form.show()
	app.exec()

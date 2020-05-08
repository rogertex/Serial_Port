'''
@Author: Roger
@Date: 2020-05-01 09:30:21
@LastEditors: Roger
@LastEditTime: 2020-05-06 20:47:47
@Email: qunlin.gu@163.com
@Version: 1.0
@Description: 
'''

from PyQt5 import QtWidgets as qw, QtGui, QtCore as qc

import sys
from Ui_form1 import Ui_MainWindow as Uart_ui

import serial
import threading
class Uart (qw.QMainWindow, Uart_ui):
    def __init__(self):
      super(Uart, self).__init__()
      self.setupUi(self)
      # initialized *ini files.
      self.settings = qc.QSettings("config.ini",qc.QSettings.IniFormat)
      self.settings.setIniCodec("UTF-8")
      self.config_uart_baud = self.settings.value("SETUP/UART_BAUD",0,type=int)
      #initialized default parameters
      self.radioButton_rcv_ascii.setChecked(True)
      self.radioButton_std_ascii.setChecked(True)
      self.spinBox.setRange(100, 30*1000)  # 设置时间范围
      self.spinBox.setSingleStep(100)
      self.spinBox.setWrapping(True)
      self.spinBox.setValue(1000)

      self.comboBox_baud.setCurrentText(str(self.config_uart_baud))

      print(self.config_uart_baud)
      #link signals and slots
      self.comboBox_baud.currentIndexChanged.connect(self.comboBox_baud_cb)
      self.btn_send.clicked.connect(self.btn_send_cb)
      self.action_start.triggered.connect(self.action_start_cb)
      self.action_pause.triggered.connect(self.action_pause_cb)
      self.action_stop.triggered.connect(self.action_stop_cb)
      self.action_clean.triggered.connect(self.action_clean_cb)
      self.radioButton_rcv_ascii.toggled.connect(self.radioButton_rcv_ascii_cb)
      self.radioButton_std_ascii.toggled.connect(self.radioButton_std_ascii_cb)
      self.radioButton_rcv_hex.toggled.connect(self.radioButton_rcv_hex_cb)
      self.radioButton_std_hex.toggled.connect(self.radioButton_std_hex_cb)
      self.checkBox_auto_line.toggled.connect(self.checkBox_auto_line_cb)
      self.checkBox_display_std.toggled.connect(self.checkBox_display_std_cb)
      self.checkBox_display_time.toggled.connect(self.checkBox_display_time_cb)
      self.checkBox_resend.toggled.connect(self.checkBox_resend_cb)
      self.spinBox.valueChanged.connect(self.spinBox_cb)

      #initial form
      self.statusbar.showMessage('status ', 1000)
    #   self.setWindowTitle('串口调试助手ROG')

    #combox list index change event

    def comboBox_baud_cb(self):
        content = "你当前选择了"+self.comboBox_baud.currentText()
        qw.QMessageBox.information(
            self, '提示', content, qw.QMessageBox.Yes | qw.QMessageBox.No)
    #Button click event

    def btn_send_cb(self):
        # text = self.textEdit_get.toPlainText()
        #  print('test is',text)
        # self.comboBox_uart.addItem(text)
        uart_baud = self.comboBox_baud.currentText()
        print(uart_baud)
        self.settings.setValue("SETUP/UART_BAUD",uart_baud)


    # menu acktion event.

    def action_start_cb(self):
        print('you clicked the start menu.')

    def action_pause_cb(self):
        print('you clicked the pause menu.')

    def action_stop_cb(self):
        print('you clicked the stop menu.')

    def action_clean_cb(self):
        print('you clicked the clean menu.')

    def radioButton_rcv_ascii_cb(self):
        print('you select receive ascii ratiobutton')

    def radioButton_std_ascii_cb(self):
        print('you select send ascii ratiobutton')

    def radioButton_rcv_hex_cb(self):
        print('you select receive hex ratiobutton')

    def radioButton_std_hex_cb(self):
        print('you select send hex ratiobutton')

    def checkBox_auto_line_cb(self):
        print('you checked checkbox_auto_line')
        result_auto_line = self.checkBox_auto_line.isChecked()
        print(result_auto_line)

    def checkBox_display_std_cb(self):
        print('you checked checkbox_display_std')

    def checkBox_display_time_cb(self):
        print('you checked checkbox_display_time')

    def checkBox_resend_cb(self):
        print('you checked checkbox_resend_cb')
    def spinBox_cb(self,value): # 信号把spinbox 的值发给了槽.
        print('spin box current value is',value)

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    u = Uart()
    u.show()
    sys.exit(app.exec_())

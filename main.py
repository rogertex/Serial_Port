# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roger <qunlin.gu@163.com>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 10:20:15 by roger             #+#    #+#              #
#    Updated: 2020/05/01 10:20:15 by roger            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from PyQt5 import QtWidgets,QtGui,QtCore

import sys
from Ui_form1 import Ui_MainWindow as uart_ui

class Uart (QtWidgets.QMainWindow,uart_ui):
    def __init__(self):
      super(Uart,self).__init__()
      self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    u = Uart()
    u.show()
    sys.exit(app.exec_())

     
    

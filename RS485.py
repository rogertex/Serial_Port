'''
@Author: Roger
@Date: 2020-05-07 20:04:17
@LastEditors: Roger
@LastEditTime: 2020-05-08 20:52:13
@Email: qunlin.gu@163.com
@Version: 
@Description: 
'''
import sys
import serial
import threading
from time import sleep
class Uart(object):
    def __init__(self,port,baud):
        self.err = 0
    #  open serial
        try:
            self.serial = serial.Serial(port,baud)
            
            print('open port success!')
        except :
            print('open port fail!')
            self.err =1
    def uart_recv_thread(self):
        print('start uart receive thread')
        while(True):
            try:
                recv_raw_data = self.serial.readline()   
                raw_data = "Device->pc " + recv_raw_data.decode()   
                print(raw_data)
            except:
                print('receive data error')
                break
    def recv_thread(self):
        thread = threading.Thread(target=self.uart_recv_thread, daemon=True)
        thread.start()

    def send_uart_data(self,data):
         self.serial.write(data.encode("gbk"))  

    def uart_close(self):
        self.serial.close()
             
if __name__ == "__main__":
    
    myuart = Uart("COM2",9600)
    if myuart.err==0:
        print("it's done")
    #如果打开串口成功,开始接受线程.
    myuart.recv_thread()
    origin_data=''
    while(True):
        type_data = input('please key data...')
        
        if (type_data=='quit'):
            #退出
            myuart.uart_close()
            break
        elif type_data != origin_data:
            #发送数据
            myuart.send_uart_data(type_data)
            origin_data = type_data
        sleep(0.05)  
    print("exit")
            

      
      
      
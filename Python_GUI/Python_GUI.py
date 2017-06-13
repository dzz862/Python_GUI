import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QTimer
from CCtrl import CMouseCtrl



class Form(QWidget):

    def __init__(self, name):

        super().__init__()
        self.IniForm(name)
        self.IniTimer()

    def IniForm(self, name):

        form = QWidget()
        form.resize(800, 450)
        form.setWindowTitle(name)
        form.move(1000,1000)

        self.rec_btn = QPushButton('Start Record', self)
        self.rec_btn.resize(100, 60)
        self.rec_btn.move(form.width()/2-self.rec_btn.width()/2 - 55, form.height()/2-self.rec_btn.height()/2)
        self.rec_btn.clicked.connect(self.StartRecord)

        self.ply_btn = QPushButton('Start RePlay', self)
        self.ply_btn.resize(100, 60)
        self.ply_btn.move(form.width()/2-self.rec_btn.width()/2 + 55, form.height()/2-self.rec_btn.height()/2)
        self.ply_btn.clicked.connect(self.StartPlay)

        self.lab = QLabel('this is the mouse point', self)
        self.lab.resize(200,30)
        self.lab.move(self.rec_btn.x(), self.rec_btn.y()-40)

    def IniTimer(self):
        self.rec_timerflag = False
        self.rec_timer = QTimer()
        self.rec_timer.setInterval(50)
        self.rec_timer.timeout.connect(self.RecordPath)

        self.ply_timerflag = False
        self.ply_timer = QTimer()
        self.ply_timer.setInterval(100)
        self.ply_timer.timeout.connect(self.PlayPath)
        
        self.path = []

    def StartRecord(self):

        if self.rec_timerflag:
            self.rec_timerflag = False
            self.rec_timer.stop()
            self.rec_btn.setText('Start Record')          

        else:
            self.rec_timerflag = True
            self.rec_timer.start()
            self.rec_btn.setText('Stop Record')

    def StartPlay(self):
        if self.rec_timerflag == False and self.ply_timerflag:
            self.ply_timerflag = False
            self.ply_timer.stop()
            self.ply_btn.setText('Start Play')          

        if self.rec_timerflag == False and self.ply_timerflag == False:
            self.ply_timerflag = True
            self.ply_timer.start()
            self.ply_btn.setText('Stop Play')

    def RecordPath(self):
        p_x, p_y = ctrl.Get_Mouse_Local()
        self.lab.setText(p_x.__str__() + ',' + p_y.__str__())
        self.path.append([p_x,p_y])

    def PlayPath(self):
        if(len(self.path) > 0):
            p_x, p_y = self.path.pop(0)
            ctrl.Move_Mouse(p_x, p_y)
        else:
            self.ply_timerflag = False
            self.ply_timer.stop()
            self.ply_btn.setText('Start Play')
        

#class Point(Structure):
# _fields_ = [("x", c_ulong),("y", c_ulong)]
#def get_mouse_point():
# po = Point()
# windll.user32.GetCursorPos(byref(po))
# return int(po.x), int(po.y)
#def mouse_click(x=None,y=None):
# if not x is None and not y is None:
#     mouse_move(x,y)
#     time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#def mouse_dclick(x=None,y=None):
# if not x is None and not y is None:
#     mouse_move(x,y)
#     time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#def mouse_move(x,y):
# windll.user32.SetCursorPos(x, y)
#def key_input(str=''):
# for c in str:
#     win32api.keybd_event(VK_CODE[c],0,0,0)
#     win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
#     time.sleep(0.01)

###if __name__ == "__main__":
#while 1:
#    mouse_click(800,600)
#    time.sleep(5)
#    str = 'hello'
#    key_input(str)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    msgbox = QMessageBox()

    form = Form('this is a test form')
    form.show()
    ctrl = CMouseCtrl
    #ctrl.Move_Mouse(350, 20)
    #ctrl.Mouse_Click(0,0)
    #ctrl.Get_Mouse_Local()
    
    #msgbox.setText(ctrl.Get_Mouse_Local().__str__())
    #msgbox.show()

    sys.exit(app.exec_())

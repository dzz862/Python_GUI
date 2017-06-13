import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel
from CCtrl import CMouseCtrl



class Form(QWidget):
    def __init__(self, name):

        super().__init__()
        self.IniForm(name)

    def IniForm(self, name):

        form = QWidget()
        form.resize(800, 450)
        form.setWindowTitle(name)
        form.move(1000,1000)

        btn = QPushButton('This is a test button', self)
        btn.resize(200, 60)
        btn.move(form.width()/2-btn.width()/2, form.height()/2-btn.height()/2)
        btn

        lab = QLabel('this is a test message', self)
        lab.resize(200,30)
        lab.move(btn.x(), btn.y()-40)


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
    ctrl.Move_Mouse(350, 20)
    ctrl.Mouse_Click(0,0)
    #ctrl.Get_Mouse_Local()
    
    msgbox.setText(ctrl.Get_Mouse_Local().__str__())
    msgbox.show()

    sys.exit(app.exec_())

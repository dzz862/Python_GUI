import win32api
import win32con
import win32gui
from ctypes import *
import time

class CMouseCtrl():

    def Get_Mouse_Local():
        return win32gui.GetCursorPos()

    def Move_Mouse(x, y):
        windll.user32.SetCursorPos(x, y)


    def Mouse_Click(LMR, SD):

        #hwndmain = win32gui.FindWindow(0, 'Python')
        #hwndbtn = win32gui.FindWindowEx(hwndmain, 0, 0, 'This is a test button')
        #win32gui.PostQuitMessage(

        if(LMR == 0):
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            if(SD == 1):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        
        if(LMR == 1):
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
            if(SD == 1):
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

        if(LMR == 2):
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN | win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
            if(SD == 1):
                win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN | win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)    
                

    #def Mouse_Wheel(UD):

    


if __name__ == '__main__':

    ctrl = CCtrl()
    ctrl.Get_Mouse_Local()



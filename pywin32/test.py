# coding=utf-8

import win32gui
import win32ui
import win32con
import win32api


def window_capture(filename):
    hwnd = win32gui.FindWindow(None, "Windows PowerShell")

    hwndDC = win32gui.GetWindowDC(hwnd)

    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()

    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]

    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    win32gui.DeleteObject(saveBitMap.GetHandle())


if __name__ == "__main__":
    window_capture("photo.jpg")

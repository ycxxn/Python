from tkinter import *
import serial
import time
import cv2

ser=serial.Serial("COM5", baudrate = 115200 , timeout = 1)

def R1(data):
    senddata=bytearray()
    senddata.append(data)
    return senddata

def processRight():
    for i in range(10):
        print("Right")
        RXD=R1(1)
        ser.write(RXD)

def processLeft():
    for i in range(10):
        print("Left")
        LXD=R1(2)
        ser.write(LXD)

def processUp():
    for i in range(10):
        print("Up")
        UXD=R1(3)
        ser.write(UXD)
    
def processDown():
    for i in range(10):
        print("Down")
        DXD=R1(4)
        ser.write(DXD)

def main():
    window=Tk()
    button_Right=Button(window,text="往右",command=processRight)
    button_Left=Button(window,text="往左",command=processLeft)
    button_Up=Button(window,text="往上",command=processUp)
    button_Down=Button(window,text="往下",command=processDown) 

    button_Right.pack()
    button_Left.pack()
    button_Up.pack()
    button_Down.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

RPi.GPIO.setmode(GPIO.BCM)
ledGreen = LED(17)
ledBlue = LED(27)
ledRed = LED(22)

#GUI Definitions
win = Tk()
win.title("LED Toggler")
win.minsize(150,100)
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

#Event functions
def ledToggle():
        colour = var.get()
        if colour == "green":
                ledBlue.off()
                ledRed.off()
                ledGreen.on()
        else if colour == "blue":
                ledRed.off()
                ledGreen.off()
                ledBlue.on()
        else if colour == "red":
                ledGreen.off()
                ledBlue.off()
                ledRed.on()

#Widgets
var = StringVar()
Radiobutton(win, text="Green", font=myFont, variable=var, value="green", command=ledToggle).pack(anchor=W)
Radiobutton(win, text="Blue", font=myFont, variable=var, value="blue", command=ledToggle).pack(anchor=W)
Radiobutton(win, text="Red", font=myFont, variable=var, value="red", command=ledToggle).pack(anchor=W)

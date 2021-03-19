from Tkinter import *
import tkFont
from gpiozero import LED
import RPi.GPIO as GPIO


#hardware
ledBlue  = 22    # pin22
ledGreen = 18    # pin18
ledRed   = 16    # pin16

GPIO.setmode(GPIO.BOARD)       # GPIO Numbering of Pins
GPIO.setup(ledBlue, GPIO.OUT)   # Set ledPin as output
GPIO.output(ledBlue, GPIO.LOW)  # Set ledPin to LOW to turn Off the LED
GPIO.setup(ledGreen, GPIO.OUT)   # Set ledPin as output
GPIO.output(ledGreen, GPIO.LOW)  # Set ledPin to LOW to turn Off the LED
GPIO.setup(ledRed, GPIO.OUT)   # Set ledPin as output
GPIO.output(ledRed, GPIO.LOW)  # Set ledPin to LOW to turn Off the LED

## GUI Definations ###
win = Tk()
win.title("LED Selector")
myFont = tkFont.Font(family = 'Helvetica', size = 12, weight = 'bold')

var = StringVar()
l = Label(win, bg='white', width=20, text='No Button Selected')
l.pack()

### WIDGETS #####
def ledToggle():
    buttonVal = var.get()
    l.config(text= buttonVal + ' Button pressed')
    if buttonVal == 'RED':
        print 'LED Red ON'
        GPIO.output(ledGreen, GPIO.LOW)
        GPIO.output(ledBlue, GPIO.LOW)
        GPIO.output(ledRed, GPIO.HIGH)   # LED OFF
        
    elif buttonVal == 'GREEN':
        print 'LED Green ON'
        GPIO.output(ledRed, GPIO.LOW)
        GPIO.output(ledBlue, GPIO.LOW)
        GPIO.output(ledGreen, GPIO.HIGH)   # LED ON
        
    else:
        print 'LED Blue ON'
        GPIO.output(ledRed, GPIO.LOW)
        GPIO.output(ledGreen, GPIO.LOW)
        GPIO.output(ledBlue, GPIO.HIGH)   # LED ON
          

def close():
    GPIO.cleanup()
    win.destroy()

r1 = Radiobutton(win, text='Turn Red LED On', variable=var, value='RED', font = myFont, command=ledToggle)
r1.pack()
r2 = Radiobutton(win, text='Turn Green LED On', variable=var, value='GREEN', font = myFont, command=ledToggle)
r2.pack()
r3 = Radiobutton(win, text='Turn Blue LED On', variable=var, value='BLUE', font = myFont, command=ledToggle)
r3.pack()

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.pack()
 
win.protocol("WM_DELETE_WINDOW", close) ## exit cleanly

win.mainloop() # loop forever

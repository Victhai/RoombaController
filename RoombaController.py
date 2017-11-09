import serial
import time
import RPi.GPIO as GPIO
#from tkinter import *
#from tkinter import ttk


class Roomba():
    def __init__(self):
	self.ser = Serial('/dev/ttyAMA0', 115200)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(16, GPIO.OUT)
	
    def wakeUp(self):
	GPIO.output(16, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(16, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(16, GPIO.HIGH)
	time.sleep(2)
	
    def switchMode(self, mode)
	if mode == "Safe":
            self.ser.write(chr(131))
	elif mode == "Full":
            self.ser.write(chr(132))
	else:
            print ("No mode named: {}".format(mode))
		
	time.sleep(0.5)
	
    def sendCommand(self, command):
	if command == "start":
	    self.ser.write(chr(128))
	elif command == "stop":
	    self.ser.write(chr(173))
	elif command == "clean":
	    self.ser.write(chr(135))
	elif command == "pauseClean":
	    self.ser.write(chr(135))
    	elif command == "spot":
            self.ser.write(chr(134))
    	elif command == "dock":
            self.ser.write(chr(143))
    	elif command == "powerDown":
            self.ser.write(chr(133))
	else:
            print ("Not a valid command")
	
        time.sleep(0.5)

#class Gui():
#    def __init__(self):
#	self.root = Tk()
#		
#    def setup(self):
#	self.root.title("iRobot Roomba Controller")
#		
#    def startGui(self):
#	self.root.mainloop()


def main():
    roomba = Roomba()
    roomba.wakeUp()
    roomba.switchMode("Safe")
    roomba.sendCommand("spot")
    
    #gui = Gui()
    #gui.setup()
    #gui.startGui()

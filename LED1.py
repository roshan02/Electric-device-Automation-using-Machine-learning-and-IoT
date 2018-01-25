import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
file1 = open("output.txt", "r")
c = file1.readline()
c = c.strip()
c = int(c)
while(c):
	y = c
#for x in range(0,10):
	#y = input("What is the light amount expected? (0,1,2,3,4:exit) ")
	#print "Light amount expected is: ", y
	if y == 0:
		print "Red LED off"
		GPIO.output(2,GPIO.LOW)
		print "Yellow LED off"
		GPIO.output(17,GPIO.LOW)
		print "Green LED off"
		GPIO.output(4,GPIO.LOW)
		time.sleep(1)
	if y == 1:
		print "Red LED on"
		GPIO.output(2,GPIO.HIGH)
		print "Yellow LED off"
		GPIO.output(17,GPIO.LOW)
		print "Green LED off"
		GPIO.output(4,GPIO.LOW)
		time.sleep(1)
	if y == 2:
		print "Red LED on"
		GPIO.output(2,GPIO.HIGH)
		print "Yellow LED on"
		GPIO.output(17,GPIO.HIGH)
		print "Green LED off"
		GPIO.output(4,GPIO.LOW)
		time.sleep(1)
	if y == 3:
		print "Red LED on"
		GPIO.output(2,GPIO.HIGH)
		print "Yellow LED on"
		GPIO.output(17,GPIO.HIGH)
		print "Green LED on"
		GPIO.output(4,GPIO.HIGH)
		time.sleep(1)
	c = file1.readline()
	c = c.strip()
	c = int(c)
	if y == 4:
		break


print "Red LED off"
GPIO.output(2,GPIO.LOW)
print "Yellow LED off"
GPIO.output(17,GPIO.LOW)
print "Green LED off"
GPIO.output(4,GPIO.LOW)

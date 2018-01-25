import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while 1: 
	ret, img = cap.read()
	#img_file = raw_input("Name of the image file:")
	#img_file = '5.png'
	#gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # grayscale
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	
	#print type(gray_img)
	#print 'Gray shape:', gray_img.shape
	r=gray_img.shape[0]
	c=gray_img.shape[1]
	#print(r)
	#print(c)
	s=0
	for x in range(0,r):
		for y in range(0,c):
			s = s + gray_img[x,y]


	i = (((s/(r*c)) / 255.0) * 100)

	print "The Light(Greyscale) intensity is: ",i

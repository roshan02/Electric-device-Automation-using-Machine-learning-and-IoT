
AWS :
	S3(Simple Storage service) : To store the dataset
	Machine Learning service : To generate the prediction model 

Regression Model (Machine Learning):
	
Used Raspberry Pi 3 in this project.

Python Dependencies to be installed :
Numpy
Pandas 
Opencv
Matplotlib
Scikit-learn

On Laptop : Terminal > python <file_name>

cam2.py : This gives natural light intensity as output(in %) (Using Image processing in Python Opencv)
		[Converting the image after continuously capturing from webcam to Grayscale and then finding Average Grayscale intensity(value) for complete image : Refer program for formula  ]
cam3.py : This gives 1,2,3 (Categorisation done in above program ) as output which can be given be passed to output.txt on raspberry pi usingUse of Prediction Algorithms in Smart Homes shell command :
		 > python cam2.py | ssh pi@10.42.0.202 "cat > output.txt" 

On Raspberry pi : Terminal > python <file_name>
![alt text](https://github.com/roshan02/Electricity--Automation-using-Machine-learning-and-IoT/blob/master/Raspberry-1.jpg = 250x250)

![alt text](https://github.com/roshan02/Electricity--Automation-using-Machine-learning-and-IoT/blob/master/raspberry_pi_circuit_fig.jpg)

LED.py : You have to give input to this program using command line interface 
LED1.py : This program reads the .txt file and then manipulate the lights placed on the breadboard 
		(GPIO pins used in this case : 2,4,17(Serial pin no. : 3,7,11) and 6 for ground )	
		You can refer Images below for Breadboard connections

How to connect to Raspberry Pi ?

Default OS :Raspbian
Default Username : pi
Default password : raspberry 

Important setting (Ethernet):

1) Connect Raspberry Pi 3 using Ethernet Cable.
2) Click on network connection icon in status bar on right top corner of your ubuntu screen .
3) Go to Edit connection option.
4) Click on wired connection and click on Edit.
5) Go to IPv4 settings.
6) In method , choose : "shared to other computers" (This is important)
	(By default , it is DHCP using which it will not work and this step is important.)

Finding the ip address of raspberry Pi 3 which will be required in both the methods :
>cat /var/lib/misc/dnsmasq.leases
1516528149 b8:27:eb:12:6a:d7 10.42.0.202 raspberrypi 01:b8:27:eb:12:6a:d7

So,in this case , The IP address to be used :10.42.0.202

Method 1 (Command line):

1) ssh pi@<ip_address>
	in my case, ssh pi@10.42.0.202

Method 2 (Graphical):
1)Install VNC Viewer(on laptop) and VNC Server(On raspberry Pi 3)

Refer this link for complete step-by-step installation : 
https://www.raspberrypi.org/documentation/remote-access/vnc/

2)Enter the ip address obtained above .

3)Enter the login credentials to view the raspberry pi graphical interface 

Further scope : Use of Prediction Algorithms in Smart Homes
http://www.ijmlc.org/papers/405-LC120.pdf





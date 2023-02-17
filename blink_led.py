import time 
import RPi.GPIO as GPIO

# Pin definitions 

led_pin = 12


#Suppress warnings 
GPIO.setwarnings(False)

#Use "GPIO pin numbering
GPIO.setmode(GPIO.BCM)

# Set LET pin as output
GPIO.setup(led_pin, GPIO.OUT)

# Blink forever 
sec = 0
count = 1
while True:
	sec += 1
	GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on 
	time.sleep(count)					 # Deley for 1 second 
	GPIO.output(led_pin, GPIO.LOW)   # Turn LED off 
	time.sleep(count) 
	
	print(sec)
	
	if (sec == 4):
		count = 4
	elif(sec > 4):
		count = 1
		sec = 0
	
	
	
	
	
	
	
	
	

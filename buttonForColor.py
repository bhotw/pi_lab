import time
import RPi.GPIO as GPIO

# Pin deifinitions
# buttons
btn_blue = 4
btn_yell = 5
btn_genn = 6
btn_redd = 12


# LEDS
led_redd = 18
led_genn = 19
led_yell = 20
led_blue = 21

GPIO.setwarnings(False)

# Set up pins
GPIO.setmode(GPIO.BCM)

# Buttons
GPIO.setup(btn_blue, GPIO.IN)
GPIO.setup(btn_genn, GPIO.IN)
GPIO.setup(btn_yell, GPIO.IN)
GPIO.setup(btn_redd, GPIO.IN)

# Leds
GPIO.setup(led_redd, GPIO.OUT)
GPIO.setup(led_genn, GPIO.OUT)
GPIO.setup(led_yell, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)
try:
	while True:
		if(GPIO.input(btn_genn)):
			GPIO.output(led_genn, GPIO.LOW)
		else:
			GPIO.output(led_genn, GPIO.HIGH)
			print("Green")

		if(GPIO.input(btn_redd)):
			GPIO.output(led_redd, GPIO.LOW)
		else:
			GPIO.output(led_redd, GPIO.HIGH)
			print("Red")

		if(GPIO.input(btn_yell)):
			GPIO.output(led_yell, GPIO.LOW)
		else:
			GPIO.output(led_yell, GPIO.HIGH)
			print("Yellow")

		if(GPIO.input(btn_blue)):
			GPIO.output(led_blue, GPIO.LOW)
		else:
			GPIO.output(led_blue, GPIO.HIGH)
			print("Blue")



finally:
	GPIO.cleanup()

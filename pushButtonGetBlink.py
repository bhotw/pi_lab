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

# Remember the current and previous button states
current_state = True
prev_state = True

# Function for blinking the lights for seconds

def blink_light(sec):
    count = 0
    while (count < sec):
        GPIO.output(led_redd, GPIO.HIGH)  # Turn LED on
        time.sleep(0.5)					 # Deley for 1 second
        GPIO.output(led_redd, GPIO.LOW)   # Turn LED off

        time.sleep(0.5)

        GPIO.output(led_genn, GPIO.HIGH)  # Turn LED on
        time.sleep(0.5)					 # Deley for 1 second
        GPIO.output(led_genn, GPIO.LOW)   # Turn LED off

        time.sleep(0.5)
        count += 1

# blink with a loop. this function will blink starting from the color of the button that was pressed 

def blink(start):

    leds = [led_redd, led_genn, led_yell, led_blue]

    for i in range(4):
        GPIO.output(leds[start], GPIO.HIGH)
        time.sleep(.05)
        GPIO.output(leds[start], GPIO.LOW)
        if start == 4:
            start = 1
        else:
            start += 1


# this is to know what button was pressed. 
button = 0
# if button is pushed, light up LED

try:
    while True:

		if(GPIO.input(btn_blue)):
			button = 0

        elif(GPIO.input(btn_yell)):
			button = 1
		
        elif(GPIO.input(btn_genn)):
			button = 2

        elif(GPIO.input(btn_redd)):
			button = 3
		
        blink(button)


# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()

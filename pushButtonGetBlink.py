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


# if button is pushed, light up LED

try:
    while True:
        current_state = GPIO.input(btn_blue or btn_yell or btn_genn or btn_redd)
        if (current_state == False) and (prev_state == True):
            blink_light(4)
            print("Lights Blinking")

        prev_state = current_state


# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()

import time
import RPi.GPIO as GPIO
from pygame import mixer

# Pin deifinitions
btn_pin = 4
led_pin = 12

GPIO.setwarnings(False)

# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

# Initialize pygame mixer
mixer.init()

# Remember the current and previous button states
current_state = True
prev_state = True

# Load the sounds
sound = mixer.Sound('applause-1.wav')

# Function for blinking the lights for seconds 

def blink_light(sec):
    count = 0
    while (count < sec):
        GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on 
        time.sleep(0.5)					 # Deley for 1 second 
        GPIO.output(led_pin, GPIO.LOW)   # Turn LED off 
        time.sleep(0.5) 
        count += 1
    

# if button is pushed, light up LED

try:
    while True:
        current_state = GPIO.input(btn_pin)
        if (current_state == False) and (prev_state == True):
            sound.play()
            blink_light(7)
            
            print("Sound Playing")
            print("Lights Blinking")

        prev_state = current_state
       

# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()

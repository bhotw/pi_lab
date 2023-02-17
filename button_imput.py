import time
import RPi.GPIO as gpio


# Pins deifinitions
btn1_pin = 4
led_pin = 12

gpio.setwarnings(False)

# Set up pins
gpio.setmode(gpio.BCM)
gpio.setup(btn1_pin, gpio.IN)
gpio.setup(led_pin, gpio.OUT)



# If button is pushed, light up LED
x = 0
try:
    while True:
        if gpio.input(btn1_pin):
            print ("button pressed",btn1_pin)
            x = 0
        else:
            x = 1
        if x == 0:
            gpio.output(led_pin, gpio.LOW)
        else:
            gpio.output(led_pin, gpio.HIGH)

finally:
    gpio.cleanup()

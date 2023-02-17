import time 
import RPi.GPIO as gpio

# Pin definition
led_pin = 12

#Suppress warnings 
gpio.setwarnings(False)

# Use "GPIO numbring 
gpio.setmode(gpio.BCM)

# Set led pin as output 
gpio.setup(led_pin, gpio.OUT)

# Initialize pwm object with 50 Hz and 0% duty cycle 
pwm = gpio.PWM(led_pin, 50)
pwm.start(0)


# Set PWM duty cycle to 50%, wait, then to 90%
pwm.ChangeDutyCycle(50)
time.sleep(2)
pwm.ChangeDutyCycle(90)
time.sleep(2)

# Stop, clean, and exit

pwm.stop()
gpio.cleanup()

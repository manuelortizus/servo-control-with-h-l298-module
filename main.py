from microbit import *
import utime

servo_pin = pin0 #Select pin GPIO available

#Funtion for move servo to specific position
def move_servo(position)
    duty = int((position / 180) * 1023) #convert the angle to PWM value
    servo_pin.write_analog(duty)
    ultime.sleep_ms(500) #Wait a enought time for the servo move
    servo_pin.write_digital(0) #Stop the PWM signal

while True:
    move_servo(0) #Move the servo to 0 grades
    ultime.sleep(1) #Wait 1 second
    move_servo(90) #Move the servo to 90 grades
    ultime.sleep(1) #Wait 1 second
    
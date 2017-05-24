# http://rpitips.com/python-libraries-pigpio/
import time
import pigpio 
 
PWM_PIN = 25
SERVO_PIN = 24

#connect to pigpiod daemon
pi = pigpio.pi()
 
# setup pin as an output
pi.set_mode(PWM_PIN, pigpio.OUTPUT)
pi.set_mode(SERVO_PIN, pigpio.OUTPUT)
 
for x in xrange(1,3):
	# enable LED
	# for x in xrange(0,255):

	# 	pi.set_PWM_dutycycle(PWM_PIN, x)
	# 	# wait 1 second
	# 	time.sleep(.05) 

	# for x in xrange(255,0):
	# 	# disable LED
	# 	pi.set_PWM_dutycycle(PWM_PIN, x)
	# 	time.sleep(.05)
	pi.set_PWM_dutycycle(PWM_PIN, 0)
	# 500-2500 only
	#666 = 10degrees, 
	pi.set_servo_pulsewidth(SERVO_PIN, 700)
	time.sleep(1)
	pi.set_servo_pulsewidth(SERVO_PIN, 2350)
	time.sleep(1)

#cleanup
pi.set_mode(PWM_PIN, pigpio.INPUT)
pi.set_mode(PWM_PIN, pigpio.INPUT)
#disconnect
pi.stop()
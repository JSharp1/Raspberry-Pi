# picar is allways looking for a client connection 
# i.e. car control
# PC, recieves images from picam -server
#     send movement commands to 'ardino server' 
# to another script that sends serial data to arduino

#sudo pigpiod
# ls /dev/tty*
import sys
import pigpio
import time


#connect to pigpiod daemon
pi = pigpio.pi()
h1 = pi.serial_open("/dev/ttyACM1", 115200)

def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;


while (1):
	nb = raw_input('input: ')
	if nb == "close":
		print 'client close connection'
		break
	print 'data recieved'
	print nb
	d1, d2  = nb.split(",", 1 )
	print "d1 "+d1
	print "d2 "+d2
	data = "s"+d1+","+d2
	pi.serial_write(h1, data)
	# servo = int(d1)
	# motor = int(d2)
	print data
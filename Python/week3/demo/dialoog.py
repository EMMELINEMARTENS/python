from sense_hat import SenseHat
import sys

sense = SenseHat()
# joystick tegen houden op raspberry pie
sense.set_imu_config(False,False,False)

# kleuren bepalen
def main():
# 1
	sense.set_pixel(7,7,225,0,0)
# meerdere (X,y, rgb waarden)
	while True:
	sense.set_pixel(0,0,0,255,0)
	sense.set_pixel(1,1,0,225,0)
	sense.set_pixel(2,2,0,225,0)
	sense.set_pixel(3,3,0,225,0)
	sense.set_pixel(4,4,0,225,0)
	sense.set_pixel(5,5,0,225,0)
try:
	main()
except (KeyboardInterupt, SystemExit) : 
		print('Programma sluiten')

# opkuisen matrix
finally: 
	print('Opkuisen van de Matrix')
	sense.clear()
	sys.exit()
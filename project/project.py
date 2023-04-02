import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)

while True:
	val1 = GPIO.input(3)
	val2 = GPIO.input(2)
	print(val1+val2)
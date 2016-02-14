#!/usr/bin/env python

# Thanks to http://www.youtube.com/watch?v=Dc16mKFA7Fo

#website of the project: http://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/

def movestepper(steps):
  import time
  import RPi.GPIO as GPIO

  GPIO.setmode(GPIO.BOARD)

  ControlPin = [7,11,13,15]

  for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, 0)


  seq = [ [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1],
          [1,0,0,1] ]

  for i in range(steps):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(ControlPin[pin], seq[halfstep][pin])
      time.sleep(0.001)
  #GPIO.cleanup()

  #"""
  time.sleep(2)

  for i in range(steps):
    for halfstep in reversed(range(8)):
      for pin in range(4):
        GPIO.output(ControlPin[pin], seq[halfstep][pin])
      time.sleep(0.001)

  GPIO.cleanup()
#"""

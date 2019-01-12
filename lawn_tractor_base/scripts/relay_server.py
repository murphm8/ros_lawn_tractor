#!/usr/bin/env python

from lawn_tractor_base.srv import *
import rospy
import time
import RPi.GPIO as GPIO

#TODO:  Add status check service call for all pins
#  relayState = GPIO.input(msg.channel)
#  print("Relay Status is: %s" % (relayState))
# 
#  Problem with PIN check.  the service returns true when there isn't a pin

GPIO.setmode(GPIO.BCM)

#  Initilize setting all pins to 'low'
pins = [2, 3, 4, 17, 27, 22, 10, 9]
for p in pins:
  GPIO.setup(p, GPIO.OUT)
  GPIO.output(p, GPIO.HIGH)


def callback_relay(msg):
  if (msg.channel in pins):
    if (msg.state == 1):
      GPIO.output(msg.channel, GPIO.LOW)
    else:
      GPIO.output(msg.channel, GPIO.HIGH)

    response = relayCmdResponse()
    response.success = True
    return response

  else:
    rospy.loginfo("No GPIO pin number found")
    response = relayCmdResponse()
    response.success = False
    return response

def relay_server():
  rospy.init_node("relay_server")
  s = rospy.Service("relay_cmd", relayCmd, callback_relay)
  print("Ready to recieve relay cmd")

  rospy.on_shutdown(shutdown)
  rospy.spin()

def shutdown():
  rospy.loginfo("Shutting down cleaning up GPIO")
  GPIO.cleanup()


if __name__ == "__main__":
  relay_server()


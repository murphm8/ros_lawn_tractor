#!/usr/bin/python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import std_msgs.msg
from lawn_tractor.srv import *


mode = False


def on_joy_data(data):
    global mode

    """
    :type data: Joy
    """
    if data.buttons[1]: # B button on xbox 360 controller
        mode = not mode

    if not mode:
        # rospy.loginfo("not mode")
        msg = Twist()
        msg.linear.x = data.axes[1]
        msg.angular.z = data.axes[0]
        pub.publish(msg)


    if data.buttons[1]:
        service_relay_client_object.channel = 27
        service_relay_client_object.state = 0
        result = set_relay("Kill Engine", service_relay_client_object)


    if ((data.buttons[6]) and (data.buttons[9])):
       rospy.loginfo("Start engine")
       service_relay_client_object.channel = 17
       service_relay_client_object.state = 1
       result = set_relay("starter power", service_relay_client_object)
    

    if data.buttons[8]:
       rospy.loginfo("Turn off Starter")
       service_relay_client_object.channel = 17
       service_relay_client_object.state = 0
       result = set_relay("Turn starter off", service_relay_client_object)


def set_relay(who, data):
    result = service_relay_client(service_relay_client_object)
    rospy.loginfo(who + str(result))


rospy.init_node("joystick_button_control")
rospy.wait_for_service("/relay_cmd")
service_relay_client = rospy.ServiceProxy("/relay_cmd", relayCmd)
service_relay_client_object = relayCmdRequest()
sub = rospy.Subscriber("joy", Joy, on_joy_data)
pub = rospy.Publisher("cmd_vel_mux/teleop", Twist, queue_size=1)
rospy.spin()

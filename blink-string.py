#!/usr/bin/env python

# ros libraries
import rospy
from std_msgs.msg import String

# import keyboard controls
import pygame
from sys import exit

def keyboard_input():

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:   # window close button
            return "q"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:     # pressing s for stop
                return "s"
            elif event.key == pygame.K_b:   # pressing b for blink
                return "b" 
            elif event.key == pygame.K_q:   # pressing q
                 return "q"

def blink_command(my_command, my_pub, my_rate):
    rospy.loginfo(my_command)
    my_pub.publish(my_command)
    my_rate.sleep()
    return command  # added a return value for quiting

if __name__ == '__main__':
    try:

        # 1. create window for keyboard control
        pygame.init()
        window = pygame.display.set_mode((300,300))
        pygame.display.set_caption("Control")

        # 2. create a topic
        pub = rospy.Publisher('blink', String, queue_size=10)
        
        # 3. initialize a node and specify that it is a subscriber node
        rospy.init_node('blink', anonymous=True)
        rate = rospy.Rate(10) # 10hz

        # 4. loop for 
        while not rospy.is_shutdown():
            command = keyboard_input()
            if command == "q":
                break
            elif command == "s" or command == "b":
                blink_command(command,pub,rate)
            
    except rospy.ROSInterruptException:
        pass

    finally:
        exit

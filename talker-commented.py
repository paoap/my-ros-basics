#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy                            # ros library for publishing and subscribing
from std_msgs.msg import String         # ros library for string type of msgs

def talker(): # procedure for the main function
    # creates a chatter topic, that can hold 10 strings at a time
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # initialize a talker node
    rospy.init_node('talker', anonymous=True)
    
    # rate at which this node will publish or check msgs in the container
    rate = rospy.Rate(10) # 10hz

    # loop the node
    while not rospy.is_shutdown():

        # creates the msg
        hello_str = "hello world %s" % rospy.get_time()
        
        # prints hello_str to console, debug, and node log
        rospy.loginfo(hello_str)
        # writes hello_str to chatter topic
        pub.publish(hello_str)

        # wait for a period of time depending on the set rospy.rate
        rate.sleep()

# standard coding style to guard unnecessary execution of functions
# variable __name__ is a special variable that is first ready by the python interpreter
if __name__ == '__main__':
    try:


        # calls the talker function
        talker()


    except rospy.ROSInterruptException:
        
        # when interrupted such a
        #  pressing ctrl+C
        pass

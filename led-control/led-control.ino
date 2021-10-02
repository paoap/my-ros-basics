/*
 * copyright (c) 2021 Paolo Rommel Sanchez 
 * Note: only use numeric variable in serial communication
  */


#include <ros.h>                // ROS serial communication library
#include <std_msgs/Int32.h>    // ros string type msg

ros::NodeHandle nh;            // initialize the serial node

// fetches string type messages and passed it on led_status
void toggle_blink(const std_msgs::Int32& led_status){
  if (led_status.data == 1)
    digitalWrite(LED_BUILTIN, HIGH);   // LED ON
  else if (led_status.data == 0)
    digitalWrite(LED_BUILTIN, LOW);   // LED OFF
}

// subscribe to blink, name the subscription as led, and calls the procedure toggle_blink
ros::Subscriber<std_msgs::Int32> led("/blink", &toggle_blink);    


void setup()
{ 
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(led);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}

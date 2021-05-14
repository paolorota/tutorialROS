#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Header
from sensor_msgs.msg import CompressedImage



class ImageReader:
    def __init__(self, params):
        self.subscribing_topic = params['subscribing_topic']

        self.image_input_subscriber = rospy.Subscriber(self.subscribing_topic,
                                                      CompressedImage, 
                                                      self._callback,  
                                                      queue_size = 1)

    def _callback(self, ros_data):
        np_arr = np.frombuffer(ros_data.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        filename = f"/tmp/file{ros_data.header.stamp}.jpg"
        cv2.imwrite(filename, image_np)
        rospy.loginfo(f"saving file: {filename} of shape {image_np.shape}")


if __name__ == '__main__':
    params = dict()
    params['subscribing_topic'] = '/head_front_camera/image_raw/compressed'
    rospy.init_node('image_subscriber', anonymous=True)
    ir = ImageReader(params)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down ROS face detector module")

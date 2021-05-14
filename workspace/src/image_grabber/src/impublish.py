#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Header
from sensor_msgs.msg import CompressedImage



class ImageGrabber:
    def __init__(self, params):
        self.publishing_topic = params['publishing_topic']
        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

        self.publisher = rospy.Publisher(self.publishing_topic, CompressedImage, queue_size=1)
        self.cap = cv2.VideoCapture(0)
        self.frame_count = 0

    def publish(self):
        ret, frame = self.cap.read()
        rospy.loginfo(frame.shape)
        result, encimg = cv2.imencode('.jpg', frame, self.encode_param)

        msg = CompressedImage()
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(encimg).tostring()
        self.publisher.publish(msg)

if __name__ == '__main__':
    try:
        params = dict()
        params['publishing_topic'] = '/head_front_camera/image_raw/compressed'
        params['camera_index'] = 0

        ig = ImageGrabber(params)
        rospy.init_node('image_grabber', anonymous=True)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            ig.publish()
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
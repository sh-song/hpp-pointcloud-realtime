import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import sys
import signal

class PCParser:

    #set scale factor
    BYTE_TO_POINT = 1 / 48 #48 bytes for one point

    def __init__(self):

        #init ros
        rospy.init_node('pc_parser', anonymous=False)
        rospy.Subscriber("/ouster/points", PointCloud2, self.lidar_cb)

        #init memory
        self.pc_array = np.zeros((131072, 4))
        self.pc_array_buffer = np.zeros((131072, 4))

    def lidar_cb(self, msg):
        """
        len(msg.data) == 6291456
        BYTES_TO_POINT == 1 / 48
        6291456 bytes / 48 = 131072 points
        131072 points = 128(height) * 1024(width)
        """
        length = len(msg.data) * self.BYTE_TO_POINT #131072
        point_list = [None] * int(length)

        for i, p in enumerate(pc2.read_points(msg)):
            point_list[i] = p[:4]

        self.pc_array_buffer = np.array(point_list)

    def run(self):
        self.pc_array = self.pc_array_buffer
        return self.pc_array

if __name__ == "__main__":

    #force stop 
    def force_exit(_, __):
        print('\nCtrl+C -> exit')
        sys.exit(0)
    signal.signal(signal.SIGINT, force_exit)

    #main
    parser = Parser()
    rate = rospy.Rate(10) #10 hz
    while True:
        test_pc_array = parser.run()
        print(test_pc_array[-1, :])
        rate.sleep()

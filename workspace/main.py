from pc_parser import PCParser
import sys
import signal
import rospy

if __name__ == "__main__":

    #force stop 
    def force_exit(_, __):
        print('\nCtrl+C -> exit')
        sys.exit(0)
    signal.signal(signal.SIGINT, force_exit)

    #main
    pc_parser = PCParser() #set subthread
    rate = rospy.Rate(10) #10 hz
    while True:
        pc_array = pc_parser.run()
        #----YOUR CODE HERE-----#


        print(f"\ntype: {type(pc_array)}")
        print(f"shape: {pc_array.shape}")
        print(f"last point: {pc_array[-1, :]}")


        #-----------------------#
        rate.sleep()

import rospy
from aerial_robot_base.msg import FourAxisPid
from sensor_msgs.msg import JointState
import sys

zero_time = float(sys.argv[1])

def callback1(msg):
    pass
    print('{0} {1} {2} {3} {4}'.format(msg.header.stamp.to_sec() - zero_time, msg.pitch.pos_err_no_transform, msg.roll.pos_err_no_transform, msg.throttle.pos_err_no_transform, msg.yaw.pos_err_no_transform))

def callback2(msg):
    pass
    #print('{0} {1} {2} {3} {4} {5} {6} {7}'.format(msg.header.stamp.to_sec() - 1499437745.907266, msg.position[0], msg.position[1],msg.position[2],msg.position[3],msg.position[4],msg.position[5],msg.position[6]))
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/controller/debug", FourAxisPid, callback1)
    rospy.Subscriber("/hydrusx/joint_states", JointState, callback2)
    rospy.spin()

if __name__ == '__main__':
    listener()

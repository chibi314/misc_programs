import rospy
from aerial_robot_base.msg import FourAxisPid

def callback(msg):
    print('{0} {1} {2} {3}'.format(msg.pitch.pos_err_no_transform, msg.roll.pos_err_no_transform, msg.throttle.pos_err_no_transform, msg.yaw.pos_err_no_transform))

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/controller/debug", FourAxisPid, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

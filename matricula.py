import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

rospy.init_node('matricula')
#rospy.init_node('somador')
soma_string = String()

def subCallBack(msg):
    global soma_string
    soma_string = msg

def timerCallBack(event):
    msg = String()
    msg.data = '2017003772'
    pub.publish(msg)
    
    print('soma da matricula: '+soma_string.data)
    

sub = rospy.Subscriber('/somador/sum', String, subCallBack)
pub = rospy.Publisher('matricula/mat', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)

rospy.spin()

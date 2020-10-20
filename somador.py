import rospy
#from std_msgs.msg import Int32
from std_msgs.msg import String

#rospy.init_node('matricula')
rospy.init_node('somador')
mat_string = String()

def subCallBack(msg):
    global mat_string
    mat_string = msg
    #print(mat_string.data)

def timerCallBack(event):
    soma = 0
    for i in range(len(mat_string.data)):
        soma=soma+int(mat_string.data[i])
    print('somando matricula . . . ('+mat_string.data + ')')
    
    msg_soma = String()
    msg_soma.data = str(soma)
    pub.publish(msg_soma)

sub = rospy.Subscriber('/matricula/mat', String, subCallBack)
pub = rospy.Publisher('somador/sum', String, queue_size=1)

timer = rospy.Timer(rospy.Duration(1), timerCallBack)

rospy.spin()

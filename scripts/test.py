#!/usr/bin/env python

import math
import time
TCP_position = (0,1)
import rospy


def test():
    global TCP_position
    cal=list(TCP_position)
    cal=(2,2)
    print TCP_position


def read():
    # with open('/home/lizq/win7share/NDI.txt','r') as f:
    #     print (f.read())
    f=open('/home/lizq/win7share/NDI.txt','r',10)
    flag=1
    print (f.read())
    time.sleep(1)
    print (f.read())

def quat2angle(quat):
    q1=2*(quat[3]*quat[4]+ quat[6]*quat[5])
    q2=quat[6]**2 + quat[3]**2 - quat[4]**2 - quat[5]**2
    q3=-2*(quat[3]*quat[5]- quat[6]*quat[4])
    q4=2*(quat[4]*quat[5]+ quat[6]*quat[3])
    q5=quat[6]**2 - quat[3]**2 - quat[4]**2 + quat[5]**2
    return (quat[0],quat[1],quat[2],math.atan2(q1,q2),math.asin(q3),math.atan2(q4,q5))

if __name__ == '__main__':
    # test()
    read()
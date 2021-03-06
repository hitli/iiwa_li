#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import math


def quat2matrix((dx, dy, dz, x, y, z, w)):
    #输入tuple
    matrix = np.zeros((4,4))
    # 规范化处理，保证模为1
    for n in [w, x, y, z]:
        n = n/math.sqrt(x*x+y*y+z*z+w*w)
    matrix[0] = [2*(w*w+x*x)-1 , 2*(x*y-w*z) , 2*(x*z+w*y) , dx]
    matrix[1] = [2*(x*y+w*z) , 2*(w*w+y*y)-1 , 2*(y*z-w*x) , dy]
    matrix[2] = [2*(x*z-w*y) , 2*(y*z+w*x) , 2*(w*w+z*z)-1 , dz]
    matrix[3] = [0,0,0,1]
    return matrix


def matrix2quat(matrix):
    #输入numpy矩阵
    for i in (0,1,2,3):
        for j in (0,1,2,3):
            matrix[i][j]=round(matrix[i][j],5)
    mw=1+matrix[0][0]+matrix[1][1]+matrix[2][2]
    mx=1+matrix[0][0]-matrix[1][1]-matrix[2][2]
    my=1-matrix[0][0]+matrix[1][1]-matrix[2][2]
    mz=1-matrix[0][0]-matrix[1][1]+matrix[2][2]
    if abs(mw)<1e-8:
        mw=0
        print ('mw归零')
    if abs(mx)<1e-8:
        mx=0
        print ('mx归零')
    if abs(my)<1e-8:
        my=0
        print ('my归零')
    if abs(mz)<1e-8:
        mz=0
        print ('mw归零')

    w = 0.5*math.sqrt(mw)
    x = 0.5*math.sqrt(mx)
    y = 0.5*math.sqrt(my)
    z = 0.5*math.sqrt(mz)

    #规范化处理，保证模为1
    for n in [w, x, y, z]:
        n /= math.sqrt(x*x+y*y+z*z+w*w)
    if matrix[2][1]-matrix[1][2] < 0:
        x = -x
    if matrix[0][2]-matrix[2][0] < 0:
        y = -y
    if matrix[1][0]-matrix[0][1] < 0:
        z = -z
    #返回tuple
    return matrix[0][3], matrix[1][3], matrix[2][3], x, y, z, w


def turn_TCP_axs_rad_len(position,axs,rad,len):
    if axs=='rx':
        Tmat=quat2matrix((0,0,0,math.sin(rad/2.0),0,0,math.cos(rad/2.0)))
    elif axs=='ry':
        Tmat=quat2matrix((0,0,0,0,math.sin(rad/2.0),0,math.cos(rad/2.0)))
    elif axs=='rz':
        Tmat=quat2matrix((0,0,0,0,0,math.sin(rad/2.0),math.cos(rad/2.0)))
    elif axs=='dx':
        Tmat=quat2matrix((len,0,0,0,0,0,1))
    elif axs == 'dy':
        Tmat = quat2matrix((0, len, 0, 0, 0, 0, 1))
    elif axs == 'dz':
        Tmat = quat2matrix((0, 0, len, 0, 0, 0, 1))
    else:
        print ('输入轴错误')
    # print 'Tmat',Tmat
    # print 'quat2matrix(position)',quat2matrix(position)
    # print 'quat2matrix(position)*Tmat',np.dot(quat2matrix(position),Tmat)
    return matrix2quat(np.dot(quat2matrix(position),Tmat))


def quat2angle(quat):#没用
    q1=2*(quat[3]*quat[4]+ quat[6]*quat[5])
    q2=quat[6]**2 + quat[3]**2 - quat[4]**2 - quat[5]**2
    q3=-2*(quat[3]*quat[5]- quat[6]*quat[4])
    q4=2*(quat[4]*quat[5]+ quat[6]*quat[3])
    q5=quat[6]**2 - quat[3]**2 - quat[4]**2 + quat[5]**2
    return (quat[0],quat[1],quat[2],math.atan2(q1,q2),math.asin(q3),math.atan2(q4,q5))


if __name__ == '__main__':
    print (quat2matrix((1,2,3,1,0,0,0)))
    # print matrix2quat(quat2matrix((1,2,3,1,0,0,0)))
    # print(turn_TCP_axs_rad((1, 2, 3, 1, 0, 0, 0), 'rx', 0))
    # eng=matlab.engine.start_matlab()
    # eng.MinTwoSolveTJM(nargout=0)
    # q=[1,0,1,0]
    # print eng.quat2angle(q,nargout=3)
    # print quat2angle((0,0,0,0,0,0,1))
    # print ','.join(str(i) for i in quat2angle((0.0,0,0,0,0,0,1)))
    print quat2matrix((0.3196184910824411, -0.24608946005373455, 0.9227790288091682, -0.16047115123781783, 0.06647591727366217, -0.37690016065474524, 0.9098221063613892))
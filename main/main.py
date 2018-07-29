# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:00:00 2018

@author: WZW&SYQ
"""

import sys
import time
from DLibAttack import DLibAttack

if __name__ == "__main__":
    print("1.Data Attack              2.detection")
    order = int(input('Welcome to use Dlib,please choose the operation:'))

    if order == 1:
        print ("You have choose the Data Attack:),please choose the attack way")
        attack = int(input())
        s = time.time()
        if attack == 1:
            print ('1')
        elif attack == 2:
            print ('2')
        else:
            print ('Error num!')
            exit(-1)
        dla = DlibAttack(attack)
        print (dla.user)
    elif order == 2:
        print ("You have choose the Data Attack:),please choose the algorithm way")
        algorithm = int(input())
        s = time.time()
        if algorithm == 1:
            print ('1')
        elif algorithm == 2:
            print ('2')
        else:
            print ('Error num!')
            exit(-1)
    else:
        print ('Error num!')
        exit(-1)
    e = time.time()
    print ("Run time: %f s" % (e - s))
    

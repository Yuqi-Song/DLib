# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:00:00 2018

@author: WZW&SYQ
"""

import sys
from os.path import abspath


import time

sys.path.append('../')
from baseclass.shillingAttack.Attack import Attack
if __name__ == "__main__":
    print ('Welcome to use Dlib!')
    print ("1.RandomAttack")
    print ("You have choose the Data Attack:),please choose the attack way:")
    attack = int(input())
    s = time.time()
    if attack == 1:
        dla = Attack('../config/RA_config.conf')
    elif attack == 2:
        print ('2')
    else:
        print ('Error num!')
        exit(-1)
    e = time.time()
    print ("Run time: %f s" % (e - s))
    

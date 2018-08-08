# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:00:00 2018

@author: WZW&SYQ
"""

import sys
from os.path import abspath

import random
import time

sys.path.append('../')
from baseclass.shillingAttack.Attack import Attack
from algorithm.shillingAttack.randomAttack import RandomAttack
from algorithm.shillingAttack.bandwagonAttack import BandWagonAttack
from algorithm.shillingAttack.averageAttack import AverageAttack
if __name__ == "__main__":
    print ('Welcome to use Dlib!')
    print ("1.RandomAttack   2.AverageAttack   3.BandwagonAttack")
    print ("You have choose the Data Attack:),please choose the attack way:")
    attack = int(input())
    s = time.time()
    if attack == 1:
        RandomAttack('../config/attack_config.conf')
    elif attack == 2:
        AverageAttack('../config/attack_config.conf')
    elif attack == 3:
        BandWagonAttack('../config/attack_config.conf')
    else:
        print ('Error num!')
        exit(-1)
    e = time.time()
    print ("Run time: %f s" % (e - s))
    

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:22:57 2018

@author: WZW
"""
from DAO import DAO

class RateDao(DAO):
    def __init__(self):
        super().__init__()
        print ("RateDao 初始化")

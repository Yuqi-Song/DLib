# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:22:57 2018

@author: WZW
"""
from DAO import DAO

class SocialDao(DAO):
    def __init__(self):
        super().__init__()
        print ("SocialDao 初始化")

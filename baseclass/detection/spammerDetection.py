# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:23:32 2018

@author: WZW
"""

from Detection import Detection

class SpammerDetection(Detection):
    def __init__(self):
        super().__init__()
        print ("SpammerDetection 初始化")

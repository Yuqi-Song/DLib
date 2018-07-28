# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:22:57 2018

@author: WZW
"""

from Measure import Measure

class NormMeasure(Measure):
    def __init__(self):
        super().__init__()
        print ("NormMeasure 初始化")
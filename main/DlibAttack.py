# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:45:09 2018

@author: WZW
"""


from DLib import Dlib

class DlibAttack(Dlib):
    def __init__(self,attack):
        super().__init__()
        
        print ("DlibAttack 初始化")
        print ("attack is:",attack)
        
        
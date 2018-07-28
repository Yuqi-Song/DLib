# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:22:57 2018

@author: WZW
"""

from DAO import DAO

class CommentDao(DAO):
    def __init__(self):
        super().__init__()
        print ("CommentDao 初始化")
#!/usr/bin/python

import uiautomator2 as u2
from threading import Timer

#import pototo_speak
#import douyin_lite
#import article_lite
import pototo_book
#import wukun

def talk(name):
    a.enter_app()

d = u2.connect('1e506aa60405') 
#d = u2.connect('c746dd057d28') 
s = pototo_book.TomatoBook(d)
#a = douyin_lite.douyin_lite(d)
s.enter_app()

#timer = Timer(3, talk, args=("lily",))
#timer.start()


#!/usr/bin/python

import uiautomator2 as u2
import time

d = u2.connect('1e506aa60405') 

# 头条极速版
def article_lite(): 
    d.app_stop('com.ss.android.article.lite') # 关闭app
    d.app_start('com.ss.android.article.lite','com.ss.android.article.lite.activity.SplashActivity')  # 打开app
    time.sleep(2)
    d.xpath('//*[@resource-id="com.ss.android.article.lite:id/ate"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]').click() # 打开小视频界面
    time.sleep(2)
    d.click(0.027, 0.291) # 点击进入第一个播放
    while 1:
        time.sleep(2)
        d.swipe(0.5, 0.7, 0.5, 0.3) # 下滑屏幕
    d.app_stop('com.ss.android.article.lite') # 关闭app

def al_video():
    while 1:
        time.sleep(4)
        d.swipe(0.5, 0.7, 0.5, 0.3) # 下滑屏幕	

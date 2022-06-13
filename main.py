#!/usr/bin/python

import uiautomator2 as u2
import json
import time
import pototo_speak
import douyin_lite
import article_lite

d = u2.connect('1e506aa60405') 
#print(d.info)

# 番茄免费小说
def dragon_read():
    d.app_stop('com.dragon.read') 
    d.app_start('com.dragon.read')
    time.sleep(2)
    d(resourceId="com.dragon.read:id/bk9").click() # 点击福利界面
    if d.xpath('//*[@resource-id="com.dragon.read:id/bd0"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[26]').info['text'] == '开宝箱得金币':
        d.xpath('//*[@resource-id="com.dragon.read:id/bd0"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[26]').click() # 点击开宝箱
        time.sleep(1)
        d.click(0.371, 0.592)

        dragon_read_ads_interface()                           
    else:
        d.swipe(0.5, 0.7, 0.5, 0.3) # 下滑屏幕
        if d.xpath('//*[@resource-id="com.dragon.read:id/bd0"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.FlattenUIText[43]').info['text'] == '立即领取':
            d.xpath('//*[@resource-id="com.dragon.read:id/bd0"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.FlattenUIText[43]').click() 
            d(resourceId="com.dragon.read:id/cr0").click()
            time.sleep(15)
            if d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[17]').info['text'] == '领取成功':
                d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[17]').click()

    dragon_read_ads()
    #d(className='com.lynx.tasm.behavior.ui.text.UIText')[2].click() # 再看一个广告

# 看广告
def dragon_read_ads():
    d.swipe(0.5, 0.7, 0.5, 0.1)
    if d(text="立即观看") is None:
        return False
    else:
        d(text="立即观看").click()
        dragon_read_ads_interface()
        d.swipe(0.5, 0.1, 0.5, 0.7)
        return True

# 广告界面
def dragon_read_ads_interface():
	time.sleep(15)
	while d(text="领取成功") is None:
	    time.sleep(2)

	#if d(text="领取成功").info['bounds']['top'] != 67:
	#    time.sleep(2)            

	if d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.UIText[3]').info['text'].startswith('再看一个'):
	    d.click(0.57, 0.125)
	else:
	    d(text="领取成功").click()
	return True

def dragon_read_book():
    d.click(0.685, 0.95)	
    d.click(0.195, 0.254)
    while 1:
        time.sleep(5)
        d.swipe(0.7, 0.5, 0.3, 0.5) # 左滑屏幕

###
#        if d(text="看视频领金币") is None:
 #           d.swipe(0.7, 0.5, 0.3, 0.5) # 左滑屏幕
 #       else:
 #           d(text="看视频领金币").click()
  #          time.sleep(26)
  #          d.click(0.911, 0.04)
  #          time.sleep(1)
  #          d.swipe(0.7, 0.5, 0.3, 0.5) # 左滑屏幕
###        	

dragon_read_book()
#douyin_lite.douyin_lite_video()

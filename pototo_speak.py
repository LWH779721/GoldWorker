#!/usr/bin/python

import uiautomator2 as u2
import time

d = u2.connect('1e506aa60405') 

def pototo_speak():
	d.app_stop('com.xs.fm') 
	d.app_start('com.xs.fm')
	time.sleep(4)
	d.click(0.475, 0.924) # 点击播放
	d.click(0.08, 0.061) # 退回主界面
	d.click(0.701, 0.95) # 领现金界面
	d(text='立即领取').click()
	d.click(0.425, 0.574)

def ps_ads():
	while True:
		d(text='立即观看').click()
		time.sleep(17)
		d.click(0.923, 0.049)

#!/usr/bin/python

import uiautomator2 as u2
import json
import time

d = u2.connect('1e506aa60405')

class wukun:
    def open_app(self):
        d.app_stop('com.cat.readall') 
        d.app_start('com.cat.readall', '.activity.BrowserMainActivity')

    def enter_my_gold_page(self):
        d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout[3]').click()
    
    def collect_peaches(self):
        while d(text="收桃子领金币", clickable="true").exists():
            d(text="收桃子领金币", clickable="true").click()
            time.sleep(1)  
            d.press("back")
    # 播放广告界面
    def ads_page(self):
        e = d(textContains='s') 
        if d(textContains='s后可领取奖励').exists():
            e = d(textContains='s后可领取奖励')

        if e.wait_gone(timeout=100.0):
            time.sleep(1)
            d.swipe(0.0, 0.5, 0.7, 0.5) # 左滑屏幕 退出
            time.sleep(1)
            if d(textStartsWith='再看一个', clickable='true').exists():
                d(textStartsWith='再看一个', clickable='true').click()
                self.ads_page()
            elif d(textStartsWith='继续观看', clickable='true').exists():
                d(textStartsWith='继续观看', clickable='true').click()
                self.ads_page()        
    # 开宝箱
    def open_gold_box(self):
        if d(text="开宝箱得金币").exists:
            d(text="开宝箱得金币").click() # 点击开宝箱
            time.sleep(1)
            if d(textStartsWith='再看一条', clickable="true").exists:
                d(textStartsWith='再看一条', clickable="true").click()
                self.ads_page() 
    # 领金币
    def get_coin(self):
        e = d(className='com.lynx.tasm.behavior.ui.view.UIView', textContains='/')[0].info['text'].split('/')
        if float(int(e[0])/int(e[1])) > 0.8:
            d(text="领取金币").click()
            time.sleep(1)
            if d(textStartsWith='看视频再领', clickable="true").exists:
                d(textStartsWith='看视频再领', clickable="true").click()
                self.ads_page() 
    # 看广告
    def look_ads(self):
        if d(text="去完成", className="com.lynx.tasm.behavior.ui.LynxFlattenUI", clickable="true").click():
            self.ads_page() 

    def get_time(self):
        e = d(textMatches="[0-9]+分[0-9]+秒").info['text']
        while d(textMatches="[0-9]+分[0-9]+秒").info['text'] == "":
            time.sleep(1)
        print(e)

    # 看小说
    def read_book():
        while 1:
            d.press("volume_down")
            time.sleep(2)
    # 进入app 
    def enter_app(self):
        self.open_app()
        self.enter_my_gold_page()
        self.collect_peaches()
        #self.get_coin()
        #self.open_gold_box()
        #self.look_ads()

s = wukun()
s.enter_app() 	

#!/usr/bin/python

import uiautomator2 as u2
import json
import time

# 
class UC:
    d = 0
    def __init__(self, d):
        self.d = d

    def open_app(self):
        if self.d.app_current()['package'] != "com.ucmobile.lite":
            self.d.app_stop('com.ucmobile.lite') 
            self.d.app_start('com.ucmobile.lite')
            self.d.wait_activity("com.UCMobile.main.UCMobile", timeout=100)

    # 进入任务界面
    def enter_task_page(self):  
        self.d(resourceId="com.ucmobile.lite:id/of", className="android.widget.FrameLayout").click() 

    # 开宝箱 webview 无法获取UI元素
    def open_gold_box(self):
        time.sleep(1)
        self.d.click(0.821, 0.875)
        time.sleep(1)
        self.d.click(0.852, 0.331)

    # 播放广告界面
    def ads_page(self):
        if not d.wait_activity("com.ss.android.excitingvideo.ExcitingVideoActivity", timeout=10):
            print("activity not show")
            return

        if not self.d(textContains='s').wait(timeout=20):
            print("s not show")
            return

        e = self.d(textContains='s') 
        if e.exists():
            if self.d(textContains='s后可领取奖励').exists():
                e = self.d(textContains='s后可领取奖励')
        elif self.d(textContains='跳过').exists():
            e = self.d(textContains='跳过')

        if e.wait_gone(timeout=100.0):
            time.sleep(1)
            self.d.swipe(0.0, 0.5, 0.7, 0.5) # 左滑屏幕 退出
            time.sleep(1)
            if self.d(textStartsWith='再看一个', clickable='true').exists():
                self.d(textStartsWith='再看一个', clickable='true').click()
                self.ads_page()
            elif self.d(textStartsWith='继续观看', clickable='true').exists():
                self.d(textStartsWith='继续观看', clickable='true').click()
                self.ads_page()

    # 读小说
    def read_book(self):
        time.sleep(1)
        self.d.click(0.459, 0.808)
        start = time.time()
        while round(time.time() - start, 0) < 600:
            if self.d(text="完成任务领番茄会员").exists():
                d(text="不再提示").click()
                time.sleep(0.5)
                d(text="放弃").click()
            elif self.d(text='看视频领金币').exists():
                self.d(text='看视频领金币').click()
                self.ads_page()
            else:
                self.d.press("volume_down")
                time.sleep(2)
        d.press("back") 

    # 循环获取金币
    def get_coin_from_book(self):
        self.d(text='看视频领金币').click()
        self.ads_page()
        self.d.press("volume_down")
        self.d.press("volume_down")

    # 看广告
    def look_ads(self):
        if self.d(text="看广告赚金币").exists():
            if self.d(text="看广告赚金币").right(text="立即观看", className="com.lynx.tasm.behavior.ui.LynxFlattenUI") != None:
                self.d(text="看广告赚金币").right(text="立即观看", className="com.lynx.tasm.behavior.ui.LynxFlattenUI").click()
                self.ads_page()

    # 领阅读金币
    def get_reading_coin(self):
        self.d.swipe(0.5, 0.7, 0.5, 0.1) # 下滑屏幕
        while self.d(text='立即领取', clickable="true", className="com.lynx.tasm.behavior.ui.LynxFlattenUI").exists:
            self.d(text='立即领取', clickable="true", className="com.lynx.tasm.behavior.ui.LynxFlattenUI").click() 
            time.sleep(1)
            if self.d(textStartsWith='看视频最高再领', clickable="true").exists:
                self.d(textStartsWith='看视频最高再领', clickable="true").click()
                self.ads_page()
                time.sleep(1) 
    # 进入app 
    def enter_app(self):
        self.open_app()
        self.enter_task_page()
        self.open_gold_box()
        #self.look_ads()
        #self.get_reading_coin()
        #self.enter_book()
        #self.read_book() 
    
    def main(self):
        self.open_app()
        while True:
            self.enter_task_page()
            self.open_gold_box()
            self.look_ads()
            self.get_reading_coin()
            self.enter_book()
            self.read_book() 

d = u2.connect('1e506aa60405') 
s = UC(d)

s.enter_app()
'''
while True:
    try:
        s.open_app()
        s.enter_app()
    except Exception: 
        print("exception")
'''
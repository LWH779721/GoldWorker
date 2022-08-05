#!/usr/bin/python

import uiautomator2 as u2
import json
import time

# 番茄免费小说
class TomatoBook:
    d = 0
    def __init__(self, d):
        self.d = d

    def open_app(self):
        if self.d.app_current()['package'] != "com.dragon.read":
            self.d.app_stop('com.dragon.read') 
            self.d.app_start('com.dragon.read')
            self.d.wait_activity(".pages.main.MainFragmentActivity", timeout=100)

    # 进入福利界面
    def enter_fuli_page(self):  
        self.d(className="android.widget.RadioGroup").child(className="android.widget.RadioButton")[2].click() # 点击福利界面

    # 进入小说
    def enter_book(self):
        self.d(className="android.widget.RadioGroup").child(className="android.widget.RadioButton")[3].click()  # 点击书架
        time.sleep(0.5)
        self.d(className="androidx.recyclerview.widget.RecyclerView").child(className="android.view.ViewGroup")[0].click()  # 点击第一本书

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

    # 开宝箱
    def open_gold_box(self):
        if self.d(text="开宝箱得金币").exists:
            self.d(text="开宝箱得金币").click() # 点击开宝箱
            time.sleep(1)
            if self.d(textStartsWith='看视频最高再领', clickable="true").exists:
                self.d(textStartsWith='看视频最高再领', clickable="true").click()
                self.ads_page()  
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
        self.enter_fuli_page()
        self.open_gold_box()
        self.look_ads()
        self.get_reading_coin()
        self.enter_book()
        self.read_book() 
    
    def main(self):
        self.open_app()
        while True:
            self.enter_fuli_page()
            self.open_gold_box()
            self.look_ads()
            self.get_reading_coin()
            self.enter_book()
            self.read_book() 

d = u2.connect('1e506aa60405') 
s = TomatoBook(d)

s.main()
'''
while True:
    try:
        s.open_app()
        s.enter_app()
    except Exception: 
        print("exception")
'''
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
        self.d.app_stop('com.dragon.read') 
        self.d.app_start('com.dragon.read')
        self.d.wait_activity(".pages.main.MainFragmentActivity", timeout=100)

    # 进入福利界面
    def enter_fuli_page(self):  
        self.d(resourceId="com.dragon.read:id/bsp").click() # 点击福利界面

    # 进入小说
    def enter_book(self):
        self.d(resourceId="com.dragon.read:id/n7").click()  # 点击书架
        time.sleep(1)
        self.d.xpath('//*[@resource-id="com.dragon.read:id/bsp"]\
            /android.view.ViewGroup[1]\
            /android.widget.FrameLayout[1]\
            /android.widget.FrameLayout[1]\
            /android.view.View[1]').click()  # 点击第一本书
        time.sleep(1)

    # 播放广告界面
    def ads_page(self):
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
        self.d.click(0.459, 0.808)
        start = time.time()
        while round(time.time() - start, 0) < 600:
            self.d.press("volume_down")
            #time.sleep(1)
            if self.d(text='看视频领金币').exists():
                self.d(text='看视频领金币').click()
                self.ads_page()
            else:
                time.sleep(2)

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
        self.d.swipe(0.5, 0.7, 0.5, 0.1)
        while self.d(text="去观看", clickable="true").exists:
            self.d(text="去观看", clickable="true").click()
            time.sleep(1)
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
        self.enter_fuli_page()
        self.open_gold_box()
        self.look_ads()
        self.get_reading_coin()
        self.enter_book()
        self.read_book() 


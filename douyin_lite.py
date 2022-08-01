#!/usr/bin/python

import uiautomator2 as u2
import time
from threading import Timer

# 抖音极速版
class douyin_lite:
    d = 0
    def __init__(self):
        self.d = u2.connect('1e506aa60405') 

    def open_app(self):
        self.d.app_stop('com.ss.android.ugc.aweme.lite') 
        self.d.app_start("com.ss.android.ugc.aweme.lite")

    def enter_fuli(self):
        self.d(resourceId="com.ss.android.ugc.aweme.lite:id/fmn").click()

    # 广告界面
    def ads_page(self):
        print("1")
        e = self.d(textContains='s') 
        if e.exists():
            if self.d(textContains='s后可领取奖励').exists():
                e = self.d(textContains='s后可领取奖励')
                print("2")
        elif self.d(textContains='跳过').exists():
            e = self.d(textContains='跳过')
        
        if e.wait_gone(timeout=100.0):
            #time.sleep(1)
            print("3")
            while True:
                #self.d.press("back")
                self.d.swipe(0.0, 0.5, 0.7, 0.5) # 左滑屏幕 退出
                #time.sleep(0.2)
                print("4")
                if self.d.app_current()['activity'] == "com.ss.android.ugc.aweme.main.MainActivity":
                    print("5")
                    break
                elif self.d(textStartsWith='继续观看').exists():
                    self.d(textStartsWith='继续观看').click()
                    print("6")
                    self.ads_page()
                    break
                elif self.d(textStartsWith='领取奖励').exists():
                    self.d(textStartsWith='领取奖励').click()
                    print("7")
                    self.ads_page()
                    break

    def select_like(self):
        d(resourceId="com.ss.android.ugc.aweme.lite:id/qb").click() # 点红心
        d(resourceId="com.ss.android.ugc.aweme.lite:id/byy").click() # 点评论
        d(resourceId="com.ss.android.ugc.aweme.lite:id/cg=")[0].click() # 评论第一个点红心
        d(resourceId="com.ss.android.ugc.aweme.lite:id/back_btn").click() # 关闭评论

    # 刷视频
    def look_video(self):
        count = 0
        while count < 10:
            count = count + 1
            self.select_like()
            time.sleep(5)
            self.d.swipe(0.5, 0.7, 0.5, 0.3)  

    # 开宝箱
    def open_gold_box(self):
        if self.d(text="开宝箱得金币").exists():
            self.d(text="开宝箱得金币").click() # 点击开宝箱
            if self.d(textStartsWith='看广告视频再').exists(timeout=3):
                self.d(textStartsWith='看广告视频再').click()
                self.ads_page() 

    # 看广告
    def look_ads(self):
        if self.d(text="去领取").exists():
            self.d(text="去领取").click() # 点击开宝箱
            self.ads_page()             

    def main(self):
        #self.open_app()
        #while True:
        #    self.look_video()
        #self.enter_fuli()
            #time.sleep(0.5)
        self.open_gold_box()
        self.look_ads()

s = douyin_lite()
s.main()

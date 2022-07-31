#!/usr/bin/python

import uiautomator2 as u2
import time

d = u2.connect('1e506aa60405') 

class article_lite:
    def open_app(self):
        d.app_stop('com.ss.android.article.lite') # 关闭app
        d.app_start('com.ss.android.article.lite','com.ss.android.article.lite.activity.SplashActivity')  # 打开app

    def video_page(self):
        d.xpath('//*[@resource-id="com.ss.android.article.lite:id/ate"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]').click() # 打开小视频界面

    def look_video(self): 
        d.click(0.027, 0.291) # 点击进入第一个播放
        while 1:
            time.sleep(2)
            d.swipe(0.5, 0.7, 0.5, 0.3) # 下滑屏幕

    # 广告界面
    def ads_page(self):
        if not d.wait_activity("com.ss.android.excitingvideo.ExcitingVideoActivity", timeout=10):
            print("activity not show")
            return

        d(textContains='s').wait(10.0)
        e = d(textContains='s') 
        if d(textContains='s后可领取奖励').exists():
            e = d(textContains='s后可领取奖励')

        if e.wait_gone(timeout=100.0):
            d.press("back")
            time.sleep(0.5)
            if d(textStartsWith='再看一个', clickable='true').exists():
                d(textStartsWith='再看一个', clickable='true').click()
                self.ads_page()
            elif d(textStartsWith='继续观看', clickable='true').exists():
                d(textStartsWith='继续观看', clickable='true').click()
                self.ads_page()
        else:
            print("3")

    def pick_up_coin(self):
        d(text="领金币").click()
        if d(textStartsWith="看视频再领").click_exists(timeout=3.0):
            self.ads_page()    

    def return_to_main_page(self):
        while d.app_current()['activity'] != ".activity.SplashActivity":
            d.press("back") 
            time.sleep(0.5) 

    # 看视频
    def look_video(self):
        while 1:
            d.swipe(0.5, 0.7, 0.5, 0.3) # 下滑屏幕
            if d(text="领金币").exists():
                self.pick_up_coin()
            elif d(resourceId="com.ss.android.article.lite:id/b1i").exists() and d(resourceId="com.ss.android.article.lite:id/b1i").info['text'] == '开宝箱': # 开宝箱
                d(resourceId="com.ss.android.article.lite:id/b1i").click()
                if d(text="开宝箱得金币").click_exists(timeout=10.0):
                    if d(textStartsWith="看完视频再领").click_exists(timeout=3.0):
                        self.ads_page()
                time.sleep(1)        
                d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout[1]').click()        
            else:
                time.sleep(2)

    # 查找宝箱
    def find_box(self):
        while 1:
            self.return_to_main_page() 
            d.swipe(0.5, 0.7, 0.5, 0.3) # 下滑屏幕
            if d(text="领金币").exists():
                self.pick_up_coin()
            elif d(resourceId="com.ss.android.article.lite:id/b1i", text="开宝箱").exists(): # 开宝箱
                d(resourceId="com.ss.android.article.lite:id/b1i").click()
                d(text="开宝箱得金币").wait(10.0)
                if d(text="开宝箱得金币", className="com.lynx.tasm.behavior.ui.text.UIText").click():
                    d(text="看视频领", className="com.lynx.tasm.behavior.ui.text.FlattenUIText").wait(10.0)
                    d(text="看视频领", className="com.lynx.tasm.behavior.ui.text.FlattenUIText").click()
                    self.ads_page()
                elif d(text="看视频领", className="com.lynx.tasm.behavior.ui.text.FlattenUIText").exists():
                    d(text="看视频领", className="com.lynx.tasm.behavior.ui.text.FlattenUIText").click()
                    self.ads_page()
                else:
                    print("开宝箱得金币 click failed")
                d(resourceId='android:id/tabs').child(className="android.widget.RelativeLayout")[0].click()        
            else:
                a = d(className="androidx.recyclerview.widget.RecyclerView").child(resourceId="com.ss.android.article.lite:id/b_")
                for e in a:
                    self.return_to_main_page() 
                    e.click()
                    count = 0
                    while count < 10:
                        # 获取每次滑动前页面下半部分的所有元素
                        page_content = d.dump_hierarchy()[(len(d.dump_hierarchy()) // 2):]
                        if d(text="领金币").exists():
                            self.pick_up_coin()
                        elif d(text="天降惊喜二选一").exists():
                            if d(text="天降惊喜二选一").down(className="android.widget.Image") == None:
                                d.swipe(0.5, 0.6, 0.5, 0.5)                             
                            d(text="天降惊喜二选一").down(className="android.widget.Image").click()
                            if d(textStartsWith="看视频再领").click_exists(timeout=3.0):
                                #time.sleep(1)
                                self.ads_page()  
                                break
                        elif d(description="加关注").exists():
                            if d(text="点击领取200金币").exists():
                                d(text="点击领取200金币").click()
                                d(textStartsWith="看视频再领").click_exists(timeout=3.0)
                                self.ads_page()
                            break
                        elif d(text="加入书架", resourceId="com.ss.android.article.lite:id/dn").exists():
                            break    

                        d.swipe(0.5, 0.7, 0.5, 0.3)
                        time.sleep(0.5)
                        count = count + 1
                        # 获取每次滑动后页面下半部分的所有元素，并与上一次滑动前的页面元素对比，页面元素没有变化时跳出循环
                        new_page_content = d.dump_hierarchy()[(len(d.dump_hierarchy()) // 2):]
                        if new_page_content == page_content:
                            break


s = article_lite()
while True:
    try:
        s.open_app()
        s.find_box()
    except Exception: 
        print("exception")
        #time.sleep(1) 




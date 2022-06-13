#!/usr/bin/python

import uiautomator2 as u2
import time

d = u2.connect('1e506aa60405') 

# 抖音极速版
def douyin_lite():
    #d.click(0.591, 0.921)

    #d(text="开宝箱").click()

    #d.xpath('//*[@resource-id="com.ss.android.ugc.aweme.lite:id/a5k"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[2]').click()

    # 开宝箱剩余时间
    next_time = d.xpath('//*[@resource-id="com.ss.android.ugc.aweme.lite:id/a5k"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.FlattenUIText[31]').info['text']
    print ("data2['text']: ", next_time)
    if next_time == '开宝箱得金币':
        d.click(0.811, 0.892) # 点击开宝箱
        d.click(0.49, 0.597)  # 点击看广告
        # sleep
        d.click(0.889, 0.046) # 点击关闭
        d(text="领取奖励").click()

# 刷视频
def douyin_lite_video():
	#d.click(0.685, 0.95)	
	#d.click(0.195, 0.254)
	while 1:
        	time.sleep(5)
        	d.swipe(0.5, 0.7, 0.5, 0.3) # 下滑屏幕

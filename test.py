import uiautomator2 as u2
import json
import time

d = u2.connect('1e506aa60405') 
#print(d.info)

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

        if d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.UIText[3]').info['text'].startswith('再看一个'):
            d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.UIText[3]').click()
            if d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[17]').info['text'] == '领取成功':
                d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[17]').click()                              
    else:
        d.swipe(0.5, 0.7, 0.5, 0.3) # 下滑屏幕
        if d.xpath('//*[@resource-id="com.dragon.read:id/bd0"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.FlattenUIText[43]').info['text'] == '立即领取':
            d.xpath('//*[@resource-id="com.dragon.read:id/bd0"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.FlattenUIText[43]').click() 
            d(resourceId="com.dragon.read:id/cr0").click()
            time.sleep(15)
            if d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[17]').info['text'] == '领取成功':
                d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.view.UIView[17]').click()


    d(className='com.lynx.tasm.behavior.ui.text.UIText')[2].click() # 再看一个广告

# 看广告
def dragon_read_ads():
    d.swipe(0.5, 0.7, 0.5, 0.1)
    if d.xpath('//*[@resource-id="com.dragon.read:id/bd0"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.FlattenUIText[27]').info['text'] == '立即观看':
        d.xpath('//*[@resource-id="com.dragon.read:id/bd0"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.FlattenUIText[27]').click()
        while d(text="领取成功") is None or d(text="领取成功").info['bounds']['top'] > 80:
            time.sleep(2)
        if d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.UIText[3]').info['text'].startswith('再看一个'):
            d.xpath('//*[@resource-id="com.dragon.read:id/aep"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.UIText[3]').click()
        else:
            d(text="领取成功").click()
        d.swipe(0.5, 0.1, 0.5, 0.7)
        return true
    else:
        return false

article_lite()

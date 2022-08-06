#!/usr/bin/python

import uiautomator2 as u2
import time

d = u2.connect('1e506aa60405') 

class TomatoSpeak:
	def open_app(self):
		if self.d.app_current()['package'] != "com.xs.fm":
			d.app_stop('com.xs.fm') 
			d.app_start('com.xs.fm')

	def enter_coin_page(self):
		d(className="android.widget.RadioGroup").child(className="android.widget.RadioButton", text="领现金").click()

	def open_box(self):
		d(text="开宝箱得金币").click()
		
	def look_ads(self):
		d(text='立即观看').click()

	def main(self):
		pause

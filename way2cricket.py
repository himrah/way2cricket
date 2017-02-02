import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *
from time import sleep
from bs4 import BeautifulSoup as BS

class Cricket():
	def __init__(self):
		self.username='username'
		self.passwd='password'
		self.url ='http://site24.way2sms.com/Login1.action?'
		self.data = 'username='+self.username+'&password='+self.passwd+'&Submit=Sign+in'


	def login(self):
		cj= cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		self.opener.addheaders=[('User-Agent',"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0")]
		usock = self.opener.open(self.url, self.data)
		self.session_id =str(cj).split('~')[1].split(' ')[0]
		self.opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+self.session_id)]

	def sms(self,msg):
		print('sending msg')
		send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
		send_sms_data = 'ssaction=ss&Token='+self.session_id+'&mobile='+'8287870355'+'&message='+msg+'&msgLen=136'
		sms_sent_page = self.opener.open(send_sms_url,send_sms_data)
		print('sent!')

	def score(self):
		while True:
			url = "http://www.cricbuzz.com/live-cricket-scores/16878/ind-vs-eng-3rd-t20i-england-tour-of-india-2016-17"
			s=urllib2.urlopen(url)
			soup=BS(str(s.read()),'html.parser')
			data = soup.find("span","cb-font-20 text-bold")
			score='Score is : '+data.text
			self.sms(score)
			print('Sleep for 60 Seconds')
			sleep(60)
if __name__=='__main__':
	c=Cricket()
	c.login()
	c.score()﻿

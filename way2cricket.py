import requests
from bs4 import BeautifulSoup as BS

class Cricket():
	def __init__(self):
		self.username = 'username'
		self.password = 'password'
		self.url = 'http://site24.way2sms.com/Login1.action?'
		self.data = {'username':self.username,'password':self.password}
		self.message = 'hi there'
		self.mobile = 'receiver_mobile_number'


	def login(self):
		self.session =requests.Session()
		self.session.headers.update({"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"})
		self.session.post(self.url,self.data)
		self.session_id = str(self.session.cookies).split('~')[1].split(' ')[0]
		self.session.headers.update({'Referer':'http://site25.way2sms.com/sendSMS?Token='+self.session_id})

	def sms(self,msg):
		print('sending msg')
		sms_url = 'http://site24.way2sms.com/smstoss.action?'
		sms_data = {'Token':self.session_id,'message':msg,'mobile':self.mobile,'msgLen':125}
		print(self.session_id)
		print(sms_url)
		print(sms_data)
		self.session.post(sms_url,sms_data)
		print(self.message)
		print('sent!')

	def score(self):
		while True:
			url = "http://www.cricbuzz.com/live-cricket-scores/16878/ind-vs-eng-3rd-t20i-england-tour-of-india-2016-17"
			s = urllib2.urlopen(url)
			soup = BS(str(s.read()),'html.parser')
			data = soup.find("span","cb-font-20 text-bold")
			score = 'Score is : '+data.text
			self.sms(score)
			print('Sleep for 120 Seconds')
			sleep(120)
if __name__=='__main__':
	c=Cricket()
	c.login()
	c.score()

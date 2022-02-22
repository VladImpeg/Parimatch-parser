from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# from seleniumwire
import pickle

import json
import re
import requests
from bs4 import BeautifulSoup as BS
import base64


import os
import sys
sys.path.insert(0,'..')
from time import gmtime, strftime, sleep
import time
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "live_streaming.settings")

import django
django.setup()

# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process

from ffmpeg import FFmpeg
# import asyncio
# from multiprocessing import Pool
import urllib3
# import urllib.request
# import urllib.parse as urlparse
# from urllib.parse import parse_qs

import subprocess
import threading
import operator

import sqlite3
from live_streaming.core.models import Premach
#LET THE CHAOS BEGIN...


options = webdriver.ChromeOptions()


#options.add_argument('--user-data-dir=/opt/google/chrome/User Data/Default') R.I.P,you pice of code....

# options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--disable-web-security')
user_agent = '''User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'''
options.add_argument('--no-sandbox')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-infobars')
options.add_argument('--enable-file-cookies')
options.add_argument('user-agent={0}'.format(user_agent))

driver = webdriver.Chrome(options=options, executable_path=r'/var/www/API/parsing/chromedriver')
cookies = pickle.load(open("cookies.pkl", "rb"))
driver.get('https://en.parimatch.com/en/')


cookie_dict1={
	    'name':"PARISESSID",
	    'value':"fptvfn77mdjoh2vrhnhgbpsj06",
	    "domain": ".parimatch.com",  # google chrome
	    "expires": "Fri, 24 Jan 2081 00:18:52 GMT",
	    'path': '/',
	    'httpOnly': True,
	    'HostOnly': False,
	    'Secure': True}
cookie_dict2={
		'name':"LID",
		'value':"5f2e51072a3579.75993830",
		"domain": ".parimatch.com",
		"expires": "Tue, 06 Aug 2030 07:15:19 GMT",
		'path': '/',
		'httpOnly': False,
		'HostOnly': False,
		'Secure': False}
cookie_dict3={
        'name':"cfidsgib-w-parimatch",
        'value':"DbTT5jCmoKHm81TO7HAe/2K52MTn/qjdc7PhGI9I15QFROaAEAXwIW5AxlYj7o8sk4hrg+1pHKzaulc5UhXSNX1kAR5ZA195jWGaFvLDS+pZ1XPxoVk/18OCwn483Pn8KsTmIUmU044clrGhtO+1u9ZpuSEMFyP09GkcGA==",
        "domain": ".parimatch.com",  # google chrome
        "expires": "Thu, 12 Aug 2021 14:02:43 GMT",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False}
cookie_dict4={
        'name':"cfidsgib-w-parimatch",
        'value':"MKtvgZWBn3dGKMrK2oBeEvqJ9N9VjPF/XODYxPgIlOH/aKR143EPjbJyU9G/EhgEweqmdogoDni3oJk5mxnobHm76xLGQQRNbEoh8cGFbfWqYeYDwyTh6tlEuGl/rIOlzajKk6oiKPLbLcQyj74V4zJUSk5W+P6yg4OQKw==",
        "domain": ".parimatch.com",  # google chrome
        "expires": "Thu, 12 Aug 2021 14:01:50 GMT",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': True}
cookie_dict5={
        'name':"datadome",
        'value':"VUARzJY9XLkue-fkfD9rzLwK.s.KGrEWNBc8-nyA0kDqgLlOh6oGz7FhjJUEeOUCF-lI3XFjaUzlgqSXEYBLqtjHax9nHj4IYbcG9WBfz_",
        "domain": ".parimatch.com",  # google chrome
        "expires": "Sat, 28 Aug 2021 11:20:21 GMT",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False}
cookie_dict6={
        'name':"RID",
        'value':"0010906C-72C9-4D3C-B7BA-7DB482C1E128",
        "domain": ".parimatch.com",  # google chrome
        "expires": "Sat, 01 Aug 2020 16:16:20 GMT",
        'path': '/',
        'httpOnly': True,
        'HostOnly': False,
        'Secure': True}
cookie_dict7={
        'name':"airToken",
        'value':"4501fcd8-7c62-454d-93c3-d49edbb8d7a3",
        "domain": ".parimatch.com",  # google chrome
        "expires": "Sat, 07 Nov 2020 23:02:33 GMT",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False}
cookie_dict8={
        'name':"__cfduid",
        'value':"dcf8e819db08411018f08b146540964991604779328",
        "domain": ".parimatch.com",  # google chrome
        "expires": "Mon, 07 Dec 2020 20:02:08 GMT",
        'path': '/',
        'httpOnly': True,
        'HostOnly': False,
        'Secure': False}
cookie_dict9={
        'name':"DC",
        'value':"35137A84-8E73-42BC-8DD9-D19AC10C619B",
        "domain": ".parimatch.com",  # google chrome
        "expires": "Mon, 07 Sep 2020 07:15:19 GMT",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False}
cookie_dict10={
        'name':"dt",
        'value':"034cb745cdc97027c94f7ceb869861b8",
        "domain": ".parimatch.com",  # google chrome
        "expires": "Tue, 08 Sep 2020 11:19:00 GMT",
        'path': '/',
        'httpOnly': True,
        'HostOnly': False,
        'Secure': True}
driver.add_cookie(cookie_dict1)
driver.add_cookie(cookie_dict2)
driver.add_cookie(cookie_dict3)
driver.add_cookie(cookie_dict4)
driver.add_cookie(cookie_dict5)
driver.add_cookie(cookie_dict6)
driver.add_cookie(cookie_dict7)
driver.add_cookie(cookie_dict8)
driver.add_cookie(cookie_dict9)
driver.add_cookie(cookie_dict10)


#NOTHING INTERESTING AROUND

global titles_n_subtitles_new
global titles_n_subtitles_old
global match_data
titles_n_subtitles_old = []
titles_n_subtitles_new = []
match_data = []
global new_lap
new_lap = True
# GET READY
# 3...
global has_link
has_link = False
# ...2....
global titles_n_subtitles
titles_n_subtitles = []
# ...1
global v_url
v_url = ''







# # infinity loop machine v 2.0


def wrapper(func, args):
	func(*args)

def bro(id, url):
	isDir = os.path.isdir("/var/www/html/hls/" + id)
	if isDir == True:
 		subprocess.Popen('ffmpeg -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 9 -i ' + 'https://mediadata.live/hls/' + id + "/" + id + '.m3u8 ' + '-c:v copy -hls_flags delete_segments /var/www/html/hls/' + id + "/" + id + 'bro' + '.m3u8', shell=True, stdout=subprocess.PIPE).stdout.read()
	else:
#  		os.makedirs("/var/www/html/hls/" + id)
		while True:
			http = urllib3.PoolManager()
			http.request('GET', "https://mediadata.live/main/bro_prism.php?id=" + id)
			isDir = os.path.isdir("/var/www/html/hls/" + id)
			if isDir == True:
			   last_updated = time.ctime(os.path.getmtime("/var/www/html/hls/" + id))
			   datetime_object = datetime.strptime(last_updated, '%a %b %d %H:%M:%S %Y')
			   mod_time = datetime_object.strftime("%m/%d/%Y %H:%M")
			   curr_time = strftime("%m/%d/%Y %H:%M", gmtime())
			   sleep(45)
			   if mod_time != curr_time:
			   	sleep(30)
			   	last_updated = time.ctime(os.path.getmtime("/var/www/html/hls/" + id))
			   	datetime_object = datetime.strptime(last_updated, '%a %b %d %H:%M:%S %Y')
			   	mod_time = datetime_object.strftime("%m/%d/%Y %H:%M")
			   	curr_time = strftime("%m/%d/%Y %H:%M", gmtime())
			   	if mod_time != curr_time:
			   		subprocess.Popen('ffmpeg -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 9 -i "' + 'https:' + url.replace("13","12") + '" -c:v copy -hls_flags delete_segments /var/www/html/hls/' + id + "/" + id + 'bro' + '.m3u8', shell=True, stdout=subprocess.PIPE).stdout.read()
			   else:
			   	print('its okay now')
			else:
			   try:
			   	os.makedirs("/var/www/html/hls/" + id)
			   	subprocess.Popen('ffmpeg -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 9 -i "' + 'https:' + url.replace("13","12")  + '" -c:v copy -c:a copy -hls_flags delete_segments /var/www/html/hls/' + id + '/' + id + 'bro' + '.m3u8', shell=True, stdout=subprocess.PIPE).stdout.read()
			   except Exception:
			   	print('mach has finished')


def dice(id):
	isDir = os.path.isdir("/var/www/html/hls/" + id)
	if isDir == True:
 		print('dir exists')
	else:
		while True:
			http = urllib3.PoolManager()
			http.request('GET', "https://mediadata.live/main/dice_prism.php?id=" + id)
			sleep(2)
def modification_date(filename):
	t = os.path.getmtime(filename)
	return datetime.datetime.fromtimestamp(t)

def akamized(id, url):
	isDir = os.path.isdir("/var/www/html/hls/" + id)
	if isDir == True:
		last_updated = time.ctime(os.path.getmtime("/var/www/html/hls/" + id))
		datetime_object = datetime.strptime(last_updated, '%a %b %d %H:%M:%S %Y')
		mod_time = datetime_object.strftime("%m/%d/%Y %H:%M")
		curr_time = strftime("%m/%d/%Y %H:%M", gmtime())
		sleep(45)
		if mod_time != curr_time:
			sleep(30)
			last_updated = time.ctime(os.path.getmtime("/var/www/html/hls/" + id))
			datetime_object = datetime.strptime(last_updated, '%a %b %d %H:%M:%S %Y')
			mod_time = datetime_object.strftime("%m/%d/%Y %H:%M")
			curr_time = strftime("%m/%d/%Y %H:%M", gmtime())
			if mod_time != curr_time:
				subprocess.Popen('ffmpeg -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 9 -i "' + url + '" -c:v copy -hls_flags delete_segments /var/www/html/hls/' + id + "/" + id + '.m3u8', shell=True, stdout=subprocess.PIPE).stdout.read()
		else:
			print('its okay now')
	else:
		try:
			os.makedirs("/var/www/html/hls/" + id)
			subprocess.Popen('ffmpeg -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 9 -i "' + url + '" -c:v copy -c:a copy -hls_flags delete_segments /var/www/html/hls/' + id + '/' + id + '.m3u8', shell=True, stdout=subprocess.PIPE).stdout.read()
		except Exception:
			print('mach has finished')


def sportlevel(id, url):
	isDir = os.path.isdir("/var/www/html/hls/" + id)
	if isDir == True:
		last_updated = time.ctime(os.path.getmtime("/var/www/html/hls/" + id))
		datetime_object = datetime.strptime(last_updated, '%a %b %d %H:%M:%S %Y')
		mod_time = datetime_object.strftime("%m/%d/%Y %H:%M")
		curr_time = strftime("%m/%d/%Y %H:%M", gmtime())
		sleep(45)
		if mod_time != curr_time:
			sleep(60)
			last_updated = time.ctime(os.path.getmtime("/var/www/html/hls/" + id))
			datetime_object = datetime.strptime(last_updated, '%a %b %d %H:%M:%S %Y')
			mod_time = datetime_object.strftime("%m/%d/%Y %H:%M")
			curr_time = strftime("%m/%d/%Y %H:%M", gmtime())
			if mod_time != curr_time:
				subprocess.Popen('ffmpeg -i "' + url + '" -c:v copy -c:a copy -hls_flags delete_segments /var/www/html/hls/' + id + "/" + id + '.m3u8', shell=True, stdout=subprocess.PIPE).stdout.read()
		else:
			print('its okay now')
	else:
		try:
			os.makedirs("/var/www/html/hls/" + id)
			subprocess.Popen('ffmpeg -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 9 -i "' + url + '" -c:v copy -c:a copy -hls_flags delete_segments /var/www/html/hls/' + id + '/' + id + '.m3u8', shell=True, stdout=subprocess.PIPE).stdout.read()
		except Exception:
			print('mach has finished')


def img_gaming(id):
	isDir = os.path.isdir("/var/www/html/hls/" + id)
	if isDir == True:
 		print('IMG dir exists!!!!')
	else:
		os.makedirs("/var/www/html/hls/" + id)
		while True:
			http = urllib3.PoolManager()
			http.request('GET', "https://mediadata.live/main/img_prism.php?id=" + id)
			sleep(2)
# 		subprocess.Popen('ffmpeg -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 9 -i "' + url + '" -c:v copy -c:a copy -hls_flags delete_segments /var/www/html/hls/' + id + '/' + id + '.m3u8', shell=True, stdout=subprocess.PIPE).stdout.read()

            
while True:
	sleep(8)
	driver.get('https://classic.parimatch.com/en/refresh.php?type=11')
	container = BS(driver.page_source, 'html.parser').find_all('tr')
	# bsf': 'aac_adtstoasc' , 's' : '640x480' , 'b:v' : '512k' , 'strict' : '9', 'min_seg_duration' : '1500',  -protocol_whitelist file,http,https,tcp,tls,crypto


	# this func was created by Vlad Kovryzhenko(MAY BE IN HEAVEN: https://www.youtube.com/channel/UCzbgnKH3nNF08JwdJmV2XaA/videos?view_as=subscriber)
	def parse_info():
		match_data = []
		v_url = ""
		id_array = []
		filtered_hrefs = []
		id = ""
		curr_id = 0
	# 	"In list maches loop"
		for a in container:
			try:
				json_data = []
				has_link = False
				time = a.find('td', attrs={'class':'first'}).get_text()
				curr_date = strftime("%d.%m.%y", gmtime())
				legue = a.find('div', attrs={'class':'cat'}).get_text()
				teams = a.find('a', href=True).get_text()

				hours = time[0:-3]
				minutes = time[3:]

				legue_data = legue.split('. ')
				team_data = teams.split(' - ')
				team1 = team_data[0]
				team2 = team_data[1]
				sport = legue_data[0]
				ligue = legue_data[-1]

				json_data.append({"League" : ligue})
				json_data.append({"Event_Date" : curr_date })
				json_data.append({"Event_Time" : str(int(hours) - 3) + ":" + minutes})
				json_data.append({"Sport" : sport})
				json_data.append({"Team_1" : team1})
				json_data.append({"Team_2" : team2})


				id = a.find('a', href=True)['href'][-8:]
			except Exception:
				return

	# 	first, trying to find bro...
			try:
				driver.get("https://mediadata.live/proxy.php?id=" + id)
				sleep(3)
				match_link = BS(driver.page_source, 'html.parser').find('body')
				ifurl = json.loads(match_link.text)
				vv_url = ifurl['ifurl']
				driver.get(vv_url)
				sleep(2)
				video_link = BS(driver.page_source, 'html.parser').find('body')
				json_link = video_link.prettify()
				jsArr = json_link.split()
				matchers_js = ['.m3u8']
				filtered_hrefs = [s for s in jsArr if any(xs in s for xs in matchers_js)]
				try:
					matchers_yt = ['youtube.com']
					filtered_hrefs_youtube = [s for s in jsArr if any(xs in s for xs in matchers_yt)]
					you_url = filtered_hrefs_youtube[0]
					id = id + "bro"
					json_data.append({"Provider" : "Youtube"})
					json_data.append({"Youtube_link" : you_url[5:-2].replace("\\", "")})
					has_link = True
				except:
					if 'Cyber' not in sport:
						if 'Esports' not in sport:
							if operator.contains(vv_url, "livebro.cc"):
								if len(legue_data) >= 3 and sport == "Football":
									region = legue_data[-2]
									json_data.append({"Region" : region})
								else:
									json_data.append({"Region" : "-"})
								id = id + "bro"
								matchers_bro = ['vdnsport.cc']
								filtered_hrefs_bro = [s for s in jsArr if any(xs in s for xs in matchers_bro)]
								bro_url = filtered_hrefs_bro[0]
# 								threading.Thread(target=bro, args=(id,bro_url)).start()
								sleep(6)
								json_data.append({"Provider" : "livebro.cc"})
								has_link = True
							elif operator.contains(vv_url, "imggaming.com"):
								id = id + "img"
								json_data.append({"Region" : "-"})
								json_data.append({"Provider" : "imggaming.com"})
								has_link = True
					else:
						has_link = False
						pass

			except:
				match_link = BS(driver.page_source, 'html.parser').find('body')
				uri = str(match_link.text)
				text_arr = uri.split('"')
				if operator.contains(str(match_link), "akamaized.net"):
					try:
						ak_uri = json.loads(match_link.text)
						v_url = ak_uri['uri']
						id = id + "aka"
						has_link = True
						threading.Thread(target=akamized, args=(id, v_url)).start()
						json_data.append({"Region" : "-"})
						json_data.append({"Provider" : "akamaized.net"})
					except:
						has_link = False
				elif operator.contains(uri, "sportlevel.com"):
					id = id + "slv"
					matches = [match for match in text_arr if "sportlevel.com" in match]
					v_url = matches[0]
					threading.Thread(target=sportlevel, args=(id, 'https:' + v_url.replace("\\", ""))).start()
					json_data.append({"Region" : "-"})
					json_data.append({"Provider" : "sportlevel.com"})
					has_link = True
				elif operator.contains(uri, "dice"):
					id = id + "dic"
					json_data.append({"Region" : "-"})
					json_data.append({"Provider" : "dicegaming.com"})
					has_link = True
				else:
					has_link = False
					pass
			# 		we don`t have it here....
# 			...because there is nothing
# 				all what we're doing here is bluffing

#CHORUS:

# Than we`re checking what do we have.
# Is it a problems that were carved?
# 							No bro, it was nothing here...
# 						So all of our problems has disappear?
			if has_link == False:
				pass
			else:
				try:
					curr_id = curr_id + 1
					message_bytes = id.encode('ascii')
					base64_bytes = base64.b64encode(message_bytes)
					base64_link = base64_bytes.decode('ascii')
					json_data.append({"Broadcast_link" : base64_link})
					titles_n_subtitles.append(json_data)
				except:
					pass
			
			json_data = []
			has_link = False
			v_url = ''
# PREMATCHES	
# 				try:		
# 					mach = Premach.objects.all()
# 					for pre in mach:
# 						if fuzz.ratio(pre.team1, team1) >= 44 or fuzz.ratio(pre.team1, team2) >= 44:
# 							json_data.append({"Prematch_id" : pre.event_id})
# 							break
# 						else:
# 							continue
# 				except:
# 					pass

	#
	# 		titles_n_subtitles_new.extend(titles_n_subtitles_old)
	# 		for filtered_dict in titles_n_subtitles_new:
	# 			    if filtered_dict not in match_data:
	# 			        match_data.append(filtered_dict)
	#--\\|//-->
	parse_info()
	
# 	save data and clear items array
	data = {'Match_data': titles_n_subtitles}
	data = json.dumps(data) # dict to string
	data = json.loads(data) # string to json
	if len(titles_n_subtitles) != 0:
		with open('/var/www/html/data_main.json', 'w', encoding='utf-8') as f:
			json.dump(data, f, ensure_ascii=False, indent=5)
		with open('/mnt/nfs_share/data_main.json', 'w', encoding='utf-8') as s:
			json.dump(data, s, ensure_ascii=False, indent=5)
		titles_n_subtitles = []
	os.system("python american.py")
	sleep(120)
	#---||---->
#////////////switch lap state after one lap iteration/////////...
#//////like your life after unification//////////////////////

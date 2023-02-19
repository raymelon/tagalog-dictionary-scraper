# collect_tagalog.py
#
# This script collects Tagalog words from tagalog.pinoydictionary.com,
#   a database of Tagalog words powered by Cyberspace.ph Web Hosting
#
# The collected words will be stored at a text file named "tagalog_dict.txt"
# It aims to create a dictionary of Tagalog words
#
# It works by loading and parsing each webpage, 
#   extracting the words enclosed in <dt> tag
#
# Originally this script made is for a Scrabble dictionary database,
#   but other uses may vary
#
# Script written by Raymel Francisco
# October 2016
# Modified February 2023

import string
import re
from urllib import request
from bs4 import BeautifulSoup
from requests_futures.sessions import FuturesSession
import time
from MoverException import MoverException

start_time = time.perf_counter()

# each letter has a set of webpages depending on the number of words
# this counter does the navigation on those
page_index = 1

# aids in navigating each letter's pages
letter_index = 0

# variables needed for opening each webpage
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
letters = list(string.ascii_lowercase)
headers = { 'User-Agent': user_agent, }

# worker implementation. original script took 10 min to execute.
# enhancement showed tenfold reduction in execution time
#
# reduce max_workers once network bandwidth becomes an issue
# increase max_workers to speed up scraping. 
# 	increase only if:
# 		network bandwidth can handle multiple requests at once
#			and CPU is capable of doing so.
#
# estimated sustained download rate for max_workers values and estimated script duration:
# (for 40000 words, as of 2023-02-19)
#
# max_workers=10, dl rate at 1 Mbit, 00:01:30
# max_workers=100, dl rate at 5 Mbit, 00:01:00
# max_workers=1000, dl rate at 8 Mbit, 00:00:50
#
session = FuturesSession(max_workers=1000)

worker_pool = []
last_page_number = 1
all_words = []

# page fetching
while True:

	try:

		# once the letter_index exceeds 25 (Ñ and NG excluded), the alphabet traversal is done
		if letter_index > 25:
			raise Exception('All valid URLs traversed.')

		url = 'http://tagalog.pinoydictionary.com/list/' + letters[letter_index] + '/' + str(page_index) + '/'
						
		print('Fetching from', url) # prints url for output display

		# tries opening the page
		req = session.get(url)

		if page_index == 1:
			res = req.result()

			if res.status_code == 200:
				print('Success. Response is', res.status_code)
				html = res.content

				# find the last page for the current letter
				raw = BeautifulSoup(html, 'html.parser')

				# expected raw.find()['href'] return: http://tagalog.pinoydictionary.com/list/a/88/
				# expected last_page_number: 88
				last_page_element = raw.find('a', title='Last Page')
				
				if last_page_element:
					last_page_number = int(list(filter(str.strip, last_page_element['href'].split('/')))[-1])
				else:
					last_page_number = 1

			else:
				raise MoverException('Failed. Response is', res.status_code)

		elif page_index < 1:
			raise MoverException('Failed. Invalid page_index value:', page_index)

		else:
			if page_index > last_page_number:
				raise MoverException('Last index reached for letter_index:', letter_index)


		# check response later
		worker_pool.append((url, req))

	except MoverException as me:

		print(me)

		# the trick here is when the page doesn't exist, 
		#   we need to go to the next letter page already
		letter_index += 1
					
		# new letter means new page index
		page_index = 1
		continue

	except Exception as e:

		print(e)
		break
			
	# parses the page opened
	# raw = BeautifulSoup(html, 'html.parser')
			
	#    		# each word is enclosed in <h2> tags, 
	#     	#   therefore it is the only tag we need
	# words = raw.findAll('h2', class_='word-entry')
			
	# for word in words:
	#         		# only gets words up to 8 characters length and...
	# 	if len(word.next.next) < 9:
	#             		# ...containing alphabet characters only
	# 		print(re.compile('[^a-zA-Z]').sub('', word.next.next), file=f)
			
	# go to next page index
	page_index += 1

print('Checking', len(worker_pool), 'page workers...')

for worker in worker_pool:

	try:

		(url, req) = worker

		res = req.result()

		if res.status_code == 200:
			print('Check completion of page worker for request at', url, '- Success. Response is', res.status_code, '- Extracting words...')
		else:
			raise MoverException('Check completion of page worker for request at', url, ': Failed. Response is', res.status_code)

		html = res.content

		# parses the page opened
		raw = BeautifulSoup(html, 'html.parser')
				
		# each word is enclosed in <h2> tags, 
		#   therefore it is the only tag we need
		words = raw.findAll('h2', class_='word-entry')
				
		for word in words:
			# only gets words up to 15 characters length and...
			if len(word.next.next) < 15:
				# ...containing alphabet characters only
				# print(re.compile('[^a-zA-Z]').sub('', word.next.next), file=f)
				all_words.append(re.compile('[^a-zA-Z]').sub('', word.next.next))

	except MoverException:

		print(me)
		continue

	except Exception:

		print(e)
		break


with open('tagalog_dict.txt', 'w') as f:
	# writing to file
	for word in all_words:
		print(word, file=f)


print('Writing finished. See the extracted words at "tagalog_dict.txt"')

end_time = time.perf_counter()
print('Script ended. ', time.strftime("%H:%M:%S",time.gmtime(end_time - start_time)))

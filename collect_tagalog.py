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
# Originally this is intented for a Scrabble dicitonary database,
#   but other uses may vary
#
# Script written by Raymel Francisco
# October 2016

import string
import re
from urllib import request
from bs4 import BeautifulSoup

# each letter has a set of webpages depending on the number of words
# this counter does the navigation on those
page_index = 1

# aids in navigating each letter's pages
letter_index = 0

# variables needed for opening each webpage
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
letters = list(string.ascii_lowercase)
headers = { 'User-Agent': user_agent, }

with open('tagalog_dict.txt', 'a') as f:
    
	# every iteration parses a new webpage
	while True:
		# once the letter_index reaches 27, the alphabet traversal is done and we are done as well
		try:
			url = 'http://tagalog.pinoydictionary.com/list/' + letters[letter_index] + '/' + str(page_index) + '/'
		except:
			print('EXTRACTION DONE. See the extracted words at "tagalog_dict.txt"')
			break
			      
		print('Extracting from', url) # prints url for user monitoring
        
        	# tries opening the page
		try:
			req = request.Request(url, None, headers)
			html = request.urlopen(req).read().decode('utf8')
		except:
           		# the trick here is when the page doesn't exist, 
            		#   we need to go to the next letter page already
			letter_index += 1
            
            		# new letter means new page index
			page_index = 1
			continue
        
        	# parses the page opened
		raw = BeautifulSoup(html, 'html.parser')
        
       		# each word is enclosed in <h2> tags, 
        	#   therefore it is the only tag we need
		words = raw.findAll('h2', class_='word-entry')
        
		for word in words:
            		# only gets words up to 8 characters length and...
			if len(word.next.next) < 9:
                		# ...containing alphabet characters only
				print(re.compile('[^a-zA-Z]').sub('', word.next.next), file=f)
        
        	# go to next page index
		page_index += 1

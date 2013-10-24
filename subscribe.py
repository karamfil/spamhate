import requests

from random import randrange
from time import sleep

subscribe_url = 'http://62.76.189.118/lists/?p=subscribe'
chars = 'abcdefghijklmnopqrstuvwxyz_.-0123456789'
domains = ['mail.bg', 'mail.com', 'gmail.com', 'abv.bg', 'data.bg']

chars_len = len(chars)
domains_len = len(domains)

def genranstr(length):
	string = ''
	for i in range(length):
		# print randrange(0, chars_len)
		string += chars[randrange(0, chars_len)]
	
	return string.strip('_-.').lstrip('0123456789')

while(True):
	email = genranstr(randrange(6,15)) + '@' + domains[randrange(0,domains_len)]
	
	data = {
		'VerificationCodeX'	: '',
		'email'				: email,
		'emailconfirm'		: email,
	}
	
	if randrange(0,2): data['htmlemail']		= 1
	if randrange(0,2): data['list[2]']			= 'signup'
	if randrange(0,2): data['list[3]']			= 'signup'
	if randrange(0,2): data['subscribe']		= 'Subscribe'
	
	response = requests.post(subscribe_url, data)
	
	
	print response, email
	sleep(randrange(1,30))

#!/usr/bin/python

import argparse, subprocess, re

parser = argparse.ArgumentParser(description='Upload to the real server.')
parser.add_argument('-d'		, type=str															, help='get information from domain name')
# parser.add_argument('-a'		, type=str	, nargs='?'		, default='historypin'	, const=True	, help='app name (default: historypin)')
# parser.add_argument('-p'		, type=bool	, nargs='?'		, default=False			, const=True	, help='do not pack resources')

args = parser.parse_args()
data = {}

WHOIS_KEYS = {
	'Registrant Name'			: 'name',
	'Registrant Organization'	: 'organization',
	'Registrant Address1'		: 'address',
	'Registrant Country'		: 'country',
	'Registrant Phone Number'	: 'phone',
	'Registrant Email'			: 'email',
	'Name Server'				: 'nameserver',
}



def cmd(c, print_output = True):
	output = subprocess.check_output(c, shell=True)
	if print_output: print(output)
	return output

def header(s): print('\n{0}\n----------------------------------------------------------------------------------'.format(s))


print("Checking Domain: {0.d}".format(args))

header('TRACE')
trace = cmd("traceroute {0.d}".format(args))
data['IP'] = trace.strip().split('\n')[0].strip().split()[3][1:-2]

header('WHOIS')
whois = cmd("whois {0.d} | egrep 'Registrar URL|Registrant |Name Server'".format(args))
data.update({'whois_' + WHOIS_KEYS[i[0]]: i[1].strip() for i in [w.split(':') for w in whois.strip().split('\n')] if i[0] in WHOIS_KEYS})


print data
















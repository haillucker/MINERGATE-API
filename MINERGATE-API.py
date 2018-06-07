#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import requests

# ( -- LOGO * INFO -- ) #
bugs = '''
   ____  __  __ _                  ____       _               _    ____ ___ 
  / __ \|  \/  (_)_ __   ___ _ __ / ___| __ _| |_ ___        / \  |  _ \_ _|
 / / _` | |\/| | | '_ \ / _ \ '__| |  _ / _` | __/ _ \_____ / _ \ | |_) | | 
| | (_| | |  | | | | | |  __/ |  | |_| | (_| | ||  __/_____/ ___ \|  __/| | 
 \ \__,_|_|  |_|_|_| |_|\___|_|   \____|\__,_|\__\___|    /_/   \_\_|  |___|
  \____/
\n[$] BUGS MINERGATE API SYS.
[$] URL = ('https://www.Brazzers.com/').
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

print bugs
print '[X] WELCOME TO MINERGATE API PYTHON SYSTEM.\n'

# ( - API URLS - ) #

# // $1 -> DO YOU ASK UR SELF WHERE DID I GET THOSE URLS FROM [https://github.com/MinerGate/minergate-api#].
# // $2 -> ALL THINGS FROM MINERGATE GITHUB API REQUESTS FILE.
# // $3 -> YOUR MINERGATE ACCESS TOKEN HAVE TO BE IN SCRIPT IN VAR [token].
# // $4 -> MY BEST WICHES WITH THE SCRIPT.
# // $5 -> MINERGATE API SYS [;].
balance = 'https://api.minergate.com/1.0/balance' # Balance
transfers = 'https://api.minergate.com/1.0/transfers/xmr' #Transfers
withdrawals = 'https://api.minergate.com/1.0/withdrawals/xdn' #Withdrawals
workers = 'https://api.minergate.com/1.0/workers' #Workers7
mstates = 'https://api.minergate.com/1.0/mining/stats' #Mine States
affiliate_links_all = 'https://api.minergate.com/1.0/affiliate/links' # Affiliate Links
affiliate_links_children = 'https://api.minergate.com/1.0/affiliate/childrens' # Affiliate Links Children
invoices = 'https://api.minergate.com/1.0/invoices' # Invoice
nick_name = 'https://api.minergate.com/1.0/profile/nickname' # Nick Name
block_chain_info = 'https://api.minergate.com/1.0/xmr/status' # BlockChain Info

# ( - MINERGATE TOKEN - ) #

# // HOW TO GET YOUR ACCESS TOKEN API KEY ?
# // $1 -> OPEN ANY PROGRAMME OR EXE TO GET THE BROWSER REQUESTS [HEADER/POST/URLS].
# // $2 -> DON'T YOU KNOW PROGRAMMES LIKE THIS ? HER U R => [FIDDLER / HTTP DEBUGGER / HTTP FOX / BURB SURITE].
# // $3 -> RUN THE WEB APP SUCCESSFUL + LOGIN WITH YOUR ACCOUNT ..
# // $4 -> SO YOU CAN FIND YOUR TOKEN IN THE SUCCESSFUL SRC OF THE API LOGIN REQUEST.
# // $5 -> THE TOKEN WILL BE LIKE THIS -> 'esiod2jfgio4fgjid8fjdgfj4fhkdoj2h93y.rtfhhjklgh4hjfdghkj78fhhjhjk4fg7gbjhkjkl4fedfs8cgfhj4efdffgh4fgdfrtfh4fgtrymmn4dffgdww8dcfvg.fghgjhhjh_4fg4gh5g4gh4dgfgdsfgh5g9dfhbg4dOsg'.
token = '' # ENTER YOUR MINERGATE ACCESS TOKEN PYTHON HERE !!
miner_headers = {
	'Content-Type': 'application/json',
	'token': token
}

def start(url):
	req = requests.get(url,headers=miner_headers)
	if 'error' in req.json():
		if req.json()['error'] == 'MissingToken':
			print '[X] PLEASE EDIT YOUR ACCESS TOKEN IN THE SCRIPT.'
		elif req.json()['error'] == 'TokenInvalid':
			print '[X] PLEASE WRITE YOUR ACCESS TOKEN RIGHT.'
		else:
			print '[X] UNEXPECTED ERROR.'
	else:
		print req.json()

tools = ['balance','transfers','withdrawals','workers','mstates','affiliate_links_all','affiliate_links_children','invoices','nick_name','block_chain_info']
for tool in tools:
	print '[$] '+tool
im = raw_input('\n[X] CHOOSE URL API TOOL NAME X> ')
print ''
if str(im) in tools and str(im) == 'balance':
	start(balance)
elif str(im) in tools and str(im) == 'transfers':
	start(transfers)
elif str(im) in tools and str(im) == 'withdrawals':
	start(withdrawals)
elif str(im) in tools and str(im) == 'workers':
	start(workers)
elif str(im) in tools and str(im) == 'mstates':
	start(mstates)
elif str(im) in tools and str(im) == 'affiliate_links_all':
	start(affiliate_links_all)
elif str(im) in tools and str(im) == 'affiliate_links_children':
	start(affiliate_links_children)
elif str(im) in tools and str(im) == 'invoices':
	start(invoices)
elif str(im) in tools and str(im) == 'nick_name':
	start(nick_name)
elif str(im) in tools and str(im) == 'block_chain_info':
	start(block_chain_info)
else:
	print '[X] PLEASE CHOOSE A CORRECT PARAM.'

if __name__ == '__main__':
	pass
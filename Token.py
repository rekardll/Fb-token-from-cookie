#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Made By Tech Abm 
import os,re,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,requests
    
os.system("clear") 
abm_banner ="""
\033[1;93m             d8888 888888b.   888b     d888 \033[1;0m
\033[1;91m            d88888 888  "88b  8888b   d8888 \033[1;0m
\033[1;93m           d88P888 888  .88P  88888b.d88888 \033[1;0m
\033[1;91m          d88P 888 8888888K.  888Y88888P888 \033[1;0m
\033[1;93m         d88P  888 888  "Y88b 888 Y888P 888 \033[1;0m
\033[1;91m        d88P   888 888    888 888  Y8P  888 \033[1;0m
\033[1;93m       d8888888888 888   d88P 888   "   888 \033[1;0m
\033[1;91m      d88P     888 8888888P"  888       888 \033[1;0m
\033[1;97m--------------------------------------------------
\033[1;93m➤\033[1;97m Author   : Tech-Abm                        
\033[1;93m➤\033[1;97m Github   : https://github.com/Tech-abm
\033[1;93m➤\033[1;97m Fb Page  : https://m.facebook.com/Techabm
\033[1;93m--------------------------------------------------
                                                """    
os.system("clear") 
print (abm_banner) 
print('** < GET FB ACCESS TOKEN FROM COOKIE > **').center(50)
print('** < USE ANY PROXY TO PUT COOKIES HERE >**').center(50)
print("\033[1;97m--------------------------------------------------")
cookie = input('\033[1;97mCookie :\033[1;92m ')
print("\033[1;97m--------------------------------------------------") 
try:
    data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
        'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # don't change this user agent.
        'referer'                   : 'https://m.facebook.com/',
        'host'                      : 'm.facebook.com',
        'origin'                    : 'https://m.facebook.com',
        'upgrade-insecure-requests' : '1',
        'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'             : 'max-age=0',
        'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'              : 'text/html; charset=utf-8'
    }, cookies = {
        'cookie'                    : cookie
    })
    find_token = re.search('(EAAA\w+)', data.text)
    results    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token here : ' + find_token.group(1)
except requests.exceptions.ConnectionError:
    results    = '\n* Fail : no connection here !!'
except:
    results    = '\n* Fail : unknown errors, please try again !!'

print(results)

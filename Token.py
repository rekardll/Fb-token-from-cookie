#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Made By Tech Abm 
import os,re,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,requests
    
os.system("clear") 
abm_banner ="""
\033[1;97m           _____ __________    _____   
\033[1;97m          /  _  \\______   \  /     \  
\033[1;97m         /  /_\  \|    |  _/ /  \ /  \ 
\033[1;97m        /    |    \    |   \/    Y    \
\033[1;97m        \____|__  /______  /\____|__  /
\033[1;97m                \/       \/         \/ 
\033[1;97m       [**https://github.com/Tech-abm**]  
\033[1;97m--------------------------------------------------
                                                """    
os.system("clear") 
print (abm_banner) 
print('\t** < GET FB ACCESS TOKEN FROM COOKIE > **\n')
print('\t** < USE ANY PROXY TO PUT COOKIES HERE >**\n') 
print("\033[1;97m--------------------------------------------------")
print('') 
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

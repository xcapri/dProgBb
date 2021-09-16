import requests
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore,Back,init
import datetime
import os
import random
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init()


class x504f4e424f545f424f554e54:
    def __init__(self):
		# BIKIN DIRECTORY
		self.red  = '\033[91m'
		self.blue  = '\033[94m'
		self.green = '\033[92m'
		self.white = '\033[00m'
		self.cyan    = '\033[0;96m'
		self.kolor_lo = [self.red, self.blue, self.green, self.white, self.cyan]
		self.date = datetime.datetime.now().date()
		try:
			pwd = os.getcwd()
			self.Outputs = os.path.join(pwd, "output/"+str(self.date)+"/")
			os.makedirs(self.Outputs)
		except:
			pass
		
		# tambah keyword di file listkey.txt
		self.keybounty = [i.strip() for i in open('listkey.txt').readlines()]
		self.pathbounty = [i.strip() for i in open('path.txt').readlines()]


    def x62616e6e6572(self): 
		print("""{}



     _//_///////                            _// _//   _//      
     _//_//    _//                          _/    _// _//      
     _//_//    _//_/ _///   _//       _//   _/     _//_//      
 _// _//_///////   _//    _//  _//  _//  _//_/// _/   _// _//  
_/   _//_//        _//   _//    _//_//   _//_/     _//_//   _//
_/   _//_//        _//    _//  _//  _//  _//_/      _/_//   _//
 _// _//_//       _///      _//         _// _//// _// _// _//  
                                     _//                          
        {}                               
        {}                               
        Start date: {}

			""".format(random.choice(self.kolor_lo), "Detect Program Bug Bounty",  "Mung nggo golet-golet", self.date))
    
    
    def x636865636b(self, body, url): #cek apakah ada keyword yg berbau program bug bounty
        try:
            bodyx =  body.text
            for key in self.keybounty:
                if key in bodyx:
                    print (self.green+"[!] Found  "+key+" on{} {}".format(self.white, url))
                    self.x73617665("key-"+key+".txt", url)
                else:
                    print (self.red+"[!] Not found  "+key+" on "+url)

        except:
		pass
    
    def x73617665(self, title, url): # function buat save result
		try:
			open(self.Outputs+"/"+title, "a").write(url+"\n")
		except:
			pass

    def x676173476f6c6574(self, domain): # buat ngerequest
        try:
            for pPath in self.pathbounty:

                if domain.startswith(('http://', 'https://')):
                    url = domain+pPath
                    r = requests.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0; dProgBb) Gecko/20190101 Firefox/77.0"})
                    self.x636865636b(r, url)
                else:
                    url = 'http://'+domain+pPath
                    r = requests.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0; dProgBb) Gecko/20190101 Firefox/77.0"}, allow_redirects=True)
                    hr = requests.get(r.url, headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0; dProgBb) Gecko/20190101 Firefox/77.0"})
                    self.x636865636b(hr, r.url)
        except:
		pass

# try:
x4c6f6164436c617373 = x504f4e424f545f424f554e54() # manggil class
x4c6f6164436c617373.x62616e6e6572()               # manggil banner
x6c69737472616e646f6d776562 = [i.strip() for i in open(str(raw_input("List : "))).readlines()]  # ngingput dan load list
x62616e74657265 = Pool(int(input('Thread : ')))   # input jumlah threads

try:
    x62616e74657265.map(x4c6f6164436c617373.x676173476f6c6574, x6c69737472616e646f6d776562)     # lets go 
except KeyboardInterrupt:
        print("CTRL+C Detect, Exit!")
        exit()


# refrensi code :
# aHR0cHM6Ly9naXRodWIuY29tL2p1c3Rha2F6aC9MYUNyb3Q= (Akazh)

import requests,datetime,os,random,json,optparse,re,sys
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from colorama import init, Fore, Back, Style
init()

class dProgs:
    def __init__(self):
        self.keybounty = json.load(open('helper/regex.json', "r", encoding="utf-8"))
        self.pathbounty = [i.strip() for i in open('helper/path.txt').readlines()]
        self.radncolor = [Fore.RED, Fore.CYAN, Fore.WHITE, Fore.GREEN, Fore.YELLOW, Fore.BLUE]
        self.date = datetime.datetime.now().date()
        self.headers = {
                        'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                    }    
        
    def bannEr(self):
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
			""".format(random.choice(self.radncolor), "Detect Program Bug Bounty",  "Mung nggo golet-golet, syukur nemu", self.date))
    
    
    def get(self, domain):
        try:
            for xpath in self.pathbounty:
                full_url = "{}{}".format(domain,xpath)
                getbody = requests.get(full_url, headers=self.headers,verify=False, allow_redirects=True, timeout=3) # request
                if (getbody.status_code == 404 or getbody.status_code == 403 
                    or "No route" in getbody.text or "Not Found" in getbody.text):
                    print(Fore.RED+"[FIND] "+Fore.RESET+full_url+Fore.RED+" Not Found "+Fore.RESET)
                else:
                    self.checkKeyonResponse(getbody.text, full_url) # send body to key response
	except ConnectionError:
            pass
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.ReadTimeout:
            pass
        except KeyboardInterrupt:
            print(f"CTRL+C Detect, Exit!")
            exit()
    def checkKeyonResponse(self, body, domain):
        try:
            for _data in self.keybounty["data"]:
                findkey = re.compile(r""+_data["regex"],re.IGNORECASE)
                output = findkey.findall(str(body))
                if len(output) > 0 :
                    print("\n"+Fore.GREEN+"[POSSBOUNTY] "+Fore.RESET+domain+Fore.GREEN+" ( "+_data["name"]+" | "+ str(output)  +" )"+Fore.RESET)
                    datares = "\nFOUND="+str(','.join(output))+"\n"+domain
                    saveres = open("results/found_"+_data["file"], "a+")
                    saveres.write(datares+"\n")
                else:
                    print(Fore.RED+"[NOTFOUND] "+Fore.RESET+domain+Fore.RED+" ( "+_data["name"]+" | NULL )"+Fore.RESET)
        except KeyboardInterrupt:
            print(f"CTRL+C Detect, Exit!")
            exit()
    
    def req(self, domain):
        try:
            self.get(domain)
        except ConnectionError:
            print(f"No Internet Connection")
	except ConnectionError:
            pass
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.ReadTimeout:
            pass
        except KeyboardInterrupt:
            print(f"CTRL+C Detect, Exit!")
            exit()

dProgs = dProgs() # call class 
dProgs.bannEr()

if(sys.stdin.isatty() == False):
    p = optparse.OptionParser()
    p.add_option('--thread', '-t', default=10)
    options, arguments = p.parse_args()
    yourls = [i.strip() for i in sys.stdin.readlines()]  # input and load list
    rpm = Pool(int(options.thread))        # input number of threads
    try:
        rpm.map(dProgs.req, yourls)     # lets go 
    except KeyboardInterrupt:
            print("CTRL+C Detect, Exit!")
            exit()
            
else:
    yourls = [i.strip() for i in open(str(input("List : "))).readlines()]  # input and load list
    rpm = Pool(int(input('Thread : ')))       # input number of threads
    try:
        rpm.map(dProgs.req, yourls)     # lets go 
    except KeyboardInterrupt:
            print("CTRL+C Detect, Exit!")
            exit()

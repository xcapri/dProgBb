#!/usr/bin/python3

import requests,datetime,os,random,json,optparse,re,sys,argparse
from multiprocessing.dummy import Pool
from requests.exceptions import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import init, Fore, Back, Style
from urllib.parse import urlparse

import requests

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init()


class dProgs:
    def __init__(self, options):
        self.options = options
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.keybounty_path = os.path.join(script_dir, 'helper/regex.json')
        self.pathbounty_path = os.path.join(script_dir, 'helper/path.txt')
        self.keybounty = json.load(open(self.keybounty_path, "r", encoding="utf-8"))
        self.pathbounty = [i.strip() for i in open(self.pathbounty_path).readlines()]
        self.reqexcpet = (ConnectionError, Timeout, ReadTimeout, TooManyRedirects, InvalidURL, ProxyError, HTTPError,
                          SSLError, ChunkedEncodingError)
        self.radncolor = [Fore.RED, Fore.CYAN, Fore.WHITE, Fore.GREEN, Fore.YELLOW, Fore.BLUE]
        self.date = datetime.datetime.now().date()
        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        }
        self.output_folder = options.output if options.output else "results"  # Use "results" as default if not specified
        os.makedirs(self.output_folder, exist_ok=True)

    def bannEr(self):
        print(
            """{}
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
            """.format(random.choice(self.radncolor), "Detect Program Bug Bounty", "Mung nggo golet-golet, syukur nemu", self.date))

    def get(self, domain):
        try:
            checkpath = " " if len(urlparse(domain).path) >= 1 else self.pathbounty
            for xpath in checkpath:
                full_url = "{}{}".format(domain, xpath).replace(" ", "")
                getbody = requests.get(full_url, headers=self.headers, verify=not self.options.ignore_ssl,
                                       allow_redirects=True, timeout=3)  # request
                if (getbody.status_code in [404, 403]
                        or any(error in getbody.text for error in ["Debug", "No route", "Not Found", "404", "Uncaught Exception"])):
                    if self.options.verbose:
                        print(Fore.RED + "[SKIPCHECK] " + Fore.RESET + full_url + Fore.RED + " Not Found " + Fore.RESET)
                else:
                    self.checkKeyonResponse(getbody.text, full_url)  # send body to key response

        except self.reqexcpet as e:
            pass
        except KeyboardInterrupt:
            print(f"CTRL+C Detect, Exit!")
            exit()

    def checkKeyonResponse(self, body, domain):
        try:
            for _data in self.keybounty["data"]:
                findkey = re.compile(r"" + _data["regex"], re.IGNORECASE)
                output = findkey.findall(str(body))
                if len(output) > 0:
                    print("\n" + Fore.GREEN + "[POSSBOUNTY] " + Fore.RESET + domain + Fore.GREEN + " ( " + _data[
                        "name"] + " | " + str(output) + " )" + Fore.RESET)
                    datares = "\nFOUND=" + str(','.join(output)) + "\n" + domain
                    output_filename = os.path.join(self.output_folder, "found_" + _data["file"])
                    with open(output_filename, "a+") as saveres:
                        saveres.write(datares + "\n")
                else:
                    if self.options.verbose:
                        print(Fore.RED + "[NOTFOUND] " + Fore.RESET + domain + Fore.RED + " ( " + _data[
                            "name"] + " | NULL )" + Fore.RESET)
        except KeyboardInterrupt:
            print(f"CTRL+C Detect, Exit!")
            exit()

    def req(self, domain):
        try:
            self.get(domain)
        except self.reqexcpet as e:
            pass
        except KeyboardInterrupt:
            print(f"CTRL+C Detect, Exit!")
            exit()


def main():
    parser = argparse.ArgumentParser(description="Detect Program Bug Bounty")
    parser.add_argument('-l', '--list', type=str, help='Specify a list of URLs')
    parser.add_argument('-u', '--url', type=str, help='Specify a single URL')
    parser.add_argument('-o', '--output', type=str, help='Specify the output file')
    parser.add_argument('-is', '--ignore-ssl', action='store_true', help='Ignore SSL certificate warnings')
    parser.add_argument('-t', '--thread', type=int, default=10, help='Number of threads (default: 10)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    dProgsInstance = dProgs(args)
    dProgsInstance.bannEr()

    if args.list:
        yourls = [i.strip() for i in open(args.list).readlines()]
    elif args.url:
        yourls = [args.url]
    elif not sys.stdin.isatty():
        yourls = [i.strip() for i in sys.stdin.readlines()]
    else:
        yourls = [i.strip() for i in input("List : ").split()]

    rpm = Pool(args.thread)
    try:
        rpm.map(dProgsInstance.req, yourls)
    except KeyboardInterrupt:
        print("CTRL+C Detect, Exit!")
        exit()


if __name__ == '__main__':
    main()

<h1 align="center">
dProg 🔍
</h1>

dProg is tool for Bug bounty program detection by similar <i>keyword</i> on bug bounty program page 

## Features

- Easily check multiple URLs for Bug Bounty Detector.
- Customizable keyword patterns for detection.
- Multithreaded scanning for faster results.
- Save positive findings to a file for further analysis.

#### Show Case
![image](demo.gif)

#### Instalation
- pip3 install git+https://github.com/xcapri/dProgBb.git

#### Usage
```
usage: dprog [-h] [-l LIST] [-u URL] [-o OUTPUT] [-is] [-t THREAD] [-v] [-w WORDLISTS_PATH] [-r REGEX]

Detect Program Bug Bounty

options:
  -h, --help            show this help message and exit
  -l LIST, --list LIST  Specify a list of URLs
  -u URL, --url URL     Specify a single URL
  -o OUTPUT, --output OUTPUT
                        Specify the output file
  -is, --ignore-ssl     Ignore SSL certificate warnings
  -t THREAD, --thread THREAD
                        Number of threads (default: 10)
  -v, --verbose         Enable verbose output
  -w WORDLISTS_PATH, --wordlists-path WORDLISTS_PATH
                        Specify the path to wordlists file
  -r REGEX, --regex REGEX
                        Specify one or more regex patterns for keyword matching
```

You can run like
* Oneliner with katana <br>``` cat list | httpx -silent | katana -silent | dprog -t 20 | sort -u | notify -id dprog ```
* Oneliner <br> <code>cat list | httpx | dprog -t 20 </code>
* Oneliner with hakrawler <br><code>cat list | hakrawler | sort -u | dprog -t 20 | notify</code>
* Oneliner with notify <br><code>cat list | httpx | dprog -t 20 | sort -u | notify -id dprog </code>

#### Reference
* https://github.com/JoyGhoshs/findbb (FindBBProgram) 🤘

#### Demo
You can see this video for demo : <br>
https://youtu.be/z5IkjxTGHa8

### Contribution
If you want to contribute, you can add a path or regex around the bug bounty
* [Path](/core/helper/path.txt) 
* [Regex](/core/helper/regex.json)

### Support 
Follow my organization <br>https://github.com/tegal1337

### Thanks

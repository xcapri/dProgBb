# dProg
#### About
dProg is tool for Bug bounty program detection by similar keyword on bug bounty program page
#### Picture
#### Instalation
* <code>git clone https://github.com/xcapri/dProgBb.git</code>
* <code>cd dProgBb</code>
* and run like a below
#### Run
You can run like
* Oneliner <code>cat list | httpx | py dprog.py (--thread / -t) 20</code>
* Oneliner with notify <code>cat list | httpx | py dprog.py (--thread / -t) 20 | grep "[FOUND]" | sort -u | notify -id dprog </code>
* By input list <code>py dprog.py</code>

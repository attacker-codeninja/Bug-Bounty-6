import sys

#Author: Ahmed Taher (@IAmAhmedTahar)
#Tool to find interesting subdomains
#Usage: cat subs.txt | python3 interest_subs.py

interesting_subs = ['admin','user','login','register','mail','api', 'blog', 'domain', 'test', 'proxy', 'stage', 'devops' , 'staff', 'db', 'internal', 'shop', 'news', 'landing']

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break

    for sub in interesting_subs:
    	if(sub in line):
    		print(line.strip())


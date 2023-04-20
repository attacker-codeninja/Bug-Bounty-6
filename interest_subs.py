import sys

#Author: Ahmed Taher (@IAmAhmedTahar)
#Tool to find interesting subdomains
#The tool read from stdin

interesting_subs = ['admin','user','login','register','mail','api', 'blog', 'domain', 'test', 'proxy', 'stage', 'devops' , 'staff', 'db', 'internal', 'shop', 'news', 'landing']

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break

    sub_addr = line.partition('.')[0]

    if sub_addr in interesting_subs:
    	print(line.strip())


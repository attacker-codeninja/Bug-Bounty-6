import sys

#Author: Ahmed Taher (@IAmAhmedTahar)
#Tool to find interesting subdomains

interesting_subs = ['admin','user','login','register','mail','api', 'blog', 'domain', 'test', 'proxy', 'stage', 'devops' , 'staff', 'db', 'internal', 'shop', 'news', 'landing']

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    host = line.partition('://')[2]
    sub_addr = host.partition('.')[0]

    if sub_addr in interesting_subs:
    	print(line.strip())


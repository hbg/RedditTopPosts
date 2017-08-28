
import urllib 
from bs4  import BeautifulSoup
import ssl
import re
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
if not os.path.isfile("topposts.txt"):
	topposts = []
us = 0
			
with open ("topposts.txt","a") as f:
	htmltext = urllib.urlopen("http://www.reddit.com", context=ctx).read()


	soup =  BeautifulSoup(htmltext, "html5lib")

	 
	results = soup.findAll("a", attrs={"class": "title may-blank outbound" })
	users = soup.findAll("p", attrs= {"class": "tagline"})
	i = 0
	for r in results:
		i = i + 1
		stringV = "%s" % r
		returnV = re.sub(r'.*\">', '', stringV)
		returnV = returnV.replace("</a>","",1)
		f.write(returnV + "\n\n")

		print "Post #%s, Title: %s" % (i,returnV)

	for u in users:
		us = us + 1
		stringV = "%s" % u
		returnV = re.sub(r'.*https://www.reddit.com/user/', 'https://www.reddit.com/user/', stringV)
		
		head, sep, tail = returnV.partition('\"')

		print "Author for Post %s: %s" % (us,head)
		f.write(returnV + "\n\n")


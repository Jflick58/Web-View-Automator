##Web View Automator 
##This is a script for automating views of a webpage for marketing/SEO purposes.
## Flick58 


import webbrowser ## import for navigating to the URL
import requests ## import for proxy
import time ##import for delaying the script
from random import randint ##import for random time delay
from fake_useragent import UserAgent #import for randomizing useragent (browser profile) to fool trackers



ua= UserAgent()
x = 1
while True:  
    ua.random ##randomize user agent every time the script runs
    http_proxy  = "http://40.113.118.174:8143"  ## HTTP Proxy
    https_proxy = "https://40.113.118.174:8143" ## HTTPS Proxy
    webbrowser.open('https://www.google.com', new=0, autoraise=True % x) ## Navigate to URL 
    time.sleep(randint(1,10)) ## Random time delay before page refreshes 
    x += 1 ## Makes the loop run until you quit your python shell 


    

    
    
    
    




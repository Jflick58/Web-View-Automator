##Web View Automator 
##This is a script for automating views of a webpage for marketing/SEO purposes.
## Flick58 


import webbrowser ## import for navigating to the URL
import requests ## import for proxy
import sys ## import for exiting
import time ##import for delaying the script
from random import randint ##import for random time delay
from fake_useragent import UserAgent #import for randomizing useragent (browser profile) to fool trackers
import easygui as g ##import for GUI

##This opens the start menu. The user can begin the program, visit my github page, or exit the program
while True: 

        version = 'Web View Automator 1.0.2'

        options = ['Start', 'Developer Page', 'Exit']

        button = g.buttonbox('Welcome to Web View Automator' + '\n' + '\n'  + '\n' + '\n' + '\n' + 'Created by Justin Flick, Copyright 2016' , title = version, choices = options)

        if button == options[0]:
                pass 
        if button == options[1]:
                webbrowser.open('https://github.com/Jflick58/Web-View-Automator', new=0, autoraise=True)
        if button == options[2]:
                sys.exit()

		##Opens a GUI box for the user to input their proxy information, website, and number of times they want the script to run

        msg = "Enter your website information. To find a list of free proxies, please visit https://incloak.com/proxy-list/"
        title = version
        fieldNames = ["HTTP Proxy (xxx.xxx.xxx.xxx:xx) ","HTTPS Proxy (xxx.xxx.xxx.xxx:xx)","URL","How many views?"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = g.multenterbox(msg,title, fieldNames)

		##this is the script
        ua= UserAgent()
        count = 0
        x= int(fieldValues[3])
        while (count < x):
                ua.random ##randomize user agent every time the script runs
                http_proxy  = fieldValues[0] ## HTTP Proxy
                https_proxy = fieldValues[1] ## HTTPS Proxy
                webbrowser.open(fieldValues[2], new=0,) ## Navigate to URL 
                time.sleep(randint(1,10)) ## Random time delay before page refreshes 
                count = count + 1 ## Makes the loop run until you quit your python shell 

        else :
        	options2 = ['Continue', 'Exit']
        	button = g.buttonbox('Thank you for using Web View Automator. Run again?' , title = version, choices = options2)

        	if button == options[0]:
        		pass
        	if button == options[1]:
        		sys.exit()

    
    
    
    




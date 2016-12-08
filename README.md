# Web-View-Automator
This is a script for automating views of a webpage for marketing/SEO purposes. 

Requirements: 
- Python 3.5 or higher 
- Knowledge of how to run a python script. 

Instructions: 

1. Run the "set_up.py" script. This installs the external modules that the main script uses. 

2. Open "Web View Automator.py" in a text editor

3.  Edit the line that says 

        webbrowser.open('https://www.google.com', new=0, autoraise=True % x) ## Navigate to URL 
        
   and change the url to whatever page you are navigating too 
   
4. (Optional) Edit 
         
         http_proxy  = "http://40.113.118.174:8143"  ## HTTP Proxy
         https_proxy = "https://40.113.118.174:8143" ## HTTPS Proxy
         
    To use the HTTP/HTTPS proxy of your choice. By default, it uses one located in France. Find other ones here:    
    https://incloak.com/proxy-list/
    
5. Save the file and close 

6. Run the file, it should open using your default broswer. 

7. When finished, quit your python shell. 

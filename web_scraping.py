#1st step install and import modules
#-- pip/pip3 install lxml
#--pip /pip3 install requests 
#-- pip/pip3 install beautifulSoup4

import requests 
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

#2nd step use requests to fetch the url
result =requests.get("https://wuzzuf.net/search/jobs/?q=")

#3rd step save page content/markup
src=result.content

#4th step find the elements containing info we need
soup=BeautifulSoup(src,"lxml")

#5th step find the elements containing info we need
#-- job titles|job skills|company|names|location names
job_titles=soup.find_all("h2",{"class":"css-m604qf"})
company_names=soup.find_all("a", {"class":"css-17s97q8"})
locations_names=soup.find_all("span",{"class":"css-5wys0k"})
job_skills=[]
divs = soup.find_all("div")

for div in divs:
    if div.find("a", {"class": "css-5x9pm1"}):
        job_skills.append(div)  


print(job_skills)
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

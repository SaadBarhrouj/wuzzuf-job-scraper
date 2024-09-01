#1st step install and import modules
#-- pip/pip3 install lxml
#--pip /pip3 install requests 
#-- pip/pip3 install beautifulSoup4

job_title=[]
company_name=[]
location_name=[]
skills=[]
links=[]

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
target_divs = soup.find_all("div", {"class": "css-1lh32fc"})

job_skills=[]
for target_div in target_divs:
    following_div = target_div.find_next_sibling("div") 
    
    if following_div:
        if following_div.find("a", {"class": "css-5x9pm1"}) and following_div.find("a", {"class": "css-o171kl"})  :
           job_skills.append(following_div)
#6th step loop over returned lists to extract needed info into other lists

# Iterate over the indices of the 'job_titles' list
# 'range(len(job_titles))' generates a sequence of numbers from 0 to the length of 'job_titles' - 1
# For example, if 'job_titles' has 5 elements, 'range(len(job_titles))' will generate 0, 1, 2, 3, 4
# This allows you to access each element of the list by its index 'i'

for i in range(len(job_titles)):
   job_title.append(job_titles[i].text)
   links.append(job_titles[i].find("a").attrs['href'])
   company_name.append(company_names[i].text)
   location_name.append(locations_names[i].text)
   skills.append(job_skills[i].text)

# 7th step create csv file and fill it with values
file_list=[job_title,company_name,location_name,skills,links]
exported=zip_longest(*file_list)
# Or: with open("C:\\Users\\Lenovo\\Desktop\\test22\\jobs-stats.csv", "w") as file:

with open(r"C:\Users\Lenovo\Desktop\test22\jobs-stats.csv","w") as file:
  wr=csv.writer(file)
  wr.writerow(["Job Title","Company Name","Location","Skills","links"])
  wr.writerows(exported)
 


 



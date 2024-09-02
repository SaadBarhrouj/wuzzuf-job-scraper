import requests 
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
skills = []
links = []
Salary = []
date = []
responsibilities=[]
page_num = 0

while True:
   
      # 2nd step use requests to fetch the url
      result = requests.get(f"https://wuzzuf.net/search/jobs/?a=navbl&q=python&start={page_num}")
      
      # 3rd step save page content/markup
      src = result.content
      
      # 4th step find the elements containing info we need
      soup = BeautifulSoup(src, "lxml")

      page_limit=int(soup.find("strong").text)
      if(page_num >page_limit//15):
         print("pages ended,terminate")
         break
      
      # 5th step find the elements containing info we need
      job_titles = soup.find_all("h2", {"class": "css-m604qf"})
      company_names = soup.find_all("a", {"class": "css-17s97q8"})
      locations_names = soup.find_all("span", {"class": "css-5wys0k"})
      target_divs = soup.find_all("div", {"class": "css-1lh32fc"})
      posted_new = soup.find_all("div", {"class": "css-4c4ojb"})
      
      job_skills = []
      for target_div in target_divs:
         following_div = target_div.find_next_sibling("div")
         if following_div:
               if following_div.find("a", {"class": "css-5x9pm1"}) and following_div.find("a", {"class": "css-o171kl"}):
                  job_skills.append(following_div)
      
      # 6th step loop over returned lists to extract needed info into other lists
      for i in range(len(job_titles)):
         job_title.append(job_titles[i].text.strip())
         links.append(job_titles[i].find("a").attrs['href'])
         company_name.append(company_names[i].text.strip())
         location_name.append(locations_names[i].text.strip())
         skills.append(job_skills[i].text.strip() if i < len(job_skills) else "N/A")
         date.append(posted_new[i].text.strip() if i < len(posted_new) else "N/A")
      
      page_num += 1  # Increase page number for next iteration
      print("Page switched")

      if len(job_titles) == 0:
         break  # Exit loop if no more jobs are found
  
       
# Fetch salaries
for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    requirements=soup.find("div",{"class":"css-1t5f0fr"})
    if requirements:
            requirements=requirements.ul
            responsibilities_text=""
            for li in requirements.find_all("li"):
                responsibilities_text+=li.text+"| "
            responsibilities_text=responsibilities_text[:2]    
            responsibilities.append(responsibilities_text)
       
    else:
        responsibilities.append("N/A")

       
    salaries = soup.find("span", {"class": "css-4xky9y"})
    
    if salaries:
        Salary.append(salaries.text.strip())
    else:
        Salary.append("N/A")

# 7th step create csv file and fill it with values
file_list = [job_title, company_name, location_name, skills, Salary,responsibilities, date]
exported = zip_longest(*file_list)

with open(r"C:\Users\Lenovo\Desktop\test22\jobs-stats.csv", "w", newline='', encoding='utf-8') as file:
    wr = csv.writer(file)
    wr.writerow(["Job Title", "Company Name", "Location", "Skills", "Salary","Responsibilitie" ,"Date"])
    wr.writerows(exported)

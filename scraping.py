import requests
from bs4 import BeautifulSoup

website_urls='https://infopark.in/companies/jobs'
output_file=open("jobs.txt","w")

res=requests.get(website_urls)
soup=BeautifulSoup(res.text,'lxml')
jobs=soup.find_all('div',{'class':'row company-list joblist'})
keyword=['python','php']
for job in jobs:
    title_element=job.find('a')
    title=title_element.text
    link=title_element['href']
    company_name=job.find('div',{'class':'jobs-comp-name'}).text
    last_date=job.find('div',{'class':'job-date'}).text
    # print(last_date)
    if any(word.lower() in title.lower() for word in keyword):
        # print(title,company_name,last_date)
        output_file.write(title + " - "+ company_name + " - " + last_date + " - " + link + "\n\n")

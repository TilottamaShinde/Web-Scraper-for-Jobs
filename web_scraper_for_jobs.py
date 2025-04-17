from http.client import responses

import requests
from bs4 import BeautifulSoup
import pandas as pd

url =  "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=plsql&txtLocation="
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
jobs= []

job_cards = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job_card in job_cards:
    if 'today' in job_card.find('span', class_='sim-posted').text.lower():  # Only today's jobs
        title = job_card.find('h2').text.strip()
        company = job_card.find('h3', class_='joblist-comp-name').text.strip()
        ul_tag = job_card.find('ul', class_='top-jd-dtl clearfix')
        exp = ''
        exp_tag = job_card.find('ul', class_='top-jd-dtl clearfix')
        if exp_tag and len(exp_tag.find_all('li')) > 1:
            exp = exp_tag.find_all('li')[1].text.strip()

        location = ul_tag.li.text.strip() if ul_tag and ul_tag.li else ''
        posted = job_card.find('span', class_='sim-posted').text.strip()
        job_url = job_card.header.h2.a['href']

salary = ''

jobs.append({
    'Title':title,
    'Company':company,
    'Experience':exp,
    'Location':location,
    'Salary':salary,
    'Job URL':job_url
})

df = pd.DataFrame(jobs)
df.to_csv('timesjobs_plsql_jobs.csv', index = False)
print("Srapped Job data is saved in timesjobs_plsql_jobs.csv")
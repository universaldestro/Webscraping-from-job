from bs4 import BeautifulSoup
import requests
import time
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text #where you put the website url
    #print(html_text)#200 means request done successfully

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate (jobs):
        post_date = job.find('span', class_='sim-posted').span.text
        if 'few' in post_date:
    #print(jobs)
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

            skills = job.find('span', class_='srp-skills').text.replace(' ','')
    #always    test
    #print(c   ompany_name)
    #print(s   kills)
            with open(f'Part2/posts/{index}.txt','w') as f:

                f.write(f'''
    Company Name:{company_name.strip()}

    Required Skills:{skills.strip()}

    {post_date.strip()}
            ''')
                print(f' File saved {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait =10
        print(f'Waiting {time_wait} minutes... ')
        time.sleep(time_wait * 2)

thonfrom bs4 import BeautifulSoup

def parse_job_listings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    job_listings = []
    job_items = soup.find_all('div', class_='vacancy-serp-item')

    for item in job_items:
        job_data = {}
        job_data['jobId'] = item['data-jobid']
        job_data['title'] = item.find('a', class_='bloko-link').text.strip()
        job_data['company'] = item.find('div', class_='vacancy-serp-item__meta-info').text.strip()
        job_data['salary'] = item.find('div', class_='vacancy-serp-item__sidebar').text.strip()
        job_data['location'] = item.find('span', class_='vacancy-serp-item__meta-info').text.strip()
        job_data['url'] = item.find('a', class_='bloko-link')['href']
        job_listings.append(job_data)
    
    return job_listings
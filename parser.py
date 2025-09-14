import requests
from bs4 import BeautifulSoup
import re

from data import UrlData



def get_url_data(url):
    response = requests.get(url)
    html_source = response.text
    return BeautifulSoup(html_source, 'html.parser')


def get_job_description(soup):
    job_description = soup.find('div', class_='ajd_job-details__ats-description').decode_contents()

    # clean up span tags, which tend to contain text inside of them
    text = re.sub(r'</?span[^>]*>', '', job_description)

    # clea up html tags
    text = re.sub(r'<[^>]+>', ' ', text)

    # remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def parse_url(url):
    data = UrlData(url)

    # get the raw HTML
    soup = get_url_data(url)

    # get the job title
    data.job_title = soup.find('h1', class_='ajd_header__job-title').text.strip()

    # get the job description
    data.set_job_description(get_job_description(soup))

    # return the data object
    return data


import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    # print(result.status_code)
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", {"class", "pagination"})
    links = pagination.find_all("a")
    pages = []  

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(URL + f"&start={page * LIMIT}")
        print(f"{result.status_code} <-- {page + 1}")
    return jobs
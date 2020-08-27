import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)
    # print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class", "pagination"})
    links = pagination.find_all("a")
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class", "title"}).find("a")["title"]
    company_span = html.find("span", {"class", "company"})
    if company_span.find("a") is not None:
        company = company_span.find("a").string.strip()
    else:
        company = company_span.string.strip()

    location = html.find("div", {"class", "recJobLoc"})["data-rc-loc"]
    data_jk = html["data-jk"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://kr.indeed.com/viewjob?jk={data_jk}",
    }


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"scrapping page: {page}")
        body_content = requests.get(URL + f"&start={page * LIMIT}")
        soup = BeautifulSoup(body_content.text, "html.parser")
        posters = soup.find_all("div", {"class", "jobsearch-SerpJobCard"})

        for poster in posters:
            jobs.append(extract_job(poster))

    return jobs
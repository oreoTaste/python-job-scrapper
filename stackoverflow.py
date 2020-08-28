import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"


def foreach(iterable):
    result = ""
    for element in iterable:
        result = result + " " + element.strip()
    return result


def extract_stackoverflow_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pages = soup.find_all("a", {"class", "s-pagination--item"})
    max_page = int(pages[-2].find("span").string)
    return max_page


def extract_job(html):
    title = html.find("a", {"class", "s-link stretched-link"})["title"]

    # used another way
    company, location = html.find("h3", {"class", "fc-black-700 fs-body1 mb4"}).find_all(
        "span", recursive=False
    )
    company = company.getText(strip=True)
    location = location.getText(strip=True)

    # company = html.find("h3", {"class", "fc-black-700 fs-body1 mb4"}).find("span").string
    # if company is None:
    #     company_span = html.find("h3", {"class", "fc-black-700 fs-body1 mb4"}).find("span").strings
    #     company = foreach(company_span)
    # else:
    #     company = company.strip()
    # location = html.find("span", {"class", "fc-black-500"}).string.strip()
    link = (
        "https://stackoverflow.com"
        + html.find("a", {"class", "s-link stretched-link"})["href"].strip()
    )

    return {"title": title, "company": company, "location": location, "link": link}


def extract_stackoverflow_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Jobs from StackOverFlow : {page+1} / {last_page}")
        result = requests.get(f"https://stackoverflow.com/jobs?q=python&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        posters = soup.find_all("div", {"class", "-job"})
        for poster in posters:
            jobs.append(extract_job(poster))
    return jobs
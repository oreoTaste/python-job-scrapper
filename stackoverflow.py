import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python&l=korea&d=20&u=Km"


def foreach(iterable):
    result = ""
    for element in iterable:
        result = result + " " + element.strip()
    return result


def extract_job(html):
    title = html.find("a", {"class", "s-link stretched-link"})["title"]

    company, location = html.find("h3", {"class", "fc-black-700 fs-body1 mb4"}).find_all(
        "span", recursive=False
    )
    company = company.getText(strip=True)
    location = location.getText(strip=True)

    link = (
        "https://stackoverflow.com"
        + html.find("a", {"class", "s-link stretched-link"})["href"].strip()
    )

    return {"title": title, "company": company, "location": location, "link": link}


def extract_stackoverflow_jobs():
    print(f"Scrapping Jobs from StackOverFlow : 1 / 1")
    jobs = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    num_of_result = soup.find("span", {"class", "description"}).string.strip().split(" jobs")[0]
    posters = soup.find_all("div", {"class", "-job"}, limit=int(num_of_result))
    for poster in posters:
        jobs.append(extract_job(poster))
    return jobs
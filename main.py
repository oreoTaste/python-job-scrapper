import requests
from bs4 import BeautifulSoup

indeed_result = requests.get('https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50')
print(indeed_result.status_code)
soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = soup.find("div", {"class", "pagination"})
pages = pagination.find_all("a")
span = []

for page in pages:
  span.append(page.find("span"))

print(span[:-1])


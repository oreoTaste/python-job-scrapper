import requests
from bs4 import BeautifulSoup


def get_naver_word():
  r = requests.get(
      'https://search.naver.com/search.naver?query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%8B%A8%EC%96%B4')
  soup = BeautifulSoup(r.text, 'html.parser')
  box = soup.find("ul", {"class", "word_lst"})
  items = box.find_all("li", {"class", "en"})

  dics = []
  for item in items:
    word_area = item.find("p", {"class", "word_area"}
                          ).find("a").get_text().strip()
    mean = item.find("p", {"class", "mean"}).get_text().strip()
    dics.append({"word_area": word_area, "mean": mean})

  return dics

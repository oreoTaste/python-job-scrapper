import requests
from bs4 import BeautifulSoup


def district1():
    r = requests.get(
        f"https://www.daangn.com/hot_articles")
    soup = BeautifulSoup(r.text, 'html.parser')
    options = soup.find("select", {"name", "hot-articles-nav-select"})

    district = []
    for option in options:
        try:
            if option.string.strip() != '':
                district.append(option.string.strip())
        except:
            continue
    return district


def district2(district1):
    r = requests.get(
        f"https://www.daangn.com/region/{district1}")
    soup = BeautifulSoup(r.text, 'html.parser')
    options = soup.find("select", {"name", "hot-articles-nav-select"})
    options = options.find_next_sibling("select")

    district = []
    for option in options:
        try:
            if option.string.strip() != '':
                district.append(option.string.strip())
        except:
            continue
    return district


def get_danggn_items(**kwargs):
    region1 = kwargs.get("region1")
    region2 = kwargs.get("region2")
    sub_url = ''
    if region1 != None:
        if region2 == None:
            sub_url = region1
        else:
            sub_url = f"{region1}/{region2}"

    url = f"https://www.daangn.com/region/{sub_url}"
    if sub_url == '':
        url = "https://www.daangn.com/hot_articles"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    boxes = soup.find_all("article", {"class", "card-top"})

    results = []

    for box in boxes:
        item = box.find("a", {"class", "card-link"})
        link = "https://www.daangn.com" + item["href"]
        card_photo, card_desc = item.find_all("div", recursive=False)
        img = card_photo.find("img")["src"]
        title = card_desc.find("h2").string.strip()
        region = card_desc.find(
            "div", {"class", "card-region-name"}).string.strip()
        price = card_desc.find("div", {"class", "card-price"}).string.strip()
        like, chat = card_desc.find(
            "div", {"class", "card-counts"}).find_all("span")
        like = like.string.strip().split("관심 ")[1]
        chat = chat.string.strip().split("채팅 ")[1]
        results.append({"region": region,
                        "title": title,
                        "price": price,
                        "link": link,
                        "img": img,
                        "like": like,
                        "chat": chat})

    return results

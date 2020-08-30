import requests
from bs4 import BeautifulSoup


def get_danggn_items(input_region):
    r = requests.get(
        f"https://www.daangn.com/region/{input_region}/")
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

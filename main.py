from danggn_item import get_danggn_items
from naver_word import get_naver_word
from save import save_to_csv


def run():
    items = get_danggn_items("서울특별시")
    words = get_naver_word()

    for word in words:
        print(word.get("word_area"), word.get("mean"))

    for item in items:
        print(item.get("img"), item.get("title"), item.get("price"))

    save_to_csv(items)

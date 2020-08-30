from danggn_item import get_danggn_items
from naver_word import get_naver_word
from save import save_to_csv
from flask import Flask, render_template, redirect, request


app = Flask("my page")


@app.route('/')
def index():
    words = get_naver_word()
    return render_template("index.html",
                           words=words
                           )


@app.route('/search')
def search():
    region = request.args.get("region")
    items = get_danggn_items(region)
    return render_template("danggn.html",
                           items=items)


app.run(host="0.0.0.0")

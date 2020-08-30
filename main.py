from danggn_item import get_danggn_items, district1, district2
from naver_word import get_naver_word
from save import save_to_csv
from flask import Flask, render_template, redirect, request


app = Flask("my page")


@app.route('/')
@app.route('/<path:keyword>')
def index(keyword=''):
    words = get_naver_word()
    districts = district1()
    if keyword == '':
        return render_template("index.html",
                               words=words,
                               districts=districts
                               )
    else:
        districts2 = district2(keyword)
        return render_template("index.html",
                               words=words,
                               keyword=keyword,
                               districts=districts,
                               districts2=districts2
                               )


@app.route('/search')
def search():
    region1 = request.args.get("region1")
    region2 = request.args.get("region2")
    items = get_danggn_items(region1=region1, region2=region2)
    return render_template("danggn.html",
                           items=items)


app.run(host="0.0.0.0")

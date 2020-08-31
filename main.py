from danggn_item import get_danggn_items, district1, district2
from naver_word import get_naver_word
from save import save_to_csv
from flask import Flask, render_template, redirect, request, send_from_directory


app = Flask("my page")
db0 = {}
db1 = {}
db2 = {}


@app.route('/')
@app.route('/<path:keyword>')
def index(keyword=''):
    global db0
    if db0 != {}:
        words = db0
    else:
        words = get_naver_word()
        db0 = words

    global db1
    if db1 != {}:
        districts = db1
    else:
        districts = district1()
        db1 = districts

    if keyword == '':
        districts2 = ''
    else:
        global db2
        try:
            districts2 = db2[keyword]
        except:
            districts2 = district2(keyword)
            db2[keyword] = districts2
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

    save_to_csv(items, filename="danggn.csv")
    return render_template("danggn.html",
                           items=items,
                           filename="danggn.csv")


@app.route('/download/<path:filename>')
def download(filename):

    return send_from_directory(directory="download",
                               filename=filename,
                               as_attachment=True,
                               cache_timeout=0)


app.run(host="0.0.0.0")

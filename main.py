from flask import Flask, render_template, request, redirect
from scrapper import start_scrap as scrap
app = Flask("job scrapper")


@app.route('/')
def index():
  return render_template("home.html")


@app.route("/report")
def report():
  lan = request.args.get("lan")
  if lan:
    lan = lan.lower()
    print(scrap(lan))
    return render_template("report.html", searchingBy=lan)
  else:
    return redirect('/')


app.run(host="0.0.0.0")

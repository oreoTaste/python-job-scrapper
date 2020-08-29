from flask import Flask, render_template, request, redirect, send_file
from scrapper import start_scrap as scrap
from save import save_to_csv

app = Flask("job scrapper")
db = {}


@app.route('/')
def index():
  return render_template("home.html")


@app.route("/report")
def report():
  lan = request.args.get("lan")
  if lan:
    lan = lan.lower()
    existingJobs = db.get(lan)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = scrap(lan)
      db[lan] = jobs
    return render_template(
        "report.html",
        searchingBy=lan,
        resultNumber=len(jobs),
        jobs=jobs
    )
  else:
    return redirect('/')


@app.route("/export")
def download():
  try:
    lan = request.args.get("lan")
    if not lan:
      raise Exception()
    lan = lan.lower()
    jobs = db.get(lan)
    if not jobs:
      raise Exception()
    save_to_csv(jobs)
    return send_file("jobs.csv")
  except:
    return redirect('/')


app.run(host="0.0.0.0")

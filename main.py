from flask import Flask, render_template, request, redirect
from scrapper import start_scrap as scrap
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


app.run(host="0.0.0.0")

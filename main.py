from indeed import extract_indeed_pages, extract_indeed_jobs
from stackoverflow import extract_stackoverflow_jobs
from save import save_to_csv
from flask import Flask, render_template

app = Flask("job scrapper")


@app.route('/')
def index():
  return render_template("home.html")


@app.route('/<username>')
def contact(username):
  return f"Hello Nice to meet you {username}"


app.run(host="0.0.0.0")

# last_indeed_page = extract_indeed_pages()
# indeed_jobs = extract_indeed_jobs(last_indeed_page)

# stackoverflow_jobs = extract_stackoverflow_jobs()

# jobs = indeed_jobs + stackoverflow_jobs
# save_to_csv(jobs)

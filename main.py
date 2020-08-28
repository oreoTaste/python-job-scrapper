from indeed import extract_indeed_pages, extract_indeed_jobs
from stackoverflow import extract_stackoverflow_jobs
from save import save_to_csv

last_indeed_page = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_indeed_page)

stackoverflow_jobs = extract_stackoverflow_jobs()

jobs = indeed_jobs + stackoverflow_jobs
save_to_csv(jobs)

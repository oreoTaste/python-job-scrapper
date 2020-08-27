from indeed import extract_indeed_pages, extract_indeed_jobs
import stackoverflow

last_indeed_page = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_indeed_page)

last_stackoverflow_page = stackoverflow.extract_stackoverflow_pages()
stackoverflow_jobs = stackoverflow.extract_stackoverflow_jobs(last_stackoverflow_page)

jobs = indeed_jobs + stackoverflow_jobs

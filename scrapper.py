from indeed import extract_indeed_jobs
from stackoverflow import extract_stackoverflow_jobs
from save import save_to_csv


def start_scrap(lan):
  indeed_jobs = extract_indeed_jobs(lan)
  stackoverflow_jobs = extract_stackoverflow_jobs(lan)

  jobs = indeed_jobs + stackoverflow_jobs
  return jobs

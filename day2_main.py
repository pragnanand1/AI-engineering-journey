import job_utils

job = {
    "title": "AI Engineer",
    "required_skill": "Java",
    "required_experience" : 0
}

candidate = {
    "skills": ["Python", "SQL", "Git"],
    "Experience" : 1
}

print(job_utils.is_job_match(candidate, "Python", 0))
print(job_utils.is_job_match(candidate, "Java", 0))
      





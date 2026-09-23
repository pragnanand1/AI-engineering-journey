jobs = [
    {
        "title": "Python Developer",
        "skills": ["Python", "SQL"],
        "experience": 0
    },
    {
        "title": "Java Developer",
        "skills": ["Java", "SQL"],
        "experience": 1
    },
    {
        "title": "AI Engineer",
        "skills": ["Python", "PyTorch"],
        "experience": 0
    }
]

required_skill = "Python"
matching_jobs = []
for job in jobs:
    if required_skill in job["skills"] and job["experience"] == 0:
        matching_jobs.append(job["title"])

for job in matching_jobs:
    print(job)
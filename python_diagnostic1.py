name = "pragnanand"
age = 22
cgpa = 9.49
skills = ["python", "java", "SQL", "git", "Machine Learning"]

print(name,age,cgpa,skills)

print(len(skills))

for number, skill in enumerate(skills, start=1):
    print(number, skill)
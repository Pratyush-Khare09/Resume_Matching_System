from src.preprocess import clean_text
from src.similarity import calculate_similarity
from src.skill_matcher import compare_skills

# read files
with open("data/sample_resume.txt", "r") as f:
    resume = f.read()

with open("data/sample_job_description.txt", "r") as f:
    job_description = f.read()

# preprocess
clean_resume = clean_text(resume)
clean_jd = clean_text(job_description)

# similarity score
score = calculate_similarity(clean_resume, clean_jd)

# skill matching
matched, missing = compare_skills(clean_resume, clean_jd)

# output
print("\nResume–Job Description Matching System")
print("--------------------------------------")

print(f"\nMatch Score: {score}%")

print("\nMatched Skills:")
for skill in matched:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing:
    print("-", skill)

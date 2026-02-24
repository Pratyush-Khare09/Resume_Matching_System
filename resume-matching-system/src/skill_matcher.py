def extract_skills(text):

    skills_list = [
        "python", "java", "sql", "html", "css",
        "machine learning", "data analysis",
        "deep learning", "statistics",
        "pandas", "numpy"
    ]

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def compare_skills(resume, job_description):

    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job_description)

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    return matched, missing

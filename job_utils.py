def is_skill_match(candidate, required_skill):
    return required_skill in candidate["skills"]

def is_experience_match(candidate, required_experience):
    return candidate["Experience"] >= required_experience

def is_job_match(candidate: dict, required_skill : str, required_experience: int) -> bool:

    """Check whether a candidate matches the required skill and experience"""

    if not is_skill_match(candidate, required_skill):
        return False
    
    if not is_experience_match(candidate, required_experience):
        return False

    return True

def get_match_message(candidate, required_skill, required_experience):
    if is_job_match(candidate, required_skill, required_experience):
        return "Candidate matches the job requirements"
    else:
        return "Candidate does not match the job requirements"

def is_major(candidate):
    return True

if __name__ == "__main__":
    print("i'm running directly!")
        
def filter_by_location(job_postings, location):
    """
    Returns all jobs within a list of job_postings that are located in the desired location.

    Args:
        job_postings (list (of dictionaries)): list of dictionaries. Dictionaries composition:
            "title": title (str)
            "location": location (str)
        location (str): city where job is located
    
    Returns
        list: of jobs located in specific city
    """
    return list(filter(lambda job: location in job["location"], job_postings))
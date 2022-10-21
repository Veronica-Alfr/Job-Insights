from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    data_filter_types = set()
    for row in file:
        types = row["job_type"]
        data_filter_types.add(types)
    return data_filter_types


def filter_by_job_type(jobs, job_type):
    all_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            all_jobs.append(job)
    return all_jobs


def get_unique_industries(path):
    file = read(path)
    data_filter_industry = set()
    for row in file:
        industries = row["industry"]
        if industries != "":
            data_filter_industry.add(industries)
    return data_filter_industry


def filter_by_industry(jobs, industry):
    all_industries = []
    for job in jobs:
        if job["industry"] == industry:
            all_industries.append(job)
    return all_industries


def get_max_salary(path):
    file = read(path)
    data_filter_max_salary = set()
    for row in file:
        max_salary = row["max_salary"]
        if max_salary != "" and max_salary.isdigit():
            data_filter_max_salary.add(int(max_salary))
    return max(data_filter_max_salary)


def get_min_salary(path):
    file = read(path)
    data_filter_min_salary = set()
    for row in file:
        min_salary = row["min_salary"]
        if min_salary != "" and min_salary.isdigit():
            data_filter_min_salary.add(int(min_salary))
    return min(data_filter_min_salary)


def matches_salary_range(job, salary):
    if not type(salary) is int:
        raise ValueError("Only integers salaries are allowed")
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary is not in job")
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("min_salary or max_salary is not integer")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary can't be greather than max_salary")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_based_on_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_based_on_salary.append(job)
        except ValueError:
            print("Salary is not passed")
    return jobs_based_on_salary

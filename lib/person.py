#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    APPROVED_JOBS = ["ITC", "Sales"]

    def __init__(self, name=None, job=None):

        if name is not None:
            self.name = self._validate_name(name)
        else:
            self.name = None

        if job is not None:
            self.job = self._validate_job(job)
        else:
            self.job = None

    def _validate_name(self, name):

        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
            return None
        elif len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return None
        else:
            return name.title()

    def _validate_job(self, job):

        if job not in self.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return None
        else:
            return job
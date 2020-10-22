"""
CP1404 Practical - Guitar Class
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        age = 2020 - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50

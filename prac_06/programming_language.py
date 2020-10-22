"""CP1404 Practicals - Programming Language"""


class ProgrammingLanguage:
    """Store information about a programming language"""
    def __init__(self, name, typing, reflection, year):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True

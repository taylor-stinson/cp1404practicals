"""
CP1404 Practical - Guitars
"""
from prac_06.guitar import Guitar


def main():
    guitars = get_guitars()
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost}{vintage_string}")


def get_guitars():
    guitars = []
    name = str(input("Name: "))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        print(f"{new_guitar} added.")
        guitars.append(new_guitar)
        name = str(input("Name: "))
    return guitars


main()

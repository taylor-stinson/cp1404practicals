"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    rank = determine_rank(score)
    print(rank)
    import random
    score = random.randrange(1, 101, 1)
    rank = determine_rank(score)
    print(rank)


def determine_rank(score):
    if score < 50:
        rank = "Bad"
    elif score < 90:
        rank = "Passable"
    else:
        rank = "Excellent"
    return rank


main()

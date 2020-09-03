""""
CP1404- Practical 4
Quick Picks
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks?: "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(6):
            number = random.randint(1, 45)
            while number in quick_pick:
                number = random.randint(1, 45)
            quick_pick.append(number)
        quick_pick.sort()
        print(quick_pick)


main()

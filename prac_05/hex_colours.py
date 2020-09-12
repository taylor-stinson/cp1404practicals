"""
CP1404 - Practical 5
Hex Colours Dictionary
"""

NAME_TO_CODE = {"SKYBLUE": "#87ceeb", "THISTLE": "#d8bfd8", "HONEYDEW1": "#f0fff0", "DARKORCHID": "#9932cc",
                "CORNFLOWERBLUE": "#6495ed", "CORAL": "#ff7f50", "BURLYWOOD": "#deb887", "GREY": "#bebebe",
                "LIGHTBLUE": "#add8e6", "LIGHTSEAGREEN": "#20b2aa"}
print(NAME_TO_CODE)

colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(colour_name, "is", NAME_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()

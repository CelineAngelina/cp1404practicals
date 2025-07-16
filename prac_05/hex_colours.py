COLOUR_TO_CODE = {"Baby Pink": "#f4c2c2", "Aureolin": "#fdee00", "Celadon": "#ace1af", "Dark Orchid": "#9932cc",
                "French Sky Blue": "#77b5fe", "Imperial Red": "#ed2939", "Mango": "#fdbe02", "Persian Blue": "#1c39bb",
                "Pumpkin": "#ff7518", "Rocket Metallic": "#8a7f80"}
print(COLOUR_TO_CODE)
colours = []

colour_name = input("Enter the colour name: ").title()
while colour_name != "":
    try:
        colours.append((colour_name, COLOUR_TO_CODE[colour_name]))
    except KeyError:
        print("Invalid colour")
    colour_name = input("Enter the colour name: ").title()
name_width = max((len(pair[0]) for pair in colours))
print()
for colour, code in colours:
    print(f"{colour:{name_width}} code is {code}")
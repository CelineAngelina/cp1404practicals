CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)
states = []

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        states.append((state_code, CODE_TO_NAME[state_code]))
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
print()
for code, name in states:
    print(f"{code:3} is {name}")
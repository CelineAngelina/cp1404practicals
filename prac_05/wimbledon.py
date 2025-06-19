"""
Wimbledon
Estimate: 60 minutes
Actual:    minutes
start 12:08
"""
import csv

def main ():
    filename = "wimbledon.csv"
    champion_to_count = {}
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            name = record[2]
            if name in champion_to_count:
                champion_to_count[name] += 1
            else:
                champion_to_count[name] = 1

    name_width = max((len(name) for name in champion_to_count))

    for name, count in champion_to_count.items():
        print(f"{name:{name_width}} {count}")


main()
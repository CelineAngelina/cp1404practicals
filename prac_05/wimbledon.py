"""
Wimbledon
Estimate: 60 minutes
Actual:    minutes
start 12:08
"""
import csv

def main ():
    filename = "wimbledon.csv"
    champion_to_count = load_champion_count(filename)
    display_champion_name_and_count(champion_to_count)

def load_champion_count(filename):
    """Load Wimbledon champion data from a CSV file and count the number of wins per champion."""
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
    return champion_to_count

def display_champion_name_and_count(champion_to_count):
    """Display the champions and their win count, neatly aligned."""
    name_width = max((len(name) for name in champion_to_count))
    for name, count in champion_to_count.items():
        print(f"{name:{name_width}} {count}")

main()
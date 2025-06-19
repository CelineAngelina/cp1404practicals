"""
Wimbledon
Estimate: 60 minutes
Actual:  102 minutes
"""
import csv

def main():
    """Read Wimbledon data and display champion win counts and countries."""
    filename = "wimbledon.csv"
    champion_to_count, countries = load_wimbledon_data(filename)
    display_champions_count(champion_to_count)
    print()
    display_champion_country(countries)

def load_wimbledon_data(filename):
    """Load Wimbledon champion data from a CSV file."""
    champion_to_count = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            name = record[2]
            if name in champion_to_count:
                champion_to_count[name] += 1
            else:
                champion_to_count[name] = 1

            country = record[1]
            countries.add(country)
    return champion_to_count, countries

def display_champions_count(champion_to_count):
    """Display the champions and their win count, neatly aligned."""
    name_width = max((len(name) for name in champion_to_count))
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(f"{name:{name_width}} {count}")

def display_champion_country(countries):
    """Display the countries of the champions in alphabetical order."""
    print(f"These {len(countries)} countries have won Wimbledon:\n{", ".join(sorted(countries))}")

main()
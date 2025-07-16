from prac_07.guitar import Guitar

def main():
    """Load existing guitars, allow addition of new guitars data and display all guitars sorted by year."""
    guitars = []
    load_guitar_data(guitars)
    write_new_guitar_data(guitars)
    guitars.sort()
    print()
    for guitar in guitars:
        print(guitar)

def load_guitar_data(guitars):
    """Read guitar data from CSV file."""
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], float(parts[2]))
            guitars.append(guitar)

def get_valid_year():
    """Get new guitar's year by ensuring it is integer."""
    new_guitar_year = input("Year: ")
    while not new_guitar_year.isdigit():
        print("Invalid year")
        new_guitar_year = input("Year: ")
    return new_guitar_year

def write_new_guitar_data(guitars):
    """Write new guitars data to CSV file."""
    with open("guitars.csv", 'a') as out_file:
        new_guitar_name = input("Name: ").title()
        while new_guitar_name != "":
            new_guitar_year = get_valid_year()
            new_guitar_cost = float(input("Cost: $"))
            new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
            guitars.append(new_guitar)
            out_file.write(f"{new_guitar.name},{new_guitar.year},{new_guitar.cost}\n")
            new_guitar_name = input("Name: ").title()


main()
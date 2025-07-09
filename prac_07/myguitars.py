from prac_07.guitar import Guitar


def main():
    """"""
    guitars = []
    load_guitar_data(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def load_guitar_data(guitars):
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
    in_file.close()


main()
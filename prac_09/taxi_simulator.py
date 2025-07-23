from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    trip_fare = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_fare:,.2f}")
                    bill_to_date += trip_fare
                except ValueError:
                    print("Enter valid number.")
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:,.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:,.2f}")
    print("Taxis are now:")
    display_taxi(taxis)

def display_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
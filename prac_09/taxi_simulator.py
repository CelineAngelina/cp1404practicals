from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
bill_to_date = 0
current_taxi = None

print("Let's drive!")
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
choice = input(">>> ").lower()
while choice != "q":
    if choice == "c":
        print("Taxis available:")
        for i, taxi in enumerate(taxis):
            print(f"{i} - {taxi}")
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice >= len(taxis):
            print("Invalid taxi choice")
        else:
            current_taxi = taxis[taxi_choice]

    elif choice == "d":
        if current_taxi:
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            trip_fare = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${trip_fare:,.2f}")
            bill_to_date += trip_fare
        else:
            print("You need to choose a taxi before you can drive")

    else:
        print("Invalid option")
    print(f"Bill to date: ${bill_to_date:,.2f}")
    print(MENU)
    choice = input(">>> ").lower()

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

print("Let's drive!")
MENU = "q)uit, c)hoose taxi, d)rive"
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
choice = input(">>> ").lower()
while choice != "":
    if choice == "c":
        print("Taxis available:")
        for i, taxi in enumerate(taxis):
            print(f"{i} - {taxi}")
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice >= len(taxis):
            print("Invalid taxi choice")

    elif choice == "d":
        pass
    elif choice == "q":
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").lower()

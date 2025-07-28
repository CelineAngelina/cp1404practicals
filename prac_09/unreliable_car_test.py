from prac_09.unreliable_car import UnreliableCar

low_reliability_car = UnreliableCar("LowReliability", 100, 30)
high_reliability_car = UnreliableCar("HighReliability", 100, 90)

for i in range(1, 11):
    print(f"\n--- Attempt {i} ---")
    print(f"{low_reliability_car.name} drove {low_reliability_car.drive(i)} km.")
    print(f"{high_reliability_car.name} drove {high_reliability_car.drive(i)} km.")

print("\n--- Final Status ---")
print(low_reliability_car)
print(high_reliability_car)
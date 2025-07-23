from prac_09.silver_service_taxi import SilverServiceTaxi

silver_taxi1 = SilverServiceTaxi("Hummer", 200, 2)
silver_taxi1.drive(18)

fare = silver_taxi1.get_fare()
assert abs(fare) == 48.78, f"Expected $48.78, but got ${fare:.2f}"

print(silver_taxi1)
print(f"${fare}")
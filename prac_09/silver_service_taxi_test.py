from prac_09.silver_service_taxi import SilverServiceTaxi

silver_taxi1 = SilverServiceTaxi("Hummer", 200, 2)
silver_taxi1.drive(18)
print(silver_taxi1)
print(f"${silver_taxi1.get_fare()}")
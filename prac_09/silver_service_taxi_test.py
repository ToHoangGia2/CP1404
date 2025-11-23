from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxi1 = SilverServiceTaxi("Taxi1", 1000, 2)
    taxi1.drive(18)
    print(taxi1)
    print(taxi1.get_fare())

if __name__ == '__main__':
    main()
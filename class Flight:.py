flight_data = {
    "AI161E90": ("BLR", "BOM", 5600),
    "BR161F91": ("BOM", "BBI", 6750),
    "AI161F99": ("BBI", "BLR", 8210),
    "VS171E20": ("JLR", "BBI", 5500),
    "AS171G30": ("HYD", "JLR", 4400),
    "AI131F49": ("HYD", "BOM", 3499)
}

city_codes = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur"
}

def get_flight_details(flight_id=None, source_city=None, dest_city=None):
    if flight_id:
        if flight_id in flight_data:
            source, dest, price = flight_data[flight_id]
            print(f"Flight ID: {flight_id}")
            print(f"Source: {city_codes[source]}")
            print(f"Destination: {city_codes[dest]}")
            print(f"Price: {price}")
        else:
            print("Flight not found.")
    elif source_city:
        matching_flights = [(fid, source, dest, price) for fid, (source, dest, price) in flight_data.items() if source == source_city]
        if matching_flights:
            print("Flights from", city_codes[source_city])
            for fid, source, dest, price in matching_flights:
                print(f"Flight ID: {fid}")
                print(f"Destination: {city_codes[dest]}")
                print(f"Price: {price}")
        else:
            print("No flights found from", city_codes[source_city])
    elif dest_city:
        matching_flights = [(fid, source, dest, price) for fid, (source, dest, price) in flight_data.items() if dest == dest_city]
        if matching_flights:
            print("Flights to", city_codes[dest_city])
            for fid, source, dest, price in matching_flights:
                print(f"Flight ID: {fid}")
                print(f"Source: {city_codes[source]}")
                print(f"Price: {price}")
        else:
            print("No flights found to", city_codes[dest_city])
    else:
        print("Please provide valid input.")

user_input_type = int(input("Enter 1 for Flight ID, 2 for source city, or 3 for destination city: "))
if user_input_type == 1:
    flight_id = input("Enter Flight ID: ")
    get_flight_details(flight_id=flight_id)
elif user_input_type == 2:
    source_city = input("Enter source city: ")
    get_flight_details(source_city=source_city)
elif user_input_type == 3:
    dest_city = input("Enter destination city: ")
    get_flight_details(dest_city=dest_city)
else:
    print("Invalid input type.")
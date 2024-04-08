class Bus:
    city_name = 'Los Angeles'
    bus_fare = 2.50
    def __init__(self, route_num, capacity):
        self.route_number= route_num
        self.capacity = capacity


bus1 = Bus(7, 50)
print(f'Bus Route number: {bus1.route_number}, can hold a capacity of {bus1.capacity}, has a fare 0f ${bus1.bus_fare} in {bus1.city_name}')
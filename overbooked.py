class Flight():
    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight:
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
# Flight with 0 to 60 passengers:
flight = Flight(60)

# List of People
people = ["Seinfeld", "Larry", "Elaine", "George", "Superman"]

# Add person in the list to a flight
for person in people:
    if flight.add_passenger(person):
        print(f"{person} addto flight successfully")
    else:
        print(f"No available seats for {person}")
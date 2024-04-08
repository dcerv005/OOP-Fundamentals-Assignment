#Question 1
#Task 1


class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        
    def update_owner(self, new_owner):
        self.owner = new_owner
        return f"Registration number: {self.registration_number}, type: {self.type}, owner: {new_owner}"
        
Vehicle_reg=Vehicle(1, 'sedan', 'Greg')


print(Vehicle_reg.update_owner('David'))
print(Vehicle_reg.update_owner('Coding Temple'))

#Task 2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.counter = 0
    def add_participant(self):
        self.counter += 1


    def get_participant_count(self):
        return self.counter

event1 = Event('Coding Event', 4/7/2024)
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()

print(event1.get_participant_count())
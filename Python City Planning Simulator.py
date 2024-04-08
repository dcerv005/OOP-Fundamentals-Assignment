#Question 2
class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def savingto_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f'Building: {self.name} has {self.floors} floor(s)')

    def loadingfrom_file(filename):
        with open(filename, 'r') as file:
            content = file.read()
            return content

building1 = Building('Costco', 2)
#building1.savingto_file('building_file.txt')
building2 = Building.loadingfrom_file('building_file.txt')
print(building2)

class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors and new_floor >= 1:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('There is not such a floor.')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h2.go_to(0)
h1.go_to(-1)
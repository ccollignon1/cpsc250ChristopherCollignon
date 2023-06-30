class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')


class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')
        print(f'   Annual: {self.is_annual}')
        print(f'   Color of flowers: {self.color_of_flowers}')


def print_list():
    count = 0
    for plant in my_garden:
        count += 1
        print("Plant", count, "Information:")
        plant.print_info()
        print()


# TODO:  Define the print_list() function that prints a list of plant (or flower) objects

if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []
    user_string = input()
    while user_string != '-1':
        if "plant" in user_string:
            vals = user_string.split()
            plant = Plant(vals[1], vals[2])
            my_garden.append(plant)
        else:
            vals = user_string.split()
            flower = Flower(vals[1], vals[2], vals[3], vals[4])
            my_garden.append(flower)
        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        user_string = input()

    # TODO: Call the print_list() function to print my_garden
    print_list()
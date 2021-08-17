import random  # from random import randint (вызов - randint(2,5))
import math


class Car:
    """Use as template for creating cars"""
    cost_car = 10000

    def __init__(self, type_enj: str, tank_val: int):
        assert tank_val in (60, 75), 'Incorrect value fuels tank (tank_val)'  # проверка
        self.kmage = random.randint(55000, 286000)
        self.tank_val = tank_val
        self.type_enj = type_enj
        if type_enj == 'diesel':
            self.amort = 105
            self.cost_rep = 700
            self.fuel_rate = 6 / 100
            self.kmage_rep = 150000
            self.fuel_cost = 1.8
        elif type_enj == 'petrol':
            self.amort = 95
            self.cost_rep = 500
            self.fuel_rate = 8 / 100
            self.kmage_rep = 100000
            self.fuel_cost = 2.4
        else:  # лучше через assert
            x = 5 / 0
            print('Incorrect type engine (type_enj)')
        """
        :param type_enj: str, type of engine in the car   (pep 257)
        :param tank_val: int, tank's value in the car 
        """

    def balance(self) -> float:
        """
        Use for calculated balance cost car
        :return: car cost after kmage
        """
        balance_cost = Car.cost_car - (self.kmage / 1000) * self.amort
        return balance_cost

    def cost_fuel(self) -> float:
        """
        Use for calculated cost of fuel for entire kmage
        :return: cost of fuel for entire kmage
        """
        num = self.kmage // 1000
        iter_fuel_rate = self.fuel_rate
        iter_fuel_quan = 0
        for i in range(num):
            iter_fuel_quan += iter_fuel_rate * 1000
            iter_fuel_rate = iter_fuel_rate * 1.01
        full_cost = (iter_fuel_quan + (self.kmage % 1000) * (iter_fuel_rate / 1.01)) * self.fuel_cost
        return full_cost

    def refueling(self) -> int:
        """
        Use for calculated quantity of refuel for entire kmage
        :return: quantity of refuel for entire kmage
        """
        num = self.kmage // 1000
        iter_fuel_rate = self.fuel_rate
        iter_fuel_quan = 0
        for i in range(num):
            iter_fuel_quan += iter_fuel_rate * 1000
            iter_fuel_rate = iter_fuel_rate * 1.01
        num_refuel = math.ceil((iter_fuel_quan + (self.kmage % 1000) * (iter_fuel_rate / 1.01)) / self.tank_val)
        return num_refuel

    def utilization(self) -> float:
        """
        Use for calculated kmage to utilization (cost of car = 0)
        :return: kmage to utilization
        """
        if Car.balance(self) <= 0:
            return 0
        else:
            x = Car.balance(self) / self.amort * 1000
            return x


class Factory:
    """Use for creating car's park"""

    def __init__(self, quan_cars: int):

        self.quan_cars = quan_cars
        self.all_cars = Factory.create_car(self)  # передаем наш лист с машинами creat_car в экземпляр класса
        """
        :param quan_cars: quantity of cars will be created
        """

    def create_car(self) -> list:  # ожидаем список
        """
        Gets parameters of the car and make car depending on the car number
        :return:list of object class Car
        """
        quan_cars1 = self.quan_cars
        all_cars = []
        for i in range(quan_cars1):
            if (i + 1) % 3 == 0:
                type_enj = 'diesel'
            else:
                type_enj = 'petrol'
            if (i + 1) % 5 == 0:
                tank_val = 75
            else:
                tank_val = 60
            all_cars.append(Car(type_enj, tank_val))
        return all_cars


if __name__ == '__main__':  # далее инструкции будут выполнены если модуль не импортирован а запущен как main
    cars_park = Factory(6)  # создаем экземпляр, внутри которого лежит наш лист под именем all_cars

    diesel_cars = []
    petrol_cars = []
    for i in cars_park.all_cars:
        if i.type_enj == 'diesel':
            diesel_cars.append(i)
        else:
            petrol_cars.append(i)

    print(cars_park.all_cars)
    print(diesel_cars)
    print(petrol_cars)
import random
cars = dict()

class Car:
    """Use as template for creating cars"""
    cost_car = 10000

    def __init__(self,type_enj,tank_val):
        assert tank_val in (60, 75), 'Incorrect value fuels tank (tank_val)'   # проверка
        self.kmage=random.randint(55000, 286000)
        self.tank_val=tank_val
        self.type_enj=type_enj
        if type_enj == 'diesel':
            self.amort=105; self.cost_rep = 700; self.fuel_rate = 6 / 100; self.kmage_rep = 150000; self.fuel_cost = 1.8
        elif type_enj == 'petrol':
            self.amort=95; self.cost_rep = 500; self.fuel_rate = 8 / 100; self.kmage_rep = 100000; self.fuel_cost = 2.4
        else:                                                                  # или лучше через assert?
            x=5/0
            print ('Incorrect type engine (type_enj)')
        """
        :param type_enj: str, type of engine in the car   (pep 257)
        :param tank_val: int, tank's value in the car 
        """

    def balance(self):
        """
        Use for calculated balance cost car
        :return: car cost after kmage
        """
        balance_cost = Car.cost_car-(self.kmage/1000)*self.amort
        return balance_cost

    def cost_fuel(self):
        """
        Use for calculated cost of fuel for entire kmage
        :return: cost of fuel for entire kmage
        """
        num = self.kmage//1000
        iter_fuel_rate = self.fuel_rate
        iter_fuel_quan=0
        for i in range(num):
            iter_fuel_quan+=iter_fuel_rate*1000
            iter_fuel_rate=iter_fuel_rate*1.01
        used_fuel=iter_fuel_quan+(self.kmage%1000)*(iter_fuel_rate/1.01)
        full_cost=used_fuel*self.fuel_cost
        return full_cost

    def refueling(self):
        """
        Use for calculated quantity of refuel for entire kmage
        :return: quantity of refuel for entire kmage
        """
        num_refuel=Car.cost_fuel.used_fuel/self.tank_val
        return num_refuel

    def utilization(self):
        """
        Use for calculated kmage to utilization (cost of car = 0)
        :return: kmage to utilization
        """



class factory:
    """Use for creating car's park"""
    def __init__(self, quan_cars):
        self.quan_cars = quan_cars
        for i in range(quan_cars):
            if (i+1) % 3 == 0:
                type_enj = 'diesel'
            else:
                type_enj = 'petrol'
            if (i+1) % 5==0:
                tank_val=75
            else:
                tank_val=60
            cars[i + 1] = Car(type_enj, tank_val)
        """
        :param quan_cars: int, how much cars will be in car's park
        """


car1=Car('diesel',60)
print(car1.kmage, car1.cost_fuel(), car1.balance())



# class Car:

#     vehicle = '4-wheeler'

#     def __init__(self, brand) -> None:
#         self.brand = brand

#     def get_brand(self):
#         # self.vehicle = '6-wheeler'
#         print(self.vehicle)

#     @classmethod
#     def vehicle_type(cls):
#         cls.vehicle = '6-wheeler'

#     @staticmethod
#     def utils():
#         pass


# tata = Car('Tata')
# # print(dir(car))
# tata.get_brand()
# bmw = Car('Bmw')
# bmw.get_brand()
# Car.vehicle_type()

# print(tata.__dict__)


# class Bank:

#     limit = 50000

#     def __init__(self, name) -> None:
#         self.name = name

#     def deposit(self):
#         Bank.interst_calc()

#     def withdraw(self):
#         pass

#     @classmethod
#     def set_limit(cls, limit):
#         cls.limit = limit

#     @classmethod
#     def create_bank(cls):
#         return cls('icici')
    
#     @staticmethod
#     def interst_calc():
#         pass


# sbi = Bank('sbi')
# cbi = Bank('cbi')
# Bank.set_limit(100000)
# icici = Bank.create_bank()

class Vehicle:
    brand_name = 'BMW'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_price(cls, name, price):
        # ind_price = dollar * 76
        # create new Vehicle object
        print(cls)
        return cls(name, (price * 75))

    def show(self):
        print(self.name, self.price)

class Car(Vehicle):
    def average(self, distance, fuel_used):
        mileage = distance / fuel_used
        print(self.name, 'Mileage', mileage)

# bmw_us = Car('BMW X5', 65000)
# bmw_us.show()

# class method of parent class is available to child class
# this will return the object of calling class
bmw_ind = Car.from_price('BMW X5', 65000)
bmw_ind.show()

# check type
# print(type(bmw_ind))
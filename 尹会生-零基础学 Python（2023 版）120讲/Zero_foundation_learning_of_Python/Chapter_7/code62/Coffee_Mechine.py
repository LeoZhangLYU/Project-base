class WaterMixin(object):
    def __init__(self):
        self.temperature = None
        self.volume = 0

    def add_water(self, nums, temp):
        self.volume = nums
        if temp == "hot":
            self.temperature = "hot"
        elif temp == "cold":
            self.temperature = "cold"

        return f"add {self.temperature} water {self.volume} ML"


class CoffeeMixin(object):
    def __init__(self):
        self.numbers = 0

    def add_coffee(self, nums):
        self.numbers = nums
        return f"add coffee {self.numbers} part"


class MilkMixin(object):
    def __init__(self):
        self.temperature = None
        self.volume = 0

    def add_milk(self, nums, temp):
        self.volume = nums
        if temp == "hot":
            self.temperature = "hot"
        elif temp == "cold":
            self.temperature = "cold"

        return f"add {self.temperature} milk {self.volume} ML"


class Coffee(WaterMixin, CoffeeMixin, MilkMixin):
    def __init__(self, water=-1, water_temp="cold", milk=-1, milk_temp="cold", coffee=-1):
        self.water = water
        self.water_temp = water_temp
        self.milk = milk
        self.milk_temp = milk_temp
        self.coffee = coffee
        self.prescription = []

        if int(self.water) > 0:
            self.prescription.append(super().add_water(water, water_temp))

        if int(self.milk) > 0:
            self.prescription.append(super().add_milk(milk, milk_temp))

        if int(self.coffee) > 0:
            self.prescription.append(super().add_coffee(self.coffee))

    def show_prescription(self):
        for prescription in self.prescription:
            print(prescription)


americano = Coffee(water=150, water_temp="cold", coffee=1)
americano.show_prescription()

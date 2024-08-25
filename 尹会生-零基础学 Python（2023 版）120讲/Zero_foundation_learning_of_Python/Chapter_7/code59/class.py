class Coffee(object):
    water = 0
    milk = 0

    def add_water(self):
        self.water += 1

    def add_hot_milk(self):
        self.hot_milk = 10


mocha = Coffee()
mocha.add_water()
print(mocha.water)
# 不推荐
mocha.add_hot_milk()
print(mocha.hot_milk)

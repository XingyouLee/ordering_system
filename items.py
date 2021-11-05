class Item(object):

    def __init__(self, name, price, water, coco, milk, sugar, cheese):
        self.name = name
        self.price = price
        self.water = water
        self.coco = coco
        self.milk = milk
        self.sugar = sugar
        self.cheese = cheese


class Storage(object):

    def __init__(self, water, coco, milk, sugar, cheese):
        self.water = water
        self.coco = coco
        self.milk = milk
        self.sugar = sugar
        self.cheese = cheese

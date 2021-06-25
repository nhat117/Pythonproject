class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")
    def make_salad(self):
        print("The chef makes a salad")
    def make_special_dish(self):
        print("The chef is making a special dish")

class ChineseChef (Chef):
    # Overwrite stuff
    def make_special_dish(self):
        print("Make Orange BBQ Dish")
    def make_chinese_dish(self):
        print("Make Chinese Dish")

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
import random


class Dice:
    """This is a simple dice - number of sides - number of dices - number of rolls"""

    def __init__(self):
        self.sides = None
        self.dices = None
        self.rolls = None

    def ask_user(self):
        """let the user pick the attributes of the dice"""
        while True:
            try:
                self.sides = int(input("Enter the number of sides: "))
                break
            except ValueError:
                print("Enter Sides.")
        while True:
            try:
                self.dices = int(input("Enter the number of dices: "))
                break
            except ValueError:
                print("Enter Dices.")
        while True:
            try:
                self.rolls = int(input("Enter the number of rolls: "))
                break
            except ValueError:
                print("Enter Rolls.")
        self.roll_dice()

    def roll_dice(self):
        sides_list = list(range(1, self.sides + 1))
        for i in range(1, self.rolls + 1):
            # rolled_num = random.choice(sides_list)
            # print(f"Roll {i}: {rolled_num}")
            rolled_nums = random.choices(sides_list, k=self.dices)
            summa_summarum = sum(rolled_nums)
            print(f"Roll {i}: {rolled_nums} - sum: {summa_summarum} - Roll {i}")


dice_6 = Dice()
dice_6.ask_user()

def check_balance(amount):
    return "This is the balance."


class Category:

    # constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def withdraw(self, amount) -> object:
        self.amount -= amount
        return "You have successfully withdrawn {} from {} category".format(amount, self.category)

    def transfer(self, amount, category):
        # transfer between categories
        return self.withdraw(amount) + '' + category.deposit(amount)


food_category = Category("Food", 200)
clothing_category = Category("Clothing", 100)
utilities_category = Category("Utilities", 200)
rent_category = Category("Rent", 500)
entertainment_category = Category("Entertainment", 60)

print(food_category.withdraw(20))
print(food_category.budget_balance())
print(clothing_category.transfer(50, entertainment_category))
print(clothing_category.budget_balance())
print(entertainment_category.budget_balance())
print(utilities_category.deposit(50))
print(utilities_category.budget_balance())

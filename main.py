class GasPump:
    def __init__(self, initial_gas, price_per_liter):
        self.max_capacity = 5000
        self.available_gas = min(initial_gas, self.max_capacity)
        self.price_per_liter = price_per_liter

    def add_gas(self, amount):
        available_space = self.max_capacity - self.available_gas
        if amount > available_space:
            self.available_gas = self.max_capacity
            print(f"Cannot add {amount} liters. Pump is full.")
        else:
            self.available_gas += amount
            print(f"Added {amount} liters. Total gas supply: {self.available_gas} liters.")

    def sell_gas(self, amount):
        available_sale = min(amount, self.available_gas)
        cost = available_sale * self.price_per_liter
        self.available_gas -= available_sale
        return cost

shell = GasPump(3000, 0.785)
amount_to_sell = float(input("How much gas do you want to buy (in liters)? "))
cost = shell.sell_gas(amount_to_sell)
print(f"Sold {amount_to_sell} liters for {cost:.2f} dollars.")
shell.add_gas(500)
print(f"Gas supply left: {shell.available_gas} liters.")

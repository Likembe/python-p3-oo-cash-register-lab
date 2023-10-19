#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
       self.discount = discount
       self.total = 0
       self.items = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = 0
            for i in reversed(range(len(self.items))):
                if self.items[i] == self.items[-1]:
                    last_item_price = self.total
                    self.items.pop()
                else:
                    break
            self.total = last_item_price
  
    

""" CardHolder class

Write a python class of CardHolder. It should initialize a (bank) card holder's name and balance.

Also, it should have functions for checking balance, and withdrawing and depositing a given amount.
"""


class CardHolder(object):
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def balance_check(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

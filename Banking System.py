from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def create_account(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposits(self):
        return 0

    @abstractmethod
    def display_balance(self):
        return 0


class SavingsAccount:

    def __init__(self):
        self.savingsAccount = {}

    def create_account(self, name, deposits):
        self.account_number = randint(10000, 99999)
        self.savingsAccount[self.account_number] = [name, deposits]
        print(f"Hello {name} your Account  has been successfully created. your account number is: ", self.account_number)

    def authenticate(self, name, account_number):
        if account_number in self.savingsAccount.keys():
            if self.savingsAccount[account_number][0] == name:
                print("Authentication Successful")
                self.account_number = account_number
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.savingsAccount[self.account_number][1]:
            print("Insufficient amount")
        else:
            self.savingsAccount[self.account_number][1] -= withdraw_amount
            print("withdraw wsa successful.")
            self.display_balance()

    def deposits(self, deposit_amount):
        self.savingsAccount[self.account_number][1] += deposit_amount
        print("Deposit was successful.")
        self.display_balance()

    def display_balance(self):
        print("Your Available balance is: ", self.savingsAccount[self.account_number][1])


saving_account = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("enter 3 to exit")
    user_choice = int(input())
    if user_choice == 1:
        print("Enter your name:")
        name = input()
        print("Enter the initial deposits")
        deposits = int(input())
        saving_account.create_account(name, deposits)
    elif user_choice == 2:
        print("Enter your name:")
        name = input()
        print("Enter your account number:")
        account_number = int(input())
        authentication_status = saving_account.authenticate(name, account_number)
        if authentication_status is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menu")
                user_choice = int(input())
                if user_choice == 1:
                    print("Enter withdraw amount ")
                    withdraw_amount = int(input())
                    saving_account.withdraw(withdraw_amount)
                elif user_choice == 2:
                    print("Enter  an amount to be deposited")
                    deposit_amount = int(input())
                    saving_account.deposits(deposit_amount)
                elif user_choice == 3:
                    saving_account.display_balance()
                elif user_choice == 4:
                    break

    elif user_choice == 3:
        quit()

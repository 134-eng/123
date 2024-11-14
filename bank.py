class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} грн додано до рахунку {self.account_number}.баланс: {self.balance} грн.")
        else:
            print("сума поповнення повинна бути більша за нуль")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{amount} грн знято з рахунку {self.account_number}.баланс: {self.balance} грн.")
            else:
                print("нехватає коштів для зняття.")
        else:
            print("сума зняття повинна бути більша за нуль")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"рахунок {account.account_number} додано для {account.owner_name}.")

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            from_account = self.accounts[from_account_number]
            to_account = self.accounts[to_account_number]

            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"переказ {amount} грн з рахунку {from_account_number} на рахунок {to_account_number} завершено.")

account1 = BankAccount("1", "0000", 1000)
account2 = BankAccount("2", "1111", 500)

bank = Bank()
bank.add_account(account1)
bank.add_account(account2)

account1.deposit(200)
account1.withdraw(150)
bank.transfer("0000", "1111", 300)

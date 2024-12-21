class BankAccount:
    def init(self, owner_name, account_number, balance=0.0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def str(self):
        return f"Рахунок №{self.account_number}, Власник: {self.owner_name}, Баланс: {self.balance} грн."


class Bank:
    def init(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        if from_account and to_account and from_account.balance >= amount > 0:
            from_account.withdraw(amount)
            to_account.deposit(amount)

    def str(self):
        return "\n".join(str(acc) for acc in self.accounts.values())


if name == "main":
    bank = Bank()
    acc1 = BankAccount(owner_name="Олексій", account_number="12345", balance=5000)
    acc2 = BankAccount(owner_name="Марина", account_number="67890", balance=3000)

    bank.add_account(acc1)
    bank.add_account(acc2)

    acc1.deposit(2000)
    acc2.withdraw(500)
    bank.transfer(from_account_number="12345", to_account_number="67890", amount=1000)

    print(bank)
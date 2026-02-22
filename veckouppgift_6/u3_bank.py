"""
3 Banken
Skapa en klass som representerar ett bankkonto. Banken ska kunna:
- sätta in pengar (deposit)
- ta up pengar (withdraw)
- returnera nuvarande saldo (balance)
- räkna ut ränta (apply_interest, lägger till räntan till kontot)
- tala om ifall man har råd att betala en räkning (returnera True/False)

Gör en metod för varje funktion.

Skriv enhetstester för varje funktion. Använd gärna TDD-metoden, att börja med testfallen innan du skriver koden.
"""
class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0.02):
        self.__balance = initial_balance
        self.__interest_rate = interest_rate

    def deposit(self, amount):

        if amount == None:
            raise ValueError("Deposit must have a value")
        elif not isinstance(amount, (int, float)):
            raise ValueError("Deposit must be a number")
        elif amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
        
    def withdraw(self, amount):
        if amount == None:
            raise ValueError("Amount must have a value")
        elif not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        elif amount > self.__balance:
            raise ValueError("Insufficient funds")
        elif 0 < amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        

    def get_balance(self):
        return self.__balance

    def apply_interest(self):
        if self.__interest_rate == None:
            raise ValueError("Interest rate must have a value")
        elif not isinstance(self.__interest_rate, (int, float)):
            raise ValueError("Interest rate must be a number")
        elif self.__interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        else:
            self.__balance += self.__balance * self.__interest_rate

    def can_pay_bill(self, bill_amount):
        if bill_amount == None:
            raise ValueError("Bill amount must have a value")
        elif not isinstance(bill_amount, (int, float)):
            raise ValueError("Bill amount must be a number")
        elif bill_amount < 0:
            raise ValueError("Bill amount cannot be negative")
        else:
            return self.__balance >= bill_amount
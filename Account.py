# Example of an abstract base class.
# See page 22 in Lecture 3.


class Account(object):
    def __init__(self):
        self._balance = 0.0

    def withdraw(self, amount):
        if self._balance - amount >= 0.0:
            self._balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        self._balance += amount

    # To be implemented in each child class
    # An abstract method
    def deductFees(self):
        print "All abstract methods must be implemented in each child class."
        raise NotImplementedError


# Each subclass MUST implement ALL abstract methods.


class Checking(Account):
    def __init__(self):
        super(Checking, self).__init__()
        self._badCheckFee = 5.00
        self._lowBalanceFee = 25.00

    def processCheck(self, amount):
        if not self.withdraw(amount):
            self._balance -= self._badCheckFee

    # Here, the abstract method deductFees is implemented in the subclass
    def deductFees(self):
        if self._balance < 200.00:
            self._balance -= self._lowBalanceFee


def monthly_account_update(account):
    # Here's another polymorphic function
    account.deductFees()


if __name__ == "__main__":
    someAccount = Checking()
    print "\n1. You just opened a checking account. Your balance is $%0.2f" % someAccount._balance
    someAccount.deposit(300)
    print "2. Thanks for the deposit. Your balance is $%0.2f" % someAccount._balance
    someAccount.processCheck(120)
    print "3. Your check for $120.00 has been processed. Your new balance is $%0.2f" % someAccount._balance
    monthly_account_update(someAccount)
    print "4. A low balance fee of $25.00 fee has been applied. Your new balance is $%0.2f" % someAccount._balance

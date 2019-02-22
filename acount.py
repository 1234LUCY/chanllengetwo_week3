
from threading import RLock

class BankAccount(object):
   
    _lock = RLock()

    def __init__(self) -> None:
        self._balance = None


    def get_balance(self) -> int:
        #checking for account balance
        with self._lock:
            self.error_if_closed()
            return self._balance

    def open(self) -> None:
        #opening an account
        with self._lock:
            self._balance = 0

    def deposit(self, amount: int) -> None:
        #depopsit on the account but not negative amounts
        with self._lock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("Cannot  transact negative deposits!")
            self._balance += amount

    def withdraw(self, amount):
       #withdrawing from the account but not exceeding the amount on the account
        with self._lock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("Cannot withdraw negative amounts!")
            elif amount > self._balance:
                raise ValueError("Cannot transact withdrawls exceeding balance!")
            self._balance -= amount

    def close(self):
        #closing the account
        with self._lock:
            self._balance = None

    def error_if_closed(self) -> None:
        #no transaction incase the account is closed
            if self._balance is None:
                raise ValueError("Cannot perform operations transactions on a closed account!")

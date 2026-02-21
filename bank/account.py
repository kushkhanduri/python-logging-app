
import json

class BankAccount:
	def __init__(self, owner: str, balance: float):
		self.owner= owner
		self._balance = balance
		self._transaction_count = 0

	@property
	def balance(self):
		return self._balance

	def deposit(self, amount: float):
		if amount <= 0:
			print("Invalid deposit amount")
			return
		self._balance += amount
		self._transaction_count += 1

	def withdraw(self, amount: float):
		if amount <= 0:
			print("Invalid withdrawl amount")
			return
		if amount > self._balance:
			print("Insufficient funds")
			return
		self._balance -= amount
		self._transaction_count += 1

	def to_dict(self):
		return {
			"owner": self.owner,
			"Balance": self._balance,
			"transaction_count": self._transaction_count
		}

	@classmethod
	def from_dict(cls, data: dict):
		account = cls(data["owner"], data["Balance"])
		account._transaction_count = data.get("transaction_count", 0)
		return account

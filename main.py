
import logging

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s - %(message)s",
	handlers=[
		logging.FileHandler("app.log"),
		logging.StreamHandler()
	]
)

import json
import os
from bank.account import BankAccount



DATA_FILE = "data/accounts.json"



def save_account(account: BankAccount):

	with open(DATA_FILE, "w") as f:
		json.dump(account.to_dict(), f, indent=4)

def load_account():
	if not os.path.exists(DATA_FILE):
		return None

	with open(DATA_FILE, "r") as f:
		data = json.load(f)
		return BankAccount.from_dict(data)

def main():

	account = load_account()


	if account is None:
		print("Creating new account...")
		name = input("Enter your name: ")
		account = BankAccount(name, 1000)
		save_account(account)


	while True:

		print("\n==== Banking Menu ====")
		print("1. Check Balance")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Exit")

		choice = input("Select an option: ")

		if choice == "1":
			print(f"Current balance: {account.balance}")

		elif choice == "2":
			try:
				logging.debug(f"Balance before deposit: {account.balance}")
				amount = float(input("Enter amount to deposit: "))
				account.deposit(amount)
				save_account(account)
				logging.info("Deposit complete.")

			except ValueError:
				print("Invalid amount. Please enter a number")

		elif choice == "3":
			try:
				amount = float(input("Enter amount to withdraw: "))
				account.withdraw(amount)
				save_account(account)
				logging.info("Withdrawl processed.")
			except ValueError:
				print("Invalid amount. Please enter a number")

		elif choice == "4":
			print("Goodbye!")
			break

		else:
			print("Invalid option. Try again.")




if __name__ == "__main__":
	main()


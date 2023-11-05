from ATM_controller import *


list_cards = [{"card_number":"100", "pin":"1234", "accounts":{"00":3, "02":4}},
              {"card_number":"101", "pin":"1234", "accounts":{"00":5, "02":6}}]

test = {"card_number":"101", "pin":"1234", "account":"02", "action":[("See Balance", None), ("Deposit", 100), ("Withdraw", 200)]}

atm = ATMController(list_cards)
print(atm.test_case(test))
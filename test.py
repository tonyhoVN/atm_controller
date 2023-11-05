from ATM_controller import *
import pytest

# Declare list cards 
list_cards = [{"card_number":"100", "pin":"1234", "accounts":{"00":3, "02":4}},
              {"card_number":"101", "pin":"1234", "accounts":{"00":5, "02":6}}]

# Declare ATM
atm = ATMController(list_cards)

# Declare test case 
test = {
    "card_number": {"card_number":"102", "pin":"1234"},
    "pin": {"card_number":"100", "pin":"1235", "account":"02", "action":[("See Balance", None)]},
    "balance": {"card_number":"100", "pin":"1234", "account":"02", "action":[("See Balance", None)]},
    "withdraw": {"card_number":"100", "pin":"1234", "account":"02", "action":[("Withdraw", 1)]},
}

print(atm.test_case(test["card_number"]))

def test_card_number():
    assert atm.test_case(test["card_number"]) == "wrong card"

def test_pin_number():
    assert atm.test_case(test["pin"]) == "wrong pin"

def test_balance():
    assert atm.test_case(test["balance"]) == [(4,True)]






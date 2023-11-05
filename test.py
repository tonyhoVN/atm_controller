from ATM_controller import *

# Declare list cards 
list_cards = [{"card_number":"100", "pin":"1234", "accounts":{"01":3, "02":4}},
              {"card_number":"101", "pin":"1234", "accounts":{"01":5, "02":6}}]

# Declare ATM
atm = ATMController(list_cards)

# Declare test case 
test = {
    "card_number": {"card_number":"102", "pin":"1234"},
    "pin": {"card_number":"100", "pin":"1235"},
    "account": {"card_number":"100", "pin":"1234", "account":"03", "action":[]}, 
    "balance": {"card_number":"100", "pin":"1234", "account":"01", "action":[("See Balance", None)]},
    "withdraw": {"card_number":"100", "pin":"1234", "account":"02", "action":[("Withdraw", 1),("Withdraw", 5)]},
    "deposit": {"card_number":"100", "pin":"1234", "account":"01", "action":[("Deposit", 5)]}
}

def test_card_number():
    assert atm.test_case(test["card_number"]) == "wrong card"

def test_pin_number():
    assert atm.test_case(test["pin"]) == "wrong pin"

def test_account_number():
    assert atm.test_case(test["account"]) == "wrong account"

def test_balance():
    assert atm.test_case(test["balance"]) == [(3,True)]

def test_withdraw():
    assert atm.test_case(test["withdraw"]) == [(3, True),(3, False)]

def test_deposit():
    assert atm.test_case(test["deposit"]) == [(8, True)]


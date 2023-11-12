from ATM_controller import *

# Declare list cards 
list_cards = [{"card_number":"100", "pin":"1234", "accounts":{"01":3, "02":4}},
              {"card_number":"101", "pin":"1234", "accounts":{"01":5, "02":6}}]

# Declare test_cases case 
test_cases = {
    "card_number": {"card_number":"102", "pin":"1234", "account":"01", "action":[]},
    "pin": {"card_number":"100", "pin":"1235", "account":"01", "action":[]},
    "account": {"card_number":"100", "pin":"1234", "account":"03", "action":[]}, 
    "balance": {"card_number":"100", "pin":"1234", "account":"01", "action":[("See Balance", 0)]},
    "withdraw": {"card_number":"100", "pin":"1234", "account":"02", "action":[("Withdraw", 1),("Withdraw", 5)]},
    "deposit": {"card_number":"100", "pin":"1234", "account":"01", "action":[("Deposit", 5)]}
}

# Declare ATM and input all cards 
atm = ATMController(list_cards)

# Define function for each test case
def test_card_number():
    assert atm.execute(test_cases["card_number"]) == "wrong card"

def test_pin_number():
    assert atm.execute(test_cases["pin"]) == "wrong pin"

def test_account_number():
    assert atm.execute(test_cases["account"]) == "wrong account"
    
def test_balance():
    assert atm.execute(test_cases["balance"]) == [3]

def test_withdraw():
    assert atm.execute(test_cases["withdraw"]) == [3, 3]

def test_deposit():
    assert atm.execute(test_cases["deposit"]) == [8]


from ATM_controller import *

# Declare list cards 
list_cards = [{"card_number":"100", "pin":"1234", "accounts":{"01":3, "02":4}},
              {"card_number":"101", "pin":"1234", "accounts":{"01":5, "02":6}}]

# Declare test_cases case 
test_cases = {
    "card_number": {"card_number":"102", 
                    "pin":"1234", 
                    "account":"01", 
                    "action":[], 
                    "result":"wrong card"},
    "pin": {"card_number":"100", 
            "pin":"1235", 
            "account":"01", 
            "action":[], 
            "result":"wrong pin"},
    "account": {"card_number":"100", 
                "pin":"1234", 
                "account":"03", 
                "action":[], 
                "result": "wrong account"}, 
    "balance": {"card_number":"100", 
                "pin":"1234", 
                "account":"01", 
                "action":[("See Balance", 0)], 
                "result":[3]},
    "withdraw": {"card_number":"100", 
                 "pin":"1234", 
                 "account":"02", 
                 "action":[("Withdraw", 1),("Withdraw", 5)],
                 "result": [3,3]},
    "deposit": {"card_number":"100", 
                "pin":"1234", 
                "account":"01", 
                "action":[("Deposit", 5),("Deposit", 1)],
                "result": [8,9]}
}

# Declare ATM and input all cards 
atm = ATMController(list_cards)

# Test all cases
num_test = 0
pass_test = 0
for test_case_name in test_cases.keys():
    num_test += 1
    # Check the result
    result = atm.execute(test_cases[test_case_name])
    if result == test_cases[test_case_name]["result"]:
        pass_test += 1

# Print result 
print("Passed: %d/%d tests" %(pass_test, num_test))



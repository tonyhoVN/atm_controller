# ATM Controller

This is a simple ATM controller.

## How to clone the Project

Use git clone to clone the package to your directory 

```bash
git clone https://github.com/hoanhtung2000/atm_controller.git
```

## Run test

Firstly, install the __pytest__ by using [pip](https://pip.pypa.io/en/stable/)

```bash
pip install pytest
```

Use __pytest__ to run all tests in file __test.py__. Make sure to cd to main directory of folder atm_controller 

```bash
cd atm_controller
pytest ./test.py
```
The result will show the number of passed test.

## Build test

Open file __test.py__. Please make sure to update appropriately as following structure.

#### Step1: Add Credit Cards
You can add credit cards to object  ``list_card``. The input information for card is a dictionary which has key "card_number", "pin", and "accounts". The table shows keys and values of card.

| Key | Value Desc. | Key Value Type | Value |
| -------- | -------- | -------- | ------- |
| `card_number` | card number | `String` | "100" |
| `pin` | pin number | `String` | "1234" |
| `accounts` | accounts and their balances | `Dictionary` | {"01":3, "02":4} |

Example of the information of credit card:

```python
{"card_number":"100", "pin":"1234", "accounts":{"01":3, "02":4} }
```

#### Step2: Add Test Case

You can add test case to object **test_cases**, which is a dictionary contains all tests you want to execute. The test case is an item of dictionary whose key is name of test (string) and value is the content of test (dictionary). 

The following table shows keys and values of the content of test.

| Key | Value Desc. | Key Value Type | Value |
| -------- | -------- | -------- | ------- |
| `card_number` | input card number | `String` | "100" |
| `pin` | input pin number | `String` | "1234" |
| `account` | input account want to implement action | `String` | "01" |
| `action` | list of action want to implement | list of tuple(`String`, `int`) | [("See Balance", 0)] |

> **NOTE:**
> - Each action is a tuple whose first element is one of three actions: `"See Balance"`, `"Withdraw"`, or `"Deposit"`.
> - The second element of action is the amount of money for the action. If the action is `"See Balance"`, the second element is always `0`.

Example of the test case:
```python
"withdraw": {"card_number":"100", "pin":"1234", "account":"02", "action":[("Withdraw", 1),("Withdraw", 5)]}
```

#### Step3: Define Expected Result for Test Case 
The expected result is determined manually by following rules:
- If the input card number is wrong, atm returns "wrong card"
- If the input pin number is wrong, atm returns "wrong card"
- If the input account number is wrong, atm returns "wrong account"
- While implementing actions, atm returns the list of balance of the account after actions implemented. The blance is unchanged if the amount of withdraw is greater than the current balance of this account.
- If there is no action (the action is an empty list), the atm returns an empty list `[]`.

Example:
- Input card is:
```python 
{"card_number":"100", "pin":"1234", "accounts":{"01":3, "02":4}}
```
- Input action is:
```python 
"withdraw": {"card_number":"100", "pin":"1234", "account":"02", "action":[("Withdraw", 1),("Withdraw", 5)]}
```
- Expected result is: `[3, 3]`

#### Step4: Define Test Function for Test Case 
Use following format to define your own test function
```python
def your_test_fct():
    assert atm.execute(test_cases["your_test_case"]) == your_expected_result
```

Replace `your_test_fct`, `your_test_case`, `your expected_result` with a name of a function, name of test case, and the expected result for this test case.

# ATM Controller

This is a simple ATM controller.

## How to clone the Project

Use git clone to clone the package to your directory 

```bash
git clone https://github.com/tonyhoVN/atm_controller.git
```

## Run test
Run file __test.py__ to check all the tests. Ensure to cd to main directory of folder __atm_controller__.

```bash
cd atm_controller
python ./test.py
```
The result will show the number of passed tests.

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

The following table shows keys and values of the content of one test.

| Key | Value Desc. | Key Value Type | Value |
| -------- | -------- | -------- | ------- |
| `card_number` | input card number | `String` | "100" |
| `pin` | input pin number | `String` | "1234" |
| `account` | input account want to implement actions | `String` | "01" |
| `action` | list of actions want to implement on the selected account | list of tuple(`String`, `int`) | [("See Balance", 0)] |
| `result` | expected result for the test case | `String` or list of `int` | "wrong card" or [2, 4] |

#### 2.1: Define actions 
The list of actions can be selected by following rules:
- Each action is a tuple whose first element is one of three actions: `"See Balance"`, `"Withdraw"`, or `"Deposit"`.
- The second element of each action is the amount of money. If the action is `"See Balance"`, the second element is always `0`.
- If there is no input action, the action list is an empty list `[]`.

Example of the action:
```python
"action":[("Deposit", 1),("Withdraw", 5)]
```

#### 2.2: Define expected result for test case 
The expected result for test case is a list contains result after each action is implemented. The result is determined manually by following rules:
- If the input card number is wrong, atm should return "wrong card"
- If the input pin number is wrong, atm should return "wrong card"
- If the input account number is wrong, atm should return "wrong account"
- If the `card_number`, `pin`, and `account` are correct, the atm should return the list of account balance after implementing each action. 

> **Note**
> - The blance is unchanged if the amount of withdraw is greater than the current balance of this account.
> - If there is no action, the atm should return an empty list `[]`.

Example:
- Input card is:
```python 
{"card_number":"100", "pin":"1234", "accounts":{"01":3, "02":4}}
```
- Input action is:
```python 
"withdraw": {"card_number":"100", 
             "pin":"1234",
             "account":"02", 
             "action":[("Withdraw", 1),("Withdraw", 5)]}
```
- Expected result is: 
```python
"result":[3, 3]
```
- Full action define:
```python 
"withdraw": {"card_number":"100", 
             "pin":"1234",
             "account":"02", 
             "action":[("Withdraw", 1),("Withdraw", 5)],
             "result":[3, 3]}
```

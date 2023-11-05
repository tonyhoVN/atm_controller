# ATM Simulation

This is a simple ATM simulation project.

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

Use __pytest__ to run all tests in file __test.py__

```bash
pytest ./test.py
```
The result will show the number of passed test.

## Build test

Open file __test.py__. Please make sure to update appropriately as following structure.

#### Step1: Add Credit Cards
You can add credit cards to object  ``list_card``. The input information for card is a dictionary which has key "card_number", "pin", and "accounts".

| Key | Value Desc. | Key Value Type | 
| -------- | -------- | -------- |
| `card_number` | card number | `str` | 
| `pin` | pin number | `str` |
| `accounts` | accounts and their balance | `dict` {account: balance} |

For instance, the information of credit card is

```python
{"card_number":"101", "pin":"1234", "accounts":{"01":5, "02":6} }
```

#### Step2: Add Test Case

You can add test case to object **test_cases**, which is a dictionary contains all tests you want to execute. The test case is an item in dictionary whose key is name of test (string) and the content of test (dictionary). The keys of content includes input card number, input pin, selected account (if you want to implement some actions in this account), and the list of actions you want to implement. Each action is a tuple whose first element is on of three action ["See Balance", "Withdraw", or "Deposit"]. The second element of action is the amount of money if action is "Withdraw" or "Deposit", or *None* value if the action is "See Balance".

Example of the test case 

class Card:
    def __init__(self, card_info: dict):
        self.pin = card_info["pin"]
        self.accounts = card_info["accounts"]
        self.selected_account = None

    def select_account(self, account_num: str):
        self.selected_account = account_num # select the account to handle

    def see_balance(self):
        return self.accounts[self.selected_account], True
    
    def deposit(self, amount: int):
        # Increase blance
        self.accounts[self.selected_account] += amount
        return self.accounts[self.selected_account], True

    def withdraw(self, amount: int):
        current = self.accounts[self.selected_account]
        if amount > current:
            # print("Your balance is not enough")
            return self.accounts[self.selected_account], False
        if amount <= current:
            self.accounts[self.selected_account] -= amount
            # print("You withdrew %d dollars" %amount )
            return self.accounts[self.selected_account], True


class ATMController:
    def __init__(self, list_cards: list):
        self.cards = list_cards
        self.selected_card: Card = None

    def check_card_num(self, card_num):
        list_card_num = [card["card_number"] for card in self.cards]
        if card_num in list_card_num:
            index = list_card_num.index(card_num) # find card needed to handle
            self.selected_card = Card(self.cards[index]) # select card to handle
            return True
        else: 
            return False
    
    def check_pin(self,pin):
        return (pin == self.selected_card.pin)
    
    def check_account_num(self, account):
        if account in self.selected_card.accounts.keys():
            self.selected_card.select_account(account) # select account for action
            return True
        else:
            return False
    
    def implement_action(self, action: tuple):
        balance = None
        status = None
        if action[0] == "See Balance":
            balance,status = self.selected_card.see_balance()
            
        if action[0] == "Withdraw":
            balance,status = self.selected_card.withdraw(amount=action[1])

        if action[0] == "Deposit":
            balance,status = self.selected_card.deposit(amount=action[1])
        
        return balance,status
    
    def test_case(self, test_case):
        result = []
        if not self.check_card_num(test_case["card_number"]):
            return "wrong card"
        if not self.check_pin(test_case["pin"]):
            return "wrong pin"
        if not self.check_account_num(test_case["account"]):
            return "wrong account"  
        for action in test_case["action"]:
            result.append(self.implement_action(action))
        return result

            

        




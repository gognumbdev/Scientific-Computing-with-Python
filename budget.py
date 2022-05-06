class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        
    
    def deposit(self,amount,description=""):
        # This method append an object to the ledger list in the form of {"amount": amount, "description": description}.
        self.ledger.append({"amount":amount,"description":description})

    def withdraw(self,amount,description=""):
        # amount should be a negative number
        # return result : True or False
        if(self.check_funds(amount)):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        else:
            return False

    def get_balance(self):
        # returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        balance = 0
        for i in range(len(self.ledger)):
            balance += self.ledger[i]["amount"]
        return balance

    def transfer(self,amount,another_category):    
        # accepts an amount and another budget category as arguments.
        # This method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
        # This method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
        if (self.check_funds(amount)):
            self.withdraw(amount,"Transfer to {category_name}".format(category_name = another_category.name))
            another_category.deposit(amount,"Transfer from {category_name}".format(category_name = self.name))
            return True
        else:
            return False

    def check_funds(self,amount):
        # returns False if the amount is greater than the balance of the budget category and returns True otherwise
        if(amount > self.get_balance()):
            return False
        else:
            return True
    def __str__(self):
        ledger_orders = [self.name.center(30,"*")+"\n"]
        for i in range(len(self.ledger)):
            order_info = self.ledger[i]
            remain = 30-len(order_info["description"][:23]) - len(format(order_info["amount"],".2f")[:7])
            # remain -= len(str(order_info["amount"]))
            result_order = order_info["description"][:23]+(" "*remain)+str(format(order_info["amount"],".2f"))[:7]
            ledger_orders.append(result_order+"\n")
        ledger_orders.append("Total: "+str(round(self.get_balance(),2)))

        return "".join(ledger_orders)

def create_spend_chart(categories):
    ...

food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
print(food)
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
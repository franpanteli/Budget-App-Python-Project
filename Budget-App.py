class Category:

"""
	-> We first define the category class, and then the `create_spend_chart` function

    Defining the category class:
        -> There are multiple methods which we define as part of this 
        -> They are all aimed at targeting the bank balance of the category objects 

    -> We first define the category class, and then the `create_spend_chart` function

	Defining the category class:
        -> There are multiple methods which we define as part of this 
        -> They are all aimed at targeting the bank balance of the category objects 

	The __init__ method:
	-> This method initialises a category 
	-> This has a name, empty leger (list) and sets the current balance and spending to zero 
	-> self.ledger <- This is an empty list we initialise, to store transaction details 
	-> self.current_balance and self.spending are then initialised at zero
"""

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.current_balance = 0
        self.spending = 0

"""    
    The `check_funds` method:
        -> This is the method which we use to check if the account has enough money for the 
            purchase to go through 
        -> Either we have enough money for the transaction, or we don't 
        -> This truth is stored as a boolean
"""

    def check_funds(self, amount):
        return amount <= self.current_balance

"""
	The deposit method:
        -> This adds a deposit transaction to the ledger and updates the current balance 
        -> Take these amounts (`amount`) and (`description`) and update the current balance 
        -> It takes an amount and an optional argument, called `description`
        -> We append a dictionary representing the deposit transaction to `self.ledger`
        -> We then increase the current balance by this amount     
"""

    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount*1.00, 'description':description})
        self.current_balance = self.current_balance + amount

 """
   The withdraw method:
     -> We have multiple categories, each has a balance
	-> This is the method which handles withdrawals from a category
	-> This category has a balance, and to make the withdrawal we need enough money 
	-> If the balance is less than the amount we want to withdraw, then there isn't enough 
        money in the balance to execute the withdrawal and a False boolean is returned 
	-> If the balance is more than the amount we want to withdraw, then we execute the withdrawal 
	-> This means updating the balance, logging that a withdrawal has happened in the ledger 
        and updating the spending value  
"""
   
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({'amount':-amount*1.00, 'description':description})
            self.current_balance = self.current_balance - amount
            self.spending = self.spending + amount
            return True
        else:
            return False
    
 """
   The transfer method:
	-> We have a target and a withdrawal category 
	-> We want to take an amount of money and move it from the target to the withdrawal category
	-> False is returned if the amount of money which we want to transfer is greater than the balance 
        of the account we want to transfer it from
	-> Otherwise, the transfer is executed 
	-> This would involve using the `withdraw` and `deposit` methods 
"""            

    def transfer(self, amount, target):
        if self.check_funds(amount) == True:
            self.withdraw(amount, 'Transfer to ' + target.name)            
            target.deposit(amount, 'Transfer from ' + self.name)  

            return True
        else:
            return False    

# This method gives the balance of the category we are currently dealing with             
        
    def get_balance(self):
        return self.current_balance
    
    def __str__(self):
        left_star = (30-len(self.name))//2
        a = '*' * left_star + self.name + '*' * (30 - left_star - len(self.name)) + '\n'
        
        for entry in self.ledger:
            amt = f"{entry['amount']:.2f}"
            a = a + entry['description'][:23] + str(amt).rjust(30 - len(entry['description'][:23])) + '\n'            
        
        a = a + f'Total: {self.current_balance:.2f}'
        
        return a
    
 """
   The create_spend_chart:
	-> This is a bar chart function 
	-> We have multiple different categories, and each has spending associated with them 
	-> Each category has its own height on the bar chart
	-> This relates to the percentage of total spending for that category, relative to the others 
"""

def create_spend_chart(categories):
    spendings = []
    spendings_perc =[]
    total_spending = 0
    
    # find total spending
    for cate in categories:
        total_spending = total_spending + cate.spending
    
    # find spending as %
    spendings = [cate.spending for cate in categories]
    spendings_perc = [(cate.spending/total_spending * 100)//10 for cate in categories] 
    
    # make chart
    line_100 = '100| '
    for perc in spendings_perc:
        if perc >= 10:
            line_100 = line_100 + 'o  '
        else:
            line_100 = line_100 + '   '    
    
    line_90 = ' 90| '
    for perc in spendings_perc:
        if perc >= 9:
            line_90 = line_90 + 'o  '
        else:
            line_90 = line_90 + '   '   
            
    line_80 = ' 80| '
    for perc in spendings_perc:
        if perc >= 8:
            line_80 = line_80 + 'o  '
        else:
            line_80 = line_80 + '   ' 

    line_70 = ' 70| '
    for perc in spendings_perc:
        if perc >= 7:
            line_70 = line_70 + 'o  '
        else:
            line_70 = line_70 + '   '   
            
    line_60 = ' 60| '
    for perc in spendings_perc:
        if perc >= 6:
            line_60 = line_60 + 'o  '
        else:
            line_60 = line_60 + '   '
            
    line_50 = ' 50| '
    for perc in spendings_perc:
        if perc >= 5:
            line_50 = line_50 + 'o  '
        else:
            line_50 = line_50 + '   '               
    
    line_40 = ' 40| '
    for perc in spendings_perc:
        if perc >= 4:
            line_40 = line_40 + 'o  '
        else:
            line_40 = line_40 + '   ' 
            
    line_30 = ' 30| '
    for perc in spendings_perc:
        if perc >= 3:
            line_30 = line_30 + 'o  '
        else:
            line_30 = line_30 + '   '             
            
    line_20 = ' 20| '
    for perc in spendings_perc:
        if perc >= 2:
            line_20 = line_20 + 'o  '
        else:
            line_20 = line_20 + '   '               
            
    line_10 = ' 10| '
    for perc in spendings_perc:
        if perc >= 1:
            line_10 = line_10 + 'o  '
        else:
            line_10 = line_10 + '   '   
            
    line_0 = '  0| '
    for perc in spendings_perc:
        if perc >= 0:
            line_0 = line_0 + 'o  '
        else:
            line_0 = line_0 + '   '   
            
    line_dash = '    -'
    for perc in spendings_perc:
        line_dash = line_dash + '---'
            
    # make x label
    max_length = max([len(cate.name) for cate in categories])
   
    name_labels = [cate.name.ljust(max_length) for cate in categories]
    
    x_axis_labels = ''
    for i in range(max_length):
        x_axis_labels = x_axis_labels + '     '
        for label in name_labels:
            x_axis_labels = x_axis_labels + label[i] + '  '
        x_axis_labels = x_axis_labels + '\n'    
    
    x_axis_labels = x_axis_labels.rstrip() + '  '
    
    return ('Percentage spent by category\n' + line_100 + '\n' + line_90 + '\n' + line_80 + '\n' + line_70 + '\n' + line_60 + '\n' + line_50 + '\n' + 
           line_40 + '\n' + line_30 + '\n' + line_20 + '\n' + line_10 + '\n' + line_0 + '\n' + line_dash + '\n' + x_axis_labels)
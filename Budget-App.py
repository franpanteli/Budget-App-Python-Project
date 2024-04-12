class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.current_balance = 0
        self.spending = 0
    
    def check_funds(self, amount):
        return amount <= self.current_balance
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount*1.00, 'description':description})
        self.current_balance = self.current_balance + amount
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({'amount':-amount*1.00, 'description':description})
            self.current_balance = self.current_balance - amount
            self.spending = self.spending + amount
            return True
        else:
            return False
    
    def transfer(self, amount, target):
        if self.check_funds(amount) == True:
            self.withdraw(amount, 'Transfer to ' + target.name)            
            target.deposit(amount, 'Transfer from ' + self.name)  

            return True
        else:
            return False    
        
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
__author__ = 'irresolute'

import shelve # managing the database of expenditure
import datetime

f = shelve.open('credit')
g = shelve.open('expense')

#To manage the credit account

def credit(name,amount):

    if f.has_key(name):
        if amount:
            f[name] += amount
    else:
        if amount:
            f[name] = amount
    
    if f[name] == 0:
        del f[name]
    print 'bal: ' +name + ': '
    if f.has_key(name):
        print h[name]
    else:
        print 'Account Deleted'


#To manage debit

def debit(name,amount):
    
    if f.has_key(name):
        if amount:
            f[name] -= amount
    else:
        if amount:
            f[name] = (-1)*amount
    if f[name] == 0:
        del f[name]

    print 'bal: ' +name + ': '
    if f.has_key(name):
        print f[name]
    else:
        print 'Account Deleted'
# Managing monthly expenses. ;) 

def expense(amount):
    month = datetime.datetime.now().strftime("%B")
    if g.has_key(month):
        if amount:
            g[month] += amount
        else:
            print 'Account not updated'
    else:
        if amount:
            g[month] = amount
        else:
            print 'Account not updated'
    
    print month +' :' 
    print g[month]

#The total Expense Accountant. :P 

def net_expense():
    name_list  = f.keys()
    others = 0
    for i in name_list:
        others += f[i]
    print 'The loan is: '
    print others
    
    print 'The expenditure during this month is: '
    print g[datetime.datetime.now().strftime("%B")]


if __name__ == '__main__':
    #credit('shash',100)  
    expense(40)
    debit('shas',100)
    net_expense()
    

            

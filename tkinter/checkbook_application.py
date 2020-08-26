#!/usr/bin/env python
# coding: utf-8

# ## Data Acquirement

# In[ ]:

# Initiation
with open("transaction.txt", "a") as f:
        f.write('')
#assign categories to each transaction
    # add a menu item to allow the user to view all the transactions in a given category
    # provide the user with summary statistics about the transactions in each category
def get_category():
    categories = [{1:"entertaiment"}, {2:"grocery"}, {3:"business"}, {4:"transportation"}, {5:"else"}]
    while True:
        for i, category in enumerate(categories,start = 1):
            print(i, category[i].capitalize())
        category_choice = input("Please select type of your transaction:")
        if category_choice in ["1", "2", "3", "4", "5"]:
            return categories[int(category_choice) - 1][int(category_choice)]
        else:
            print("Invalid choice, please try again!\n")

#Get tansaction time
import time
def get_tansaction_time():
    tansaction_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return tansaction_time

#get description
def get_description():
    while True:
        option = input("Do you want to add a description to your transaction? Y or N :")
        if option.upper() == "Y":
            description = input("Please type your description: ")
            return description
        elif option.upper() == "N":
            description = "no description"
            return description
        else: 
            print("Invalid input, please try again")


# ## File Format Setup

# In[ ]:


#set input
def set_transaction(category, amount):
    c = category
    t = get_tansaction_time()
    a = amount
    d = get_description()
    transaction = {"category": c, "time": t, "amount": a, "description": d}
    with open("transaction.txt", "a") as f:
        f.write(str(transaction) + "\n")

#get transaction info
import ast
def get_transaction_info():
    with open("transaction.txt") as f:
        content = f.readlines()
    new_trans = []
    for item in content:
        new_trans.append(ast.literal_eval(item.replace("\n", '')))
    return new_trans
    


# ## Basic Features

# In[ ]:


#Check input
def check_input(str_num):
    string = str_num.replace(".", "")
    return string.isdigit()

#get input number
def get_input_number():
    while True:
        amount = input("How much would you like  $")
        if check_input( amount):
            return amount 
        print("Invalid input, please try again!")    
    
#get current balance 
def get_current_balance():
    transactions = get_transaction_info()
    transaction_amounts = [float(transaction["amount"]) for transaction in transactions]
    return  sum(transaction_amounts)

#Get debit
def get_debit():
    category = get_category()
#Check if the input is a valid number
    while True:
        debit = input("How much would you like to withdraw? $")
        if check_input(debit):
            break  
        print("Invalid input, please try again!")
#check if the debit excceed the current balance
    if float(debit) >= get_current_balance():
        print("The amout you withdraw ecceed your balance, please enter again.")
        return "0"
    else:
#Append withdraw amount to the storage file
        #debit_with_category
        signed_debit = "-" + debit
        set_transaction(category, signed_debit)
        return debit

#Get credit
def get_credit():
    category = get_category()
#Check if the input is a valid number
    while True:
        credit = input("How much would you like to deposit? $")
        if check_input(credit):
            break  
        print("Invalid input, please try again!")
#Append withdraw amount to the storage file
    set_transaction(category, credit)
    return credit


       


# ## Additional Feature

# In[ ]:


#Show historical transaction:
def show_historical_transactions():
    #print("No   | category    |time     |amount    |description     \n")
    with open("transaction.txt") as f:
        transactions = f.readlines()
    for i, transaction in enumerate(transactions, start = 1):
        print(str(i) + " " + transaction)      
#         if float(balance) <= 0:
#             print(str(i) + " Withdraw amount: $" + balance)
#         else:
#             print(str(i) +"Deposit amount: $" + balance)


#add a menu item to allow the user to view all the transactions in a given category
def transaction_in_a_category():
    transactions = get_transaction_info()
    category = get_category()
    transaction_amounts = []
    for transaction in transactions:
        if transaction["category"] == category:
            print(transaction)
    #provide the user with summary statistics about the transactions in each category
    transaction_amounts = [float(transaction["amount"]) for transaction in transactions if transaction["category"] == category]
    total_transactions = sum(transaction_amounts)                                    
    print("Your total transactions in this category is : $" + str(total_transactions))

#allow the user to view all the transactions for a given day
def transaction_in_a_day():
    transactions = get_transaction_info()
    year = input("Please input year: ")
    month = input("Please input month: ")
    day = input( "Please input day: ")
    date = year + "-" + month + "-" + day
    transaction_amounts = []
    for transaction in transactions:
        if transaction["time"][:10] == date:
            print(transaction)
    #provide the user with summary statistics about the transactions in this date
    transaction_amounts = [float(transaction["amount"]) for transaction in transactions if transaction["time"][:10] == date]
    total_transactions = sum(transaction_amounts)                                    
    print("Your total transactions in this date is : $" + str(total_transactions))
    
#allow the user to search for keywords in the transaction descriptions, 
#and show all the transactions that match the user's search term
def search_transaction_by_keyword():
    transactions = get_transaction_info()
    keyword = input("Please type the keyword for your search")
    for transaction in transactions:
        if keyword in transaction["description"]:
            print(transaction)


# # MAIN FUNCTION

# In[ ]:

# Greetings 
print("\n~~~ Welcome to your terminal checkbook! ~~~\n\n")

# Main function
while True:
    choice = input("What would you like to do?\n\n1) View current balance\n2) Record a debit (withdraw)\n3) Record a credit (deposit)\n4) Historical transactions \n5) Transaction in a selected category \n6) Transaction in a selected date \n7) See your transaction by a keyword \n8) Exit\n\nYour choice? ")
    if choice == "1":
        print("Your current balance is $" + str(get_current_balance()))
        
    elif choice == "2":
        print("You have withdraw $" + get_debit() + " off your account.")
        
    elif choice == "3":
        print("You have deposit $" + get_credit() + " into your account.")
    
    elif choice == "4":
        print("The following list your historical transactions ")
        show_historical_transactions()
        
    elif choice == "5":
        print("See your transaction in a selected category : ")
        transaction_in_a_category()
        
    elif choice == "6":
        print("See your transaction in a selected date : ")
        transaction_in_a_day()
        
    elif choice == "7":
        print("See your transaction by a keyword : ")
        search_transaction_by_keyword()
        
    elif choice == "8":
        print("Thanks, have a great day!")
        break
    else:
        print("Invalid input")











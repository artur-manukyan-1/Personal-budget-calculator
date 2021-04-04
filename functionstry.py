import json
import os.path

def getNumericInput(displayString):
    while(True):
        user_data = input(displayString)
        if(user_data.isnumeric()):
            user_data = int(user_data)
            return user_data
        else:
            print("Please insert a NUMBER") 


def userexpenses():
    expenses = {
            "Electricity": 0 ,
	    "Water": 0 ,
	    "Gas": 0 ,
	    "Groceries": 0 ,
	    "Eating_out": 0 ,
	    "Transportation": {
                "Taxi": 0 ,
                "Bus": 0 ,
                "Train": 0 
                },
            "Subscriptions": 0 ,
            "Phone, data, internet": 0,
            "Hygiene": 0 ,
            "Self-care": 0 ,
            "Clothing_and_accessories": 0 ,
            "Education": 0 ,
            "Medicine": 0 ,
            "Not_for_yourself": 0 ,
            "Other": 0
            },
    expenses["Electricity"] = int("Please insert the amount: ")
    expenses["Water"] = int("Please insert the amount: ")
    expenses["Gas"] = int("Please insert the amount: ")
    expenses["Groceries"] = int("Please insert the amount: ")
    expenses["eating_out"] = int("Please insert the amount: ")
    expenses["Taxi"] = int("Please insert the amount: ")
    expenses["Bus"] = int("Please insert the amount: ")
    expenses["Train"] = int("Please insert the amount: ")
    expenses["Subscriptions"] = int("Please insert the amount: ")
    expenses["Phone, data, internet"] = int("Please insert the amount: ")      
    expenses["Hygiene"] = int("Please insert the amount: ")
    expenses["Self-care"] = int("Please insert the amount: ")
    expenses["Clothing_and_accessories"] = int("Please insert the amount: ")
    expenses["Education"] = int("Please insert the amount: ")
    expenses["Medicine"] = int("Please insert the amount: ")
    expenses["Not_for_yourself"] = int("Please insert the amount: ")
    expenses["Other"] = int("Please insert the amount: ")      
            
def userincome():
    income = {
            "Allowance": 0 ,
            "Salary": 0 ,
            "Bonus": 0 ,
            "Other": 0
            },
    income["Allowance"] = int("Please insert the amount: ")
    income["Salary"] = int("Please insert the amount: ")
    income["Bonus"] = int("Please insert the amount: ")
    income["Other"] = int("Please insert the amount: ")




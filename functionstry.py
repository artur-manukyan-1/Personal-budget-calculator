import json
import os.path

def getNumericInput(displayString):
    while(True):
        user_data = input(displayString)
        if(user_data.isnumeric()):
            user_data = int(user_data)
            return user_data
        else:
            print("Please insert a NUMBER ") 


def userexpenses():
    expenses = {
            "rent": 0 ,
	    "carpayment": 0 ,
	    "loan": 0 ,
	    "electicity": 0 ,
	    "gas": 0 ,
	    "Transportation": {
                "taxi": 0 ,
                "bus": 0 ,
                "train": 0 
                },
            "water": 0 ,
            "Phone, data, internet": 0,
            "groceris": 0 ,
            "hygine": 0 ,
            "medicine": 0 ,
            "education": 0 ,
            "eatingout": 0 ,
            "subscription": 0 ,
            "selfcare": 0 ,
            "clothing": 0 ,
            "other": 0 ,
            "savings": 0 ,
            }
    expenses["rent"]= getNumericInput("Please enter the amount of your rent ")
    expenses["carpayment"]= getNumericInput("Please enter the amount of your car payment ")
    expenses["loan"]= getNumericInput("Please enter the amount of your loan payment ")
    expenses["electicity"]= getNumericInput("Please enter the amount of your electicity expense ")
    expenses["gas"]= getNumericInput("Please enter the amount of your gas expense ")
    expenses["water"]= getNumericInput("Please enter the amount of your water expense ")
    expenses["groceris"]= getNumericInput("Please enter the amount of your groceris expense ")
    expenses["hygine"]= getNumericInput("Please enter the amount of your hygine expense ")
    expenses["medicine"]= getNumericInput("Please enter the amount of your medicin expense ")
    expenses["education"]= getNumericInput("Please enter the amount of your education expense ")
    expenses["Phone, data, internet"]= getNumericInput("Please enter the amount of your internet expense ")
    expenses["eatingout"]= getNumericInput("Please enter the amount of your eatingout expense ")
    expenses["taxi"]= getNumericInput("Please enter the amount of your taxi expense ")
    expenses["bus"]= getNumericInput("Please enter the amount of your bus expense ")
    expenses["train"]= getNumericInput("Please enter the amount of your train expense ")
    expenses["subscription"]= getNumericInput("Please enter the amount of your subscription expense ")
    expenses["selfcare"]= getNumericInput("Please enter the amount of your selfcare  expense ")
    expenses["clothing"]= getNumericInput("Please enter the amount of your clothing expense ")
    expenses["other"]= getNumericInput("Please enter the amount of your other expense ")
    expenses["savings"]= getNumericInput("Please enter the amount of your other expense ")
    return expenses

def userincome():
    income = {
            "Allowance": 0 ,
            "Salary": 0 ,
            "Bonus": 0 ,
            "Other": 0
            }
    income["Allowance"] = getNumericInput("Please insert the amount:  ")
    income["Salary"] = getNumericInput("Please insert the amount:  ")
    income["Bonus"] = getNumericInput("Please insert the amount:  ")
    income["Other"] = getNumericInput("Please insert the amount:  ")
    return income

def load_user(income, expenses):

    user = {"username":"",
            "income":{},
            "expenses":{},
            "age":0
            }
    user["income"] = income
    user["expenses"] = expenses
    user["username"]= input("Please enter your name:  ")
    user["age"] = input("Please enter your age:  ")
    return user

def fixedexp(expenses):
    rent = expenses["rent"]
    carpayment = expenses["carpayment"]
    loan = expenses["carpayment"]
    f = rent+carpayment+loan
    return f

def variableEssential(expenses):
    electricity = expenses["electricity"]
    gas = expenses["gas"]
    water = expenses["water"] 
    hygine = expenses["hygine"]
    medicine = expenses["medicine"]
    education = expenses["education"] 
    internet = expenses["Phone, data, internet"]
    u = electicity+gas+water+hygine+medicine+education+internet
    return u

def varilablesNonEss(expenses):
    expenses()
    eatingout = expenses["eatingout"]
    taxi = expenses["taxi"]
    bus = expenses["bus"] 
    train = expenses["train"]
    subscription = expenses["subscription"]
    selfcare = expenses["selfcare"] 
    clothing = expenses["clothing"]
    other = expenses["other"]    
    n = eatingout+taxi+bus+train+subscription+selfcare+clothing+other
    return n

def advised(expenses):
   f = fixedexp(expenses)
   u= variableEssential(expenses)
   n = varilablesNonEss(expenses)
   s = savings
   e = f+u
   sum = e+n+s
   percente = e/s*100
   percentu = n/s*100
   percentn = s/s*100   
   if(45< percente <55):
       if(25< percentu < 35):
           if(15< percentn <25):
               print("Your expenses are balanced. 50-30-20 budget phylosophy suggest essential expenses, should represent half of your budget, wants should make up another 30%, and savings and debt repayment should make up the final 20% of your budget.")
           else:
               pass
       else:
           pass
   else:
       print("Please reconsider your expenses. 50-30-20 budget phylosophy suggest essential expenses, should represent half of your budget, wants should make up another 30%, and savings and debt repayment should make up the final 20% of your budget.")
   


def report(expenses):
   f = fixedexp(expenses)
   u = variableEssential(expenses)
   n = varilablesNonEss(expenses)
   prgetNumericInput("Your fixed expenses are", f, ".")
   prgetNumericInput("Your essential expenses for the last month were", u, ".")
   prgetNumericInput("Your non-essential expenses for the last month were", n, ".")
  

def main():
    advised()
    report()




main()

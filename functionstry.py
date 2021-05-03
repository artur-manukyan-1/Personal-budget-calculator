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



def expense_data():
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
    expenses["savings"]= getNumericInput("Please enter the amount you wish to save ")
    return expenses


def income_data():
    income = {
            "Allowance": 0 ,
            "Salary": 0 ,
            "Bonus": 0 ,
            "Other": 0 ,
            "Saved": 0 , 
            }
    income["Allowance"] = getNumericInput("Please insert the amount of your allowance:  ")
    income["Salary"] = getNumericInput("Please insert the amount of your salary:  ")
    income["Bonus"] = getNumericInput("Please insert the amount of your bonuses:  ")
    income["Other"] = getNumericInput("Please insert the amount of other incomes:  ")
    income["Saved"] = getNumericInput("Please insert the amount of you've saved:  ")
    return income



def fixedexp(expenses):
    f = expenses["rent"] + expenses["carpayment"] + expenses["loan"]
    return f


def variableEssential(expenses):
    u = expenses["electicity"] + expenses["gas"] + expenses["water"] + expenses["hygine"]+ expenses["medicine"] + expenses["education"] + expenses["Phone, data, internet"] + expenses["groceris"]
    return u


def varilablesNonEss(expenses):
    n = expenses["eatingout"] + expenses["taxi"] + expenses["bus"] + expenses["train"] + expenses["subscription"] + expenses["selfcare"] + expenses["clothing"] + expenses["other"]    
    return n



def planschange():
    modified = {
        "essentialpercent": 0,
        "savingpercent": 0,
        }
    modified["essentialpercent"] = getNumericInput("What percent of your expenses do you expect to spend of essentials? Insert only the number ")
    modified["savingpercent"] = getNumericInput("What percent of your expenses do you expect to save? Insert only the number ")
    return modified

def modification():
    k = input("Do you want to modify the plan? type 'y' for yes, 'n' for no ")
    y = "y"
    if(k == y):
        essential = modified["essentialpercent"]
        saving = modified["savingpercent"] 
        advised(expense_data())
    else:
        essential = 50
        saving = 20
        advised(expense_data())
        

def advised(expenses):
    e = fixedexp(expenses) + variableEssential(expenses)
    n = varilablesNonEss(expenses)
    s = expenses["savings"]
    sums = e+n+s
    percente = (e/sums)*100
    percentu = (n/sums)*100
    percentn = (s/sums)*100  
    nonessential = 100 - essential - saving
    if(essential - 3 < percente < essential + 3):
        if(nonessential - 3 < percentu < nonessential + 3):
            if(saving - 3 < percentn < saving + 3):
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
   print("Your fixed expenses are", f, ".")
   print("Your essential expenses for the last month were", u, ".")
   print("Your non-essential expenses for the last month were", n, ".")
  


def main():
    modification() 
    advised(expense_data())
    report(expense_data())




main()

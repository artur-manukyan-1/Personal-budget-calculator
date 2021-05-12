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



filename = "user_data.json"



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
    income["Saved"] = getNumericInput("Please insert the amount you've saved:  ")
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


def ifyes(modified, expenses, income):
    essential = modified["essentialpercent"] 
    savings = modified["savingpercent"]
    advised(expenses, essential, savings) 
    report(expenses)
    in_exp(expenses, income)



def advised(expenses, essential, saving):
    e = fixedexp(expenses) + variableEssential(expenses)
    n = varilablesNonEss(expenses)
    s = expenses["savings"]
    sums = e+n+s
    percente = (e/sums)*100
    percentu = (n/sums)*100
    percentn = (s/sums)*100  
    nonessential = 100 - essential - saving
    print("\n")
    
    if(essential - 3 < percente < essential + 3):
        a = 1
    else:
        print("You planned to spent", essential,"% of your total expenses on fixed and essential spendings, ", nonessential,"% on non-essentials and ", saving,"% save for future. Follow the plan to be in control of your spendings.")
        if(essential < percente):
            print("On essentials and fixed expenses you spent ", (e - ((essential*sums)//100)),"$ more than planned. Please pay attention to this. ")
        else:
            print("On essentials and fixed expensesy ou spent ", (((essential*sums)//100) - e),"$ less then planned. Please make sure all your basic needs are covered!")
        a = 0


    
    if(nonessential - 3 < percentu < nonessential + 3):
        b = 1
    else:
        if(nonessential < percentu):
            print("In the last month on non-essentials you spent ", (n - ((nonessential*sums)//100)),"$ more than planned,please reconsider your expenses.")
        else:
            print("In the last month you spent ", (((nonessential*sums)//100) - n),"$ less than planned, good job!")
        b = 0
               
    
    
    if((saving - 3) < percentn < (saving + 3)):
        c = 1
        print("Last month you saved", s,"$ as planned.")
    else:
        if(saving < percentn):
            print("According to your last month's budget data, your saved ", (s - ((saving*sums)//100)),"$ more than planned. Good job!")
        else:
            print("According to your last month's budget data, your saved ", (((saving*sums)//100) - s),"$ less then planned.")
        c = 0
    
   

    if(a + b + c == 3):
        print("Your expenses are balanced.", essential,"-", nonessential,"-", saving," budget phylosophy suggest essential expenses, should represent ", essential,"%, 'wants' should make up another ", nonessential,"%, and savings and debt repayment should make up the final ", saving,"% of your budget.")
    else: 
        pass




def report(expenses):
   f = fixedexp(expenses)
   u = variableEssential(expenses)
   n = varilablesNonEss(expenses)
   print("Your fixed expenses are", f, "$.")
   print("Your essential expenses for the last month were", u, "$.")
   print("Your non-essential expenses for the last month were", n, "$.")
  


def in_exp(expenses, income):
    incomes = income["Allowance"] + income["Salary"] + income["Bonus"] + income["Other"] +  income["Saved"]
    expense = fixedexp(expenses) + variableEssential(expenses) + varilablesNonEss(expenses) + expenses["savings"]
    if(incomes > expense):
        print("Your expenses are in a budget. You still have ", (incomes - expense),"$ left.")
    elif(income == expense):
        print("Your income and expenses are equal. Be careful to not go over a budget")
    else:
        print("Please review your expenses, your are over a budget with ", (expense - incomes),"$.")
    print("\n")
                
                
                
def modification():
    a = input("Do you have an existing account? type 'y' for yes, 'n' for no ")
    if (a == "y"):


        myfile = open(filename, mode = 'r')
        username = str(input("Please input your username"))

        z = {json.load(myfile)}
        print (z)
        k = input("Do you want to modify the plan? type 'y' for yes, 'n' for no ")
        if(k == "y"):
                ifyes(planschange(), expense_data(), income_data())
        elif(k == "n"):

 #           i = (z[username]["user_income"])
            e = expense_data()

            advised(e, essential = 50, saving = 20)
            report(e)
            in_exp(e, i)
        else:
            print("Invalid, input.")
            k = input("Please type 'y' for yes or 'n' for no ")

    elif (a == "n"):

        username = str(input("Please create a username"))
        myfile = open(filename, mode = 'a')

        k = input("Do you want to modify the plan? type 'y' for yes, 'n' for no ")
        if(k == "y"):
                ifyes(planschange(), expense_data(), income_data())
        elif(k == "n"):
            e = expense_data()
            i = income_data()


            userinf = {username: {"user_income" : i}}
            json.dump([userinf], myfile)
            myfile.close()

            advised(e, essential = 50, saving = 20)
            report(e)
            in_exp(e, i)
        else:
            print("Invalid, input.")
            k = input("Please type 'y' for yes or 'n' for no ")

    

def main():
    modification() 
    




main()





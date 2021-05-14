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

def load_data():
    with open('data.json') as exacs:
        accs = json.load(exacs)
        return accs



def user_check(username, accs):
    for user in accs:
        u = data["username"]
        if (username == u):
            return acc



def saveinfo():
    save = open("data.json", "w")
    save.write(json.dump(accs, indent = 2))
    save.close
                    


def user_data():

    data = {
            "username" : "",
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
            "Allowance": 0 ,
            "Salary": 0 ,
            "Bonus": 0 ,
            "Other": 0 ,
            "Saved": 0 , 
            }
    while(True):
        new_name = data["username"] = str(input("Please create a username"))
        if not(user_check(new_name, accs)):
            break
        print ("That username is taken. Try to be more creative.")
    data["rent"]= getNumericInput("Please enter the amount of your rent ")
    data["carpayment"]= getNumericInput("Please enter the amount of your car payment ")
    data["loan"]= getNumericInput("Please enter the amount of your loan payment ")
    data["electicity"]= getNumericInput("Please enter the amount of your electicity expense ")
    data["gas"]= getNumericInput("Please enter the amount of your gas expense ")
    data["water"]= getNumericInput("Please enter the amount of your water expense ")
    data["groceris"]= getNumericInput("Please enter the amount of your groceris expense ")
    data["hygine"]= getNumericInput("Please enter the amount of your hygine expense ")
    data["medicine"]= getNumericInput("Please enter the amount of your medicin expense ")
    data["education"]= getNumericInput("Please enter the amount of your education expense ")
    data["Phone, data, internet"]= getNumericInput("Please enter the amount of your internet expense ")
    data["eatingout"]= getNumericInput("Please enter the amount of your eatingout expense ")
    data["taxi"]= getNumericInput("Please enter the amount of your taxi expense ")
    data["bus"]= getNumericInput("Please enter the amount of your bus expense ")
    data["train"]= getNumericInput("Please enter the amount of your train expense ")
    data["subscription"]= getNumericInput("Please enter the amount of your subscription expense ")
    data["selfcare"]= getNumericInput("Please enter the amount of your selfcare  expense ")
    data["clothing"]= getNumericInput("Please enter the amount of your clothing expense ")
    data["other"]= getNumericInput("Please enter the amount of your other expense ")
    data["savings"]= getNumericInput("Please enter the amount you wish to save ")
    data["Allowance"] = getNumericInput("Please insert the amount of your allowance:  ")
    data["Salary"] = getNumericInput("Please insert the amount of your salary:  ")
    data["Bonus"] = getNumericInput("Please insert the amount of your bonuses:  ")
    data["Other"] = getNumericInput("Please insert the amount of other incomes:  ")
    data["Saved"] = getNumericInput("Please insert the amount you've saved:  ")
    return data




def fixedexp(data):
    f = data["rent"] + data["carpayment"] + data["loan"]
    return f



def variableEssential(data):
    u = data["electicity"] + data["gas"] + data["water"] + data["hygine"]+ data["medicine"] + data["education"] + data["Phone, data, internet"] + data["groceris"]
    return u



def varilablesNonEss(data):
    n = data["eatingout"] + data["taxi"] + data["bus"] + data["train"] + data["subscription"] + data["selfcare"] + data["clothing"] + data["other"]    
    return n



def planschange():
    modified = {
            "essentialpercent": 0,
            "savingpercent": 0,
            }
    modified["essentialpercent"] = getNumericInput("What percent of your expenses do you expect to spend of essentials? Insert only the number ")
    modified["savingpercent"] = getNumericInput("What percent of your expenses do you expect to save? Insert only the number ")
    return modified


def ifyes(modified, data):
    essential = modified["essentialpercent"] 
    savings = modified["savingpercent"]
    advised(data, essential, savings) 
    report(data)
    in_exp(data)



def advised(data, essential, saving):
    e = fixedexp(data) + variableEssential(data)
    n = varilablesNonEss(data)
    s = data["savings"]
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




def report(data):
   f = fixedexp(data)
   u = variableEssential(data)
   n = varilablesNonEss(data)
   print("Your fixed expenses are", f, "$.")
   print("Your essential expenses for the last month were", u, "$.")
   print("Your non-essential expenses for the last month were", n, "$.")
  


def in_exp(data):
    incomes = data["Allowance"] + data["Salary"] + data["Bonus"] + data["Other"] +  data["Saved"]
    expense = fixedexp(data) + variableEssential(data) + varilablesNonEss(data) + data["savings"]
    if(incomes > expense):
        print("Your expenses are in a budget. You still have ", (incomes - expense),"$ left.")
    elif(incomes == expense):
        print("Your income and expenses are equal. Be careful to not go over a budget")
    else:
        print("Please review your expenses, your are over a budget with ", (expense - incomes),"$.")
    print("\n")



                
def modification():
    
    accs = []
    accs = load_data()

    d = input("Do you have an existing account? type 'y' for yes, 'n' for no ")
    if (d == 'y'):

        username = str(input("Please enter your username"))
        c = user_check(username, accs)
        
        if (c):
            while(True):
                k = input("Do you want to modify the plan? type 'y' for yes, 'n' for no ")
                if(k == "y"):
                    ifyes(planschange(), user_data())
                    break
                elif(k == "n"):
                    e = user_data()
                    advised(e, essential = 50, saving = 20)
                    report(e)
                    in_exp(e)
                    break
                else:
                    print("Invalid, input.")
                    k = input("Please type 'y' for yes or 'n' for no ")
        
        else:
            print("The username is invalid, or doesn't exist")
            while(True):
                create = input("Do you want to create an account? Enter y for yes, and n for no. ")
                if(k == "y"):
                    d = "y"
                    break
                elif(k == "n"):
                    print("Sorry to see you leave, bye! :( ")
                    break
                else:
                    print("Invalid, input.")
                    k = input("Please type 'y' for yes or 'n' for no ")

    elif (d == 'n'):
        newacc = user_data(accs)
        accs.append(newacc)
        accs = load_data()
        saveinfo(accs)
        
       




def main():
    print("Hi! \nWelcome to budget calculator!\nAfter we recieve your data you will recieve your spending's analysis and report. The default plan suggest 50-30-20 spendings, which means 50% of your spendings are fixed and essential expenses, 30% are for non-essential spendings, and 20% should be saved. If you prefer you can modify the plan according to you needs." )
    modification() 
    




main()





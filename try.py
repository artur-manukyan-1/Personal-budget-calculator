def ExistingUser():
    if(os.path.exists("Budget.json")):
        with open('Budget.json') as file_data:
            print(file_data)
            Budget = json.load(file_data)
            return Budget
    else:
        return []

def saveToTheFile(Budget):
    f = open("Budget.json","w")
    print(Budget)
    f.write(json.dumps(Budget,indent=2))
    f.close()



def main():
    while(True):
        trial = input("please work ")
        if(trial == "y"):
            print("okay")
            break
        else:
            expense = userexpenses()
            budget.append(expense)
    print("huh?")
    saveToTheFile(Budget)


main()

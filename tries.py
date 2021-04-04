#ughaki functionnera harcakana ichqanova harmar
rent = int(input("please enter the amount of your rent"))
carpayment = int(input("please enter the amount of your car payment"))
loan = int(input("please enter the amount of your loan payment"))

electicity = int(input("please enter the amount of your electicity expense"))
gas = int(input("please enter the amount of your gas expense"))
water = int(input("please enter the amount of your water expense"))
groceris = int(input("please enter the amount of your groceris expense"))
hygine = int(input("please enter the amount of your hygine expense"))
medicine = int(input("please enter the amount of your medicin expense"))
education = int(input("please enter the amount of your education expense"))
internet = int(input("please enter the amount of your internet expense"))

eatingout = int(input("please enter the amount of your eatingout expense"))
taxi = int(input("please enter the amount of your taxi expense"))
bus = int(input("please enter the amount of your bus expense"))
train = int(input("please enter the amount of your train expense"))
subscription = int(input("please enter the amount of your subscription expense"))
selfcare = int(input("please enter the amount of your selfcare  expense"))
clothing = int(input("please enter the amount of your clothing expense"))
other = int(input("please enter the amount of your other expense"))
savings = int(input("please enter the amount of your other expense"))

def fixedexp():
    f = rent+carpayment+loan
    return f

def variableEssential():
    u = electicity+gas+water+hygine+medicine+education+internet
    return u

def varilablesNonEss():
    n = eatingout+taxi+bus+train+subscription+selfcare+clothing+other
    return n

def advised():
    f = fixedexp()
    u = variableEssential()
    n = varilablesNonEss()
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
                


def report():
    f = fixedexp()
    u = variableEssential()
    n = varilablesNonEss()
    print("Your fixed expenses are", f, ".")
    print("Your essential expenses for the last month were", u, ".")
    print("Your non-essential expenses for the last month were", n, ".")
    advised()
report()


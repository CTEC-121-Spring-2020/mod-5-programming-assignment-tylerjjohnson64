# Module 4
#   Programming Assignment 5
#       Prob-2.py

# <Tyler Johnson>

# this function takes in a total transaction and amount given as inputs from the user
# these values are then passed to the change function where it is calculated in order the money denominations the customer should recieve based on the amount tendered
# the output will be presented as the amount of each money denomination the customer should recieve back, the program will also give an appropiate message if no change back is required

# function definition
def change(transactiontotal,moneytendered):
    difference=(moneytendered-transactiontotal)
    if difference < 0:
        print("not enough money was tendered")
    elif difference == 0:
        print("No change required")
    
    
    cashback=int(round(difference*100))
    
    tens=cashback//1000
    if tens>=1:
        print("tens; ",tens)
    cashback=cashback-(tens*1000)

    fives=cashback//500
    if fives>=1:
        print("fives:",fives)
    cashback=cashback-(fives*500)    

    ones=cashback//100
    if ones>=1:
        print("ones:",ones)
    cashback=cashback-(ones*100)

    quarters=cashback//25
    if quarters>=1:
        print("quarters:",quarters)
    cashback=cashback-(quarters*25)

    dimes=cashback//10
    if dimes >=1:
        print("dimes:",dimes)
    cashback=cashback-(dimes*10)

    nickels=cashback//5
    if nickels >= 1:
        print("nickels:",nickels)
    cashback=cashback-(nickels*5)

    pennies=cashback//1
    if pennies >=1:
        print("pennies:",pennies)
    cashback = cashback-(pennies*1)

    if cashback==0:
        print('change succesfully calculated')
    else:
        print("error occured")
# main function definition
def main():
    transactiontotal=(float(eval(input("What is the cost of the transaction: "))))
    moneytendered=(float(eval(input("How much money was tendered: "))))
    changedue=(moneytendered-transactiontotal)
    changedue=round(changedue,2)
    
    #change(transactiontotal,moneytendered)

    print()

    print("TotalCost:",transactiontotal,"Money tendered:",moneytendered,"Change Due:",changedue)

    change(transactiontotal,moneytendered)
main()

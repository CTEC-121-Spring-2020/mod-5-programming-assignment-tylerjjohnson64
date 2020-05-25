# Module 4
#   Programming Assignment 5
#       Prob-3.py

# <Tyler Johnson>

# IPO
#Function take from the user input values of cost of paint and size of room to be painted
#function main then passes the values to estimate function to calculate prices and required materials
#after calculations the called estimate function spits out an estimate along with calculated values and costs before returning to main and ending

# function definition
def getestimate(sqfoot,paintcost):
    gallonsofpaint=round((sqfoot/112))
    laborhours=(round((sqfoot/112)*8))

    laborcharge=(laborhours*35.00)
    setupfee=99.00
    paintmoney= (float(gallonsofpaint*paintcost))
    estimate = (laborcharge+paintmoney+setupfee)
    
    print("\nGallons of paint required:",gallonsofpaint,"Labor hours:",laborhours)
    print("Paint cost=",paintmoney,"\n" "Labor charge=",laborcharge,"\n")
    print("Setup Fee=",setupfee,"\n")
    print("Total estimate cost=",estimate)
# main function definition
def main():
    sqfoot=(eval(input("What is the square footage of the job?: ")))
    paintcost=(eval(input('What is the cost per gallon of the paint?: ')))
    
    getestimate(sqfoot,paintcost)
main()

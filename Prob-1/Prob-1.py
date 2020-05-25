# Module 4
#   Programming Assignment 5
#       Prob-1.py

# <Tyler Johnson>

# This program takes an int value from the user
# this value is then compared through an if elif structure to determine which case it fits under and returns the value of each particular case
# the main function then prints the returned value weather it be a roman numeral or an error message in cases of numbers outside the given program range

# function definition

# unit test function
def unitTest():
    print("\nUnit Tests")
    print(converter(0))
    print(converter(1))
    print(converter(2))
    print(converter(3))
    print(converter(4))
    print(converter(5))
    print(converter(6))
    print(converter(7))
    print(converter(8))
    print(converter(9))
    print(converter(10))
    
    print()


def converter(number):
    if number == 1:
        return "I"
        
    elif number == 2:
        return 'II'
    elif number == 3:
       
        return 'III'
    elif number == 4:
        
        return 'IV'
    elif number == 5:
        
        return 'V'
    elif number == 6:
        
        return 'VI'
    elif number == 7:
        
        return 'VII'
    elif number == 8:
        
        return 'VIII'
    elif number == 9:
        
        return 'IX'
    elif number == 10:
        
        return 'X'
    else:
        print("Invalid input")




def main():
    
    number=(eval(input("Enter a number between 1 - 10 to convert to a numeral: "))) 
    
    converter(number)
    print("input number",number,"returns roman numeral",converter(number))
    
    
main()

unitTest()









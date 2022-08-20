from art import logo
import os
# print(logo)

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations={"+":add, "-":sub, "*":mul, "/":div}

# op=input("Which operation do you want to perform ? \nAddition : +\nSubtraction : -\nMultiplication : *\nDivide : /\n")

# num1=int(input("Enter the first number : "))
# while is_calculating:
def calculator():  
    print(logo)
    num1=float(input("Enter the first number : "))

    is_calculating=True
    while is_calculating:
            op=input("Which operation do you want to perform ? \nAddition : +\nSubtraction : -\nMultiplication : *\nDivide : /\n")
            num2=float(input("Enter the next number : "))
            for key in operations:
                # print(key)
                if key==op:
                    
                    # result=(calculator(num1,num2))
                    result=(operations[key](num1,num2))
                    print(f"Result : {num1} {key} {num2} = {result}")
                    
                    decision=input("\nType 'y' to continue calculating or type 'n' to exit Calculator : ").strip().lower()
                    if decision=="n":
                        is_calculating=False
                        print("\n***** Thank you for using Calculator *****\n")
                        cls = lambda: os.system('cls')
                        cls()
                        calculator()  #RECURSION:function calling itself inside it     
                    else:
                        num1=result
                        
calculator()
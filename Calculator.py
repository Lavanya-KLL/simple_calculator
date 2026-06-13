def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Cant divide by zero"
    return x/y
number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
operator=input("Enter the operator(+,-,*,/): ")
if operator=="+":
    print(add(number1,number2))
elif operator=="-":
    print(subtract(number1,number2))
elif operator=="*":
    print(multiply(number1,number2))
elif operator=="/":
    print(divide(number1,number2))
else:
    print("Invalid opearator")

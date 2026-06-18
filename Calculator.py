history=[]
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
    
operations={
        "1": ("+",add),
        "2": ("-",subtract),
        "3": ("*",multiply),
        "4": ("/",divide)
        }
while True:
    print("\n --- CALCULATOR")
    print("(1) ADD")
    print("(2) SUBTRACT")
    print("(3) MULTIPLY")
    print("(4) DIVIDE")
    print("(5) SHOW HISTORY")
    print("(6) EXIT")
    
    choice=input("ENTER CHOICE : ")
     
    if choice=="6":
        print("GOODBYE!")
        break
    elif choice=="5":
        print("\n---HISTORY---")
        print("\n".join(history) if history else "No history yet!")
    elif choice in operations:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        symbol,func=operations[choice]
        result=func(a,b)
        print("RESULT : ",result)
        history.append(f"{a} {symbol} {b} ={result}")
    else:
        print("Invalid choice")

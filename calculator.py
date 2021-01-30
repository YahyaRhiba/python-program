num1 = float(input("enter number one : "))
operator = input("enter the operator : ")
num2 = float(input("enter number two : "))

def som(a,b):
    s = a + b 
    return s

def sou(a,b):
    s = a - b 
    return s

def div(a,b):
    d = a/b
    return d 

def prod(a,b):
    p = a*b
    return p 

def clacul(a,b):
    if operator == "+" :
        return som(a,b)
    elif operator == "-" :
        return sou(a,b)
    elif operator == "*" :
        return prod(a,b)
    elif  operator == "/":
        return  div(a,b)
    else:
        print("operator erreur , try again !")   

print(f"{num1} {operator} {num2} = {clacul(num1,num2)}")

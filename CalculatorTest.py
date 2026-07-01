def Add(a, b):
    return(a + b)
def Sub(a, b):
    return(a - b) 
def Multiply(a, b):
    return(a * b)
def Divide(a, b):
    return(a / b)
print("Pick your choice")
print("1. Add, 2. Substract, 3. Multiply, 4. Substract")
choice = input("Enter your choice : ")
if choice == 1:
    Add
elif choice == 2:
    Sub
elif choice == 3:
    Multiply
elif choice == 4:
    Divide
else:
    print("Error")

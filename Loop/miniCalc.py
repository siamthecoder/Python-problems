a = input("Enter a: ")
a = int(a)
b = input("Enter b: ")
b = int(b)

while True:
    button = input("Enter add/sub: ")
    
    if button == "exit":
        terminate = True
        break
    if button not in ["add", "sub"]:
        print("Erro! Try again")
        continue
    if(button == "add"):
        print("Sum is:", a+b)
    if(button == "sub"):
        print("Result is:", a-b)

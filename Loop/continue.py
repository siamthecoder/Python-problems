while True:
    num = input("Enter a number: ")
    num = int(num)
    if(num == 0):
        break
    if(num < 0):
        print("Enter positive numbers!")
        continue
    print("Square of", num, "is", num*num)


def myfun(x):
    print("inside myfun:", x)
    x = 10
    print("inside myfun:", x)
    
x = 20
myfun(x)
print(x)
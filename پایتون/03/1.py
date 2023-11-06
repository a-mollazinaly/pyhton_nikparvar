print("In The Name OF God")
print("Hello World!")
def set_data():
    c = input("Please set your date (list = l/ dir = d): ")
    if c == "l" : c = []
    if c == "d" : c = {}
    n = int(input("please enter your data number: "))
    for i in range(n):
        key = input("Enter A key: ")
        v = input("Enter Value: ")
        c[key] = v
    print(c)
    

set_data()
input("do you want to exit: y/n ")
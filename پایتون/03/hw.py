print("In The Name Of God!")
print("Hello World!")
print("# He - Will - Come!")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
fathers_name = input("Enter your father name: ")
national_code = input("Enter your national code: ")
birth_date = input("Enter your birth date: ")

hw = dict([("first_name", first_name),("last_name",last_name),("fathers_name",fathers_name),("national_code",national_code),("birth_date",birth_date)])
print(hw)

while True:
    w = input("Enter do you want to continue? (end/continue)")
    if (w == "continue"):
        show = input("Please Enter Your Key: ")
        x = hw[show]
        print(x)
    elif (w == "end"):
        break

input("Do You Want To Exit?")
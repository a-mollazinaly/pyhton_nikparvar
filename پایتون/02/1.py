print("In The Name Of God")
print("Hello World!")
print("He Will Come!")
friends=["Ali","Reza","Seyyed","Emad","Hassan"]
print(friends)
friends.append("Alireza")
print(friends)
x = friends[0]
friends[0] = friends[2]
friends[2] = x
print(friends)
friends.remove("Alireza")
print(friends)
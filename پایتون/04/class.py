fn = input("your fn:")
ln = input("your ln:")
time = int(input("your time: ?week"))
price = int(input("your price: ?tooman"))
if time < 2:
    price = price
elif 2<= time < 8 :
    price = 1.25*price
elif 8 <= time < 8*3 :
    price = 1.4*price
else:
    price = ("we dont frosh!!  :)")
t = {
    "fn" : fn,
    'ln' : ln,
    "price" : price,
}
print(t)

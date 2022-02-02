import datetime
import os



currentdate = datetime.datetime.now()
user = os.getlogin() #currently logged in user on your computer



print("Hello " + user)
print(currentdate.strftime("Date: %d.%m.%Y"))
print(currentdate.strftime("Time: %H:%M:%S"))


print("Area Calculator")
a = float(input("a: "))
b = float(input("b: "))
f = a * b
print("Area: ", f)


print("Counting Feature")

direction = int(input("1 - Forwards, 2 - Backwards: "))
print("")


if direction == 1:
    i = 1
    while i <= 10:
        print(i)
        i = i + 1

elif direction == 2:
    i = 10
    while i >= 1:
        print(i)
        i = i - 1
else:
    print("Unknown Command")





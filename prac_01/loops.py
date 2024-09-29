#a)
for i in range(0, 101, 10):
    print(i, end=" ")
print()

#b)
for i in range(20, 0, -1):
    print(i, end=" ")
print()

#c)
number = int(input("Enter a number: "))
for i in range(0, number):
    print("*", end="")
print()
#d)
number = int(input("Enter a number: "))
for i in range(0, number):
    print("*"*(i+1))
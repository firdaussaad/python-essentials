av = 2
x = int(input("How many candies do you want?:\n"))

i = 1
while i <= x:

    if i > av:
        print("Out of stock")
        break
    print("Candy")
    i = i + 1

print("No more Candy")

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        continue

    print(i)



print("bye")

for i in range(1,101):

    if (i%2!=0):
        pass

    else:
        print(i)


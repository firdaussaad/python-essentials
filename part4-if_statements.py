#!/usr/bin/env python3.6

# "%.2f" to get 2 decimal place

is_hot = False
is_cold = True

if is_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovely day")

print("Its a lovely day")

house_price = 1000000
ten_percent = 1000000 * 0.10
twenty_percent = 1000000 * 0.20

good_credit = True

if good_credit:
    print("You have good credit")
    print("Please pay a 10% deposit of $" + str("%.2f" % ten_percent))
else:
    print("You dont have good credit")
    print("Please pay a 20% deposit of $" + str("%.2f" % twenty_percent))

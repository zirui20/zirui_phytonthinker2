food = []

while True:
    order = str(input("what would you like to order? "))
    if order == "end":
        break

    food.append(order)
    print("You have ordered the following:", food)
    
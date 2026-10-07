def restaurant_bill(name, price, quantity):
    """Calculates the total restaurant bill."""
    total = price * quantity
    print("Customer:", name)
    print("Total Bill:", total)

def seating_arrangements(people):
    """Calculates seating arrangements."""
    if people == 1:
        return 1
    return people * seating_arrangements(people - 1)

name = input("Enter your name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
people = int(input("Enter number of people: "))

restaurant_bill(name, price, quantity)

print(restaurant_bill.__doc__)
print("Seating arrangements:", seating_arrangements(people))
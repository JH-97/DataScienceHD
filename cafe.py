# A program that calculates the total stock value of a cafe

menu = ["Coffee", "Milk", "Cake", "Egg"]
stock = {"Coffee": 1,"Milk": 1,"Cake": 1,"Egg": 1}
price = {"Coffee": 5,"Milk": 6,"Cake": 7,"Egg": 8}
total_stock = 0

# loop for each element in menu list, multiply its stock level by item price
# cumulatively summing results to get the total stock
for items in range(len(menu)):
    total_stock += stock[menu[items]] * price[menu[items]]

print(total_stock)
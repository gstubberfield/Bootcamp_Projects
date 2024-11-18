# Create a list called menu and add items sold in a cafe

menu = ["Coffee", "Cake", "Ice Cream", "Hot Chocolate"]

# Create a dictionary called stock
# Add the stock value for each item on menu

stock = {
    "Coffee" : 250,
    "Cake" : 360,
    "Ice Cream" : 500,
    "Hot Chocolate" : 120
}

# Create dictionary called price
# Add prices of each item on menu

price = {
    "Coffee" : 3.20,
    "Cake" : 5.40,
    "Ice Cream" : 3.50,
    "Hot Chocolate" : 4.60
}

# Calculate the worth of total_stock in cafe
# Loop through dictionaries and lists
# Set list items as keys to access corresponding stock and price

total_stock = 0
for value in menu:
    total_stock += stock[value] * price[value]
print ("The worth of the total stock is £", total_stock)
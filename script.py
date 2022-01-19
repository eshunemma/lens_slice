# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#count occurances of 2 in prices
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

#length of toppings list
num_pizzas = len(toppings)
#print(num_pizzas)

print("We sell "+ str(num_pizzas) + " different kinds of pizza!")

# two-dimentional list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

#sort list in accending order
pizza_and_prices.sort()

# storing cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# most expenssive pizza
priciest_pizza = pizza_and_prices[-1]

# removing last pizza from list
pizza_and_prices.pop()

# adding new item
pizza_and_prices.insert(4, [2.5, "peppers"])

# first 3 lowest prices
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
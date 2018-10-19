#Len's Slice

#In this project, you will be working for a pizza place called Len's Slice. You will be using your newfound knowledge of lists to keep track of sales data for the store, and help your manager do some research. To complete the project, you will need to understand how to perform basic operations on lists, like len() and slicing. On the way, you'll refresh your knowledge of basic Python syntax. If you get stuck or confused, remember that your Slack community is there to help!

#This project is not graded and you do not need to submit it anywhere. If you would like to check your results, the solution code can be found here.


toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We sell "+str(num_pizzas)+" pizzas!")

pizzas = list(zip(prices, toppings))
pizzas.sort()

print(pizzas)

cheapest_pizza = pizzas[0]
three_cheapest = pizzas[:3]

print(cheapest_pizza)
print(three_cheapest)

num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)

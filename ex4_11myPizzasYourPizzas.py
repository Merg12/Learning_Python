myPizzas = ["pepperoni", "thin crust", "parmesan", "cheese"]
friend_pizzas = myPizzas[:]

myPizzas.append("meatball")
print("my favorite pizzas are: ")
for ingredient in myPizzas:
    print(ingredient)

friend_pizzas.append("pineapple")
print("\nmy friend's favorite pizzas are: ")
for ingredient in myPizzas:
    print(ingredient)


from content import pantry, recipes

menu = {}

shopping_list = {}

for index, material in enumerate(recipes):
    menu[str(index + 1)] = material

while True:

    print("Choose which food you want to make")
    print("----------------------------------")

    for index, food in menu.items():
        print(f"{index}: {food}")

    choice = input(">>> ")

    if choice == '0':
        break
    elif choice in menu:
        selected_choice = menu[choice]
        ingredients = recipes[selected_choice]
        print(f"Your selected choice is {selected_choice}")
        print(f"Checking for the ingredients to make {selected_choice}...")
        print(ingredients)
        for food, quantity in ingredients.items():
            available_quantity = pantry.get(food, 0)
            if quantity <= available_quantity:
                print(f"the quantity of {food} in store is: {available_quantity}")
                print(f"{food} OK")
            elif quantity > available_quantity:
                purchase = quantity - available_quantity
                print(f"the quantity of {food} in store is: {available_quantity}")
                print(f"this is insufficient, you need to buy: {quantity} {food}")
                shopping_list[quantity] = food

print("Below is your shopping list")

for things in shopping_list.items():
    print(things)





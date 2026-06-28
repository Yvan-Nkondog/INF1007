
# Write a script that stores the ingredients of a different
# meals, inside a unique programming structure.
# Write a second program that displays the ingredients of a
# meal (prior verification meal presence in meal book mandatory).

def store_meal_constituents(storing_structure: dict) -> dict:
    meal_name = (input("Please, enter the name of the meal : ")).upper()
    while meal_name in storing_structure:
        print(f"Please, select another name, the name {meal_name} already exist.")
        meal_name = (input("Please, enter the name of the meal : ")).upper()
    storing_structure[meal_name] = []
    ingredient = (input("Please, enter the first ingredient : ")).upper()
    storing_structure[meal_name].append(ingredient)
    adding_ingredient = input("Do you want to add another ingredient ? yes / no ")
    while(adding_ingredient == "yes"):
        ingredient = (input("Please, enter the next ingredient : ")).upper()
        storing_structure[meal_name].append(ingredient)
        adding_ingredient = input("Do you want to add another ingredient ? yes / no ")
    return storing_structure


def display_ingredients(storing_structure: dict, meal_name: str) -> dict:
    if meal_name.upper() in storing_structure:
        return {meal_name.upper(): storing_structure[meal_name.upper()]}
    return f"The meal selected does not exist in the book."


if __name__ == "__main__":
    meal_book1 = {}
    meal_name1 = "CAKE"
    meal_name2 = "TOMATO SAUCE"
    meal_book2 = store_meal_constituents(meal_book1)
    print(display_ingredients(meal_book1, meal_name1))
    print(display_ingredients(meal_book1, meal_name2))
    meal_book2 = {"RICE": ["WATER, CLEAN RICE, OIL, SALT"]}
    meal_book2 = store_meal_constituents(meal_book2)
    print(display_ingredients(meal_book2, "rice"))
    print(display_ingredients(meal_book2, meal_name2))
    
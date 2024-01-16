"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""

from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name = input("Name: ")

    print("Origin:")
    for i in range(len(Food.ORIGIN)):
        print(f" {i} {Food.ORIGIN[i]}")

    origin = int(input(": "))

    vegetarian_input = input("Vegetarian (Y/N): ")

    if vegetarian_input.upper() == 'Y':
        is_vegetarian = True
    else:
        is_vegetarian = False

    calories = int(input("Calories: "))

    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    components = line.split('|')

    name = components[0]
    origin = int(components[1])
    is_vegetarian_str = components[2].lower()

    if is_vegetarian_str == 'true':
        is_vegetarian = True
    else:
        is_vegetarian = False

    calories = int(components[3])

    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """

    foods = []

    for line in file_variable:

        food_example = read_food(line.strip())

        foods.append(food_example)

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for food_instance in foods:
        print(f"{food_instance.name}|{food_instance.origin}|"
              f"{food_instance.is_vegetarian}|{food_instance.calories}",
              file=file_variable)

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = [food_instance for food_instance in foods if food_instance.is_vegetarian]
    return veggies

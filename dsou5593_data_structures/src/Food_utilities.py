"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-01-21"
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

    veggies = [
        food_instance for food_instance in foods if food_instance.is_vegetarian]
    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    origins = [food for food in foods if food.origin == origin]

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    total_calories = sum(food.calories for food in foods)
    num_items = len(foods)

    avg = total_calories / num_items if num_items > 0 else 0

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    matching_foods = [food for food in foods if food.origin == origin]

    total_calories = sum(food.calories for food in matching_foods)
    num_items = len(matching_foods)

    avg = total_calories / num_items if num_items > 0 else 0

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    sorted_foods = sorted(foods, key=lambda food: food.name)

    max_name_length = max(len(food.name) for food in sorted_foods)
    max_origin_length = max(len(str(food.origin)) for food in sorted_foods)
    max_calories_length = len("Calories")

    max_vegetarian_length = len("Vegetarian")

    print(f"{ 'Food':<{max_name_length}}  {'Origin':<{max_origin_length}}  {'Vegetarian':<{max_vegetarian_length}}  {'Calories':<{max_calories_length}}")
    print("-" * (max_name_length + max_origin_length +
          max_vegetarian_length + max_calories_length + 6))

    for food in sorted_foods:
        print(
            f"{food.name:<{max_name_length}}  {Food.ORIGIN[food.origin]:<{max_origin_length}}  {str(food.is_vegetarian):<{max_vegetarian_length}}  {food.calories:<{max_calories_length}}")

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []

    for food in foods:
        origin_condition = origin == -1 or food.origin == origin
        max_cals_condition = max_cals == 0 or food.calories <= max_cals
        is_veg_condition = not is_veg or food.is_vegetarian  # Corrected attribute name

        if origin_condition and max_cals_condition and is_veg_condition:
            result.append(food)

    return result

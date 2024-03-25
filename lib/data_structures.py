spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    """
    Returns a list of names of spicy foods.
    
    Parameters:
        spicy_foods (list): A list of dictionaries representing spicy foods.
        
    Returns:
        list: A list containing names of all spicy foods.
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Returns a list of dictionaries representing spicy foods with heat level greater than 5.
    
    Parameters:
        spicy_foods (list): A list of dictionaries representing spicy foods.
        
    Returns:
        list: A list containing dictionaries of spicy foods with heat level greater than 5.
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """
    Prints information about each spicy food to the terminal.
    
    Parameters:
        spicy_foods (list): A list of dictionaries representing spicy foods.
    """
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns a dictionary representing a spicy food with a specific cuisine.
    
    Parameters:
        spicy_foods (list): A list of dictionaries representing spicy foods.
        cuisine (str): The cuisine to search for.
        
    Returns:
        dict: A dictionary representing a spicy food with the specified cuisine, or None if not found.
    """
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """
    Prints information about spiciest foods to the terminal.
    
    Parameters:
        spicy_foods (list): A list of dictionaries representing spicy foods.
    """
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    """
    Returns the average heat level of all spicy foods.
    
    Parameters:
        spicy_foods (list): A list of dictionaries representing spicy foods.
        
    Returns:
        int: The average heat level.
    """
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    """
    Adds a new spicy food to the list of spicy foods.
    
    Parameters:
        spicy_foods (list): A list of dictionaries representing spicy foods.
        spicy_food (dict): A dictionary representing the new spicy food to be added.
        
    Returns:
        list: The updated list of spicy foods.
    """
    spicy_foods.append(spicy_food)
    return spicy_foods

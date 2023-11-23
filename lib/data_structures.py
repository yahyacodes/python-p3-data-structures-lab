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
    names = [food['name'] for food in spicy_foods]
    return names
spicy_foods_names = get_names(spicy_foods)
print(spicy_foods_names)
    


def get_spiciest_foods(spicy_foods):
    names = [food for food in spicy_foods if food.get('heat_level', 0) > 5]
    return names
spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)

def print_spicy_foods(spicy_foods):
   for spicy_food in spicy_foods:
        name = spicy_food.get('name', 'Unknown Food')
        cuisine = spicy_food.get('cuisine', 'Unknown Cuisine')
        heat_level = spicy_food.get('heat_level', 0)
        heat_emojis = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

spicy_print = print_spicy_foods(spicy_foods)
print_spicy_foods(spicy_foods)
print(spicy_print)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get('heat_level', 0) > 5]
    print_spicy_foods(spiciest_foods)
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food.get('heat_level', 0) for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)
    if num_spicy_foods == 0:
        return 0
    average_heat = total_heat / num_spicy_foods
    return int(average_heat)
ans = get_average_heat_level(spicy_foods)
print(ans)

def create_spicy_food(spicy_foods, spicy_food):
    update_spicy_foods = spicy_foods.copy()
    update_spicy_foods.append(spicy_food)
    return update_spicy_foods

new_spicy_foods = [
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
            {
                "name": "Griot",
                "cuisine": "Haitian",
                "heat_level": 10,
            },
        ]

update_spicy_foods = create_spicy_food(new_spicy_foods, new_spicy_foods)
print(update_spicy_foods)
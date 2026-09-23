# reverse-mapping-test.py
# Task: We have a dict where the KEY is a restaurant name and the VALUE
# is a LIST of recipe / cuisine styles (a single restaurant can serve
# multiple styles).
# We want the REVERSE mapping where the KEY is a style and the VALUE is
# the list of restaurants that offer that style.

# ----------------------------------------------------------------------
# ORIGINAL:  restaurant name  ->  [list of styles]
# ----------------------------------------------------------------------
restaurant_to_styles = {
    "Spice Villa":      ["Indian", "Chinese"],
    "Pasta House":      ["Italian"],
    "Dragon Wok":       ["Chinese", "Japanese"],
    "Curry Leaf":       ["Indian"],
    "Sushi Zen":        ["Japanese"],
    "Bella Napoli":     ["Italian", "Mexican"],
    "Taco Fiesta":      ["Mexican"],
    "Golden Panda":     ["Chinese"],
    "Tandoori Nights":  ["Indian", "Italian"],
    "Ramen Bar":        ["Japanese", "Chinese"],
    "El Sombrero":      ["Mexican", "Indian"],
    "Olive Garden Co":  ["Italian"],
}


# ----------------------------------------------------------------------
# SAME DATA, LIST VERSION:  a list of records, each a dict with
# "restaurant" and "styles" keys.
# ----------------------------------------------------------------------
restaurant_list = [
    {"restaurant": "Spice Villa",     "styles": ["Indian", "Chinese"]},
    {"restaurant": "Pasta House",     "styles": ["Italian"]},
    {"restaurant": "Dragon Wok",      "styles": ["Chinese", "Japanese"]},
    {"restaurant": "Curry Leaf",      "styles": ["Indian"]},
    {"restaurant": "Sushi Zen",       "styles": ["Japanese"]},
    {"restaurant": "Bella Napoli",    "styles": ["Italian", "Mexican"]},
    {"restaurant": "Taco Fiesta",     "styles": ["Mexican"]},
    {"restaurant": "Golden Panda",    "styles": ["Chinese"]},
    {"restaurant": "Tandoori Nights", "styles": ["Indian", "Italian"]},
    {"restaurant": "Ramen Bar",       "styles": ["Japanese", "Chinese"]},
    {"restaurant": "El Sombrero",     "styles": ["Mexican", "Indian"]},
    {"restaurant": "Olive Garden Co", "styles": ["Italian"]},
]


def print_restaurant_to_styles(data):
    print("===== ORIGINAL: restaurant -> styles =====")
    print(f"{'Restaurant':<18} {'Styles'}")
    print("-" * 45)
    for restaurant, styles in data.items():
        print(f"{restaurant:<18} {', '.join(styles)}")


def reverse_mapping(data):
    """Build style -> [restaurants] from restaurant -> [styles]."""
    reversed_map = {}
    for restaurant, styles in data.items():
        # Each restaurant has a LIST of styles; loop over each style.
        for style in styles:
            # If we have not seen this style yet, start a new empty list.
            if style not in reversed_map:
                reversed_map[style] = []
            # Add this restaurant under the style.
            reversed_map[style].append(restaurant)
    return reversed_map


def print_style_to_restaurants(data):
    print("\n===== REVERSED: style -> restaurants =====")
    print(f"{'Style':<10} {'Restaurants'}")
    print("-" * 55)
    for style, restaurants in data.items():
        print(f"{style:<10} {', '.join(restaurants)}")


# ----------------------------------------------------------------------
# LIST VERSION helpers
# ----------------------------------------------------------------------
def print_restaurant_list(data):
    print("\n===== ORIGINAL (LIST VERSION): restaurant -> styles =====")
    print(f"{'Restaurant':<18} {'Styles'}")
    print("-" * 45)
    for record in data:
        print(f"{record['restaurant']:<18} {', '.join(record['styles'])}")


def reverse_mapping_from_list(data):
    """Build style -> [restaurants] from the list-of-records version."""
    reversed_map = {}
    for record in data:
        restaurant = record["restaurant"]
        for style in record["styles"]:
            if style not in reversed_map:
                reversed_map[style] = []
            reversed_map[style].append(restaurant)
    return reversed_map


if __name__ == "__main__":
    # ---- DICT VERSION ----
    print_restaurant_to_styles(restaurant_to_styles)
    style_to_restaurants = reverse_mapping(restaurant_to_styles)
    print_style_to_restaurants(style_to_restaurants)

    print("\nHow many restaurants per style:")
    for style, restaurants in style_to_restaurants.items():
        print(f"  {style:<10}: {len(restaurants)}")

    # ---- LIST VERSION ----
    print("\n" + "=" * 45)
    print_restaurant_list(restaurant_list)
    style_to_restaurants_2 = reverse_mapping_from_list(restaurant_list)
    print_style_to_restaurants(style_to_restaurants_2)

    print("\nHow many restaurants per style (list version):")
    for style, restaurants in style_to_restaurants_2.items():
        print(f"  {style:<10}: {len(restaurants)}")

def read_recipes(filename):
    """
 Читаем рецепты, создаем словарь
    """
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            count = int(file.readline())
            ingredients_list = []
            for i in range(count):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredients_list.append({'ingredient_name': ingredient_name.strip(),
                                         'quantity': int(quantity),
                                         'measure': measure.strip()})
            cook_book[dish_name] = ingredients_list
            file.readline()
    return cook_book

filename = "recipes.txt"
cook_book = read_recipes(filename)
print(cook_book)
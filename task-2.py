from collections import defaultdict

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    '''
    Функция для получения списка покупок на 7 человек из всех блюд.
    Отход от примера в дз для разнообразия
    '''

    shop_list = defaultdict(lambda: {'measure': '', 'quantity': 0})

    for dish in dishes:
        for ingredient in cook_book.get(dish, []):
            item = shop_list[ingredient['ingredient_name']]
            item.update({'measure': ingredient['measure'],
                         'quantity': item['quantity'] + ingredient['quantity'] * person_count})

    return dict(shop_list)


dishes = ['Запеченный картофель', 'Омлет', 'Утка по-пекински']
person_count = 7

shop_list = get_shop_list_by_dishes(dishes, person_count)

print(shop_list)
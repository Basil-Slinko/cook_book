from pprint import pprint
import os



def get_dictionary():
    folder_path = os.getcwd()
    path = f"{folder_path}/recipes.txt"
    cook_book = {}

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            name_dish = line.strip()
            amount_ingredients_in_dish = int(file.readline().strip())

            ingredient_list = []
            for ingredient in range(amount_ingredients_in_dish):
                dict_ingredient = {'ingredient_name': None, 'quantity': None, 'measure': None}
                ingredient_name, quantity, measure = file.readline().strip().split(" | ")
                dict_ingredient['ingredient_name'] = ingredient_name
                dict_ingredient['quantity'] = quantity
                dict_ingredient['measure'] = measure
                ingredient_list.append(dict_ingredient)

            file.readline()

            cook_book[name_dish] = ingredient_list
    return cook_book



def get_shop_list_by_dishes(dishes, person_count):
  cook_book = get_dictionary()
  quantity_of_ingredients_for_dishes = {}

  for name_dish in dishes:
    for names, ingredients in cook_book.items():
      for ingredients_and_quantity in ingredients:
        if name_dish == names:
          ingredient_names = ingredients_and_quantity['ingredient_name']
          if ingredient_names not in quantity_of_ingredients_for_dishes.keys():
            quantity_of_ingredients_for_dishes[ingredient_names] = \
              {'measure': ingredients_and_quantity['measure'],
               'quantity': int(ingredients_and_quantity['quantity']) * person_count}
          else:
            quantity_of_ingredients_for_dishes[ingredient_names] = \
              {'measure': ingredients_and_quantity['measure'],
               'quantity': ((int(ingredients_and_quantity['quantity'])) +
                            (int(ingredients_and_quantity['quantity']))) * person_count}

  pprint(quantity_of_ingredients_for_dishes)



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



pprint(get_dictionary())


def f_read():
    cook_book_dict = {}
    with open('recipelist.txt') as f:
        for line in f:
            dish = line.strip()
            ingredients_number = f.readline().strip()
            n = int(ingredients_number)
            ingredient_dict = {}
            ingredient_dict_list = []

            for lines in range(n):
                ingredient = f.readline().strip().split(' | ')
                ingredient_dict['ingredient_name'] = ingredient[0]
                ingredient_dict['quantity'] = ingredient[1]
                ingredient_dict['measure'] = ingredient[2]
                ingredient_dict_list.append(ingredient_dict.copy())

            cook_book_dict[dish] = ingredient_dict_list
            f.readline()
    return cook_book_dict


cook_book_dict = f_read()
print(cook_book_dict)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_dict = {}
    for dish in dishes:
        for ingredient in cook_book_dict[dish]:
            ingredient_dict = ingredient
            # print(ingredient_dict)
            if ingredient_dict['ingredient_name'] not in shop_list_dict:
                shop_list_dict[ingredient_dict['ingredient_name']] = {'measure': ingredient_dict['measure'], 'quantity': int(ingredient_dict['quantity']) * person_count}
            else:
                shop_list_dict[ingredient_dict['ingredient_name']]['quantity'] += int(ingredient_dict['quantity']) * person_count
    print(shop_list_dict)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

import os


def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingredients = {}
                ingr = f.readline().strip()
                ingredients['ingredient_name'], ingredients['quantity'], ingredients['measure'] = ingr.split('|')
                ingredients['quantity'] = int(ingredients['quantity'])
                ing_list.append(ingredients)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book


filename = "recipes.txt"
cook_book = read_cookbook()
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Блюда нет в списке!"\n')
    return ingr_list

print(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=4))


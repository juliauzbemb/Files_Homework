from pprint import pprint


def get_cook_book(file_name):
    global cook_book
    cook_book = dict()
    with open(file_name) as file:
        for line in file:
            dish_name = line.strip()
            counter = int(file.readline())
            temp_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_list.append(
                    {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure.strip()}
                )
            cook_book[dish_name] = temp_list
            file.readline()
    return cook_book


pprint(get_cook_book("recipes.txt"))
print()


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = dict()
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredients in cook_book[dish_name]:
                measure_quantity_list = dict()
                if ingredients["ingredient_name"] not in ingredients_list:
                    measure_quantity_list["measure"] = ingredients["measure"]
                    measure_quantity_list["quantity"] = ingredients["quantity"] * person_count
                    ingredients_list[ingredients["ingredient_name"]] = measure_quantity_list
                else:
                    ingredients_list[ingredients["ingredient_name"]]["quantity"] = \
                        ingredients_list[ingredients["ingredient_name"]]["quantity"] + ingredients[
                            "quantity"] * person_count
        else:
            print(f'Блюда нет в кулинарной книге!')
    return ingredients_list


pprint(get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 2))
print()


def rewrite_file():
    path1 = "1.txt"
    path2 = "2.txt"
    path3 = "3.txt"
    list_of_files = [path1, path2, path3]
    files_structure = dict()
    for items in list_of_files:
        list_of_str_text = []
        with open(items, "r", encoding='utf-8') as file:
            file = file.readlines()
            len_file = len(file)
            list_of_str_text.append(len_file)
            list_of_str_text.append(file)
        files_structure[items] = list_of_str_text

    sorted_values = sorted(files_structure.values())
    sorted_dict = {}
    for elements in sorted_values:
        for key in files_structure.keys():
            if files_structure[key] == elements:
                sorted_dict[key] = files_structure[key]
                break

    with open("final.txt", "w", encoding='utf-8') as final_file:
        for key, values in sorted_dict.items():
            file_name = key
            str_quantity = str(values[0])
            text = values[1]
            text = "".join(text)
            final_file.write(file_name + "\n" + str_quantity + "\n" + text.strip() + "\n")
        return final_file


print(rewrite_file())

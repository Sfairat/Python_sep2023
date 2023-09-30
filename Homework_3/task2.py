# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление

def hashable_objects(**kwargs):
    temp_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, frozenset)):
            value = str(value)
        temp_dict[value] = key
    return temp_dict


print(hashable_objects(things=["rope", "stone"]))
print(hashable_objects(animals={1: "cat", 2: "dog", 3: "rabbit"}))

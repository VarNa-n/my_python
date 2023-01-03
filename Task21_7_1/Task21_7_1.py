from cat import Cat
import json

# Загружаем взятый с сайта response с выводом всех животных (не знаю, как взять всё, если вывод разбит на страницы?)
with open('pets.json', encoding='utf8') as f:
    templates = json.load(f)

# объявляем массив объектов Cat
cats = []
# По всем элементам json-а
for el in templates['results']:
    for key in el:
        # Если вид животного - кошка, создаем объект класса Cat и добавляем его в массив
        if key == 'species' and el[key]['code'] == 'cat':
            cat = Cat(el['name'], el['gender']['code'], el['age'])
            cats.append(cat)

age = input("Введите возраст кошки (0..20): ")
try:
    age = int(age)
except ValueError:
    age = -1
name = input("Введите кличку кошки:")
gender = input("Введите пол кошки (m/g):")

CountCat = {"Имя": {}, "Пол": {}, "Возраст": {}}
for el in cats:
    flag = 1  # 0 - не подходит, 1 - подходит
    # Если возраст указан и совпадает или возраст не указан
    if age >= 0 and age == el.age or age == -1:
        flag *= 1
    else:
        flag *= 0
    # Если имя указано и совпадает или имя не указано
    if name and name == el.name or not name:
        flag *= 1
    else:
        flag *= 0
    # Если пол указан и совпадает или пол не указан
    if gender and gender == el.gender or not gender:
        flag *= 1
    else:
        flag *= 0
    # Если подходит
    if flag == 1:
        print(f"Кличка: {el.name}, пол: {el.gender}, возраст: {el.age}")

    # Подсчитаем количество питомцев по всем значениям параметров (статистика)
    if el.name in CountCat['Имя']:
        CountCat['Имя'][el.name] += 1
    else:
        CountCat['Имя'][el.name] = 1

    if el.gender in CountCat['Пол']:
        CountCat['Пол'][el.gender] += 1
    else:
        CountCat['Пол'][el.gender] = 1

    if el.age in CountCat['Возраст']:
        CountCat['Возраст'][el.age] += 1
    else:
        CountCat['Возраст'][el.age] = 1

# Вывод статистики
print("ИТОГО: ")
for param in CountCat:
    print(" ", param)
    for val in CountCat[param]:
        print(f'   {val} - {CountCat[param][val]} питомец(-мца/-мцев)')

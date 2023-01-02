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
        # Если вид животного - кошка, создаем объект класса Cat и добавлем его в массив
        if key == 'species' and el[key]['code'] == 'cat':
            cat = Cat(el['name'], el['gender']['code'], el['age'])
            cats.append(cat)

age = input("Введите возраст кошки (0..20): ")
try:
    age = int(age)
except ValueError:
    age = -1
name = input("Введите имя кошки:")
gender = input("Введите пол кошки (m/g):")

for el in cats:
    flag = 1 # 0 - не подходит, 1 - подходит
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

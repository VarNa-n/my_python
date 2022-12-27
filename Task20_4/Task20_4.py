# Функция убирает двойные и более пробелы из переданной строки
def DelDoubleSpace(f_text):
    def wrapper(text):
        t = f_text(text)
        t_new = t.replace("  ", " ")
        while t != t_new:
            t = t_new
            t_new = t.replace("  ", " ")
        return t
    return wrapper

@DelDoubleSpace
# Функция меняет все символы пунктуации в строке на пробелы, а декоратор DelDoubleSpace уберет из нее все лишние пробелы
def ChangeText(text):
    for symb in '"\',.-?!^$()/\n':
        text = text.replace(symb, " ")
    return text

def TwoPopWordsMore3Symb(list):
    dict = {}
    max_word = ""
    for i in list:
        if len(i) > 3:
            i = i.lower()
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        if len(i) > len(max_word):
            max_word = i

    pop_word = sorted(dict.values())[-1]
    for key in dict:
        if dict[key] == pop_word:
            return key, max_word

    return "Не найдено", max_word

# Main
f_name = input("Введите имя файла: ")
# Проверка, что файл есть
try:
    # Если есть, читаем файл в переменную str_f
    with open(f_name, encoding="utf-8") as F:
        str_f = F.read()
except FileNotFoundError:
    # Если файл не найден, сообщение об ошибке
    print(f"File {f_name} not found")
else:
    # ChangeText возвращает подготовленную строку только из слов, разделенных пробелами
    list = ChangeText(str_f).split()
    # TwoPopWordsMore3Symb возвращает кортеж из 2-элементов: самое популярное и самое длинное слова
    result = TwoPopWordsMore3Symb(list)
    print(f'Чаще всего встречается слово: "{result[0]}", самое длинное слово: "{result[1]}"')

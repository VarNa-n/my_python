try:  # Добавляем конструкцию try-except для отлова нашей ошибки
    num = int(input("Введите число: "))
except ValueError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
    print("Вы ввели неправильное число")
else :
    print("Вы ввели", num)
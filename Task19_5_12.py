def e():
     n = 1
     while True:
#         print(n, (1 + 1/n)**n)
         yield (1 + 1/n)**n
         n += 1


last = 0
for a in e(): # e() - генератор
 #   print("-- ", a)
    if (a - last) < 0.0000000001: # ограничение на точность
        print(a)
        break # после достижения которого - завершаем цикл
    else:
        last = a # иначе - присваиваем новое значение
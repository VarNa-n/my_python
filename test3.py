L = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(str.lower, L)))
# ['this', 'is', 'lower', 'string']

def pow_(x):
    return x**2


a_list = [1,2,3]
print(list(map(pow_, a_list)))  # [1, 4, 9]

for i in map(pow_, a_list):
   print(i)


# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False

result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]

# map + filter
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive(x): return x > 0

print(some_list)
print(list(map(pow2, filter(positive, some_list))))

other_list = [i**2 for i in some_list if i < 0]
print(other_list)
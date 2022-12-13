def D(a, b, c):
    return b**2 - 4*a*c

def quadratic_solve(a,b,c):
    d = D(a, b, c)
    if d < 0:
        return 'Нет вещественных корней'
    elif d == 0:
        return -b/(2*a)
    else:
        return  ((-b - d**0.5)/(2*a), (-b+- d**0.5)/(2*a))

L = list(map(float, input("Введите через пробел a b c: ").split()))
print(quadratic_solve(*L))
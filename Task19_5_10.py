def mirr_num(num):
    if num // 10 == 0:
        return num
    return str(num % 10) + str(mirr_num(num // 10))

print(mirr_num(587))

def mirror_skillF(a, res=0):
    if a == 0:
        return res
    else:
        return mirror_skillF(a // 10, res * 10 + a % 10)

print(mirror_skillF(587))
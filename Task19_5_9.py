def min_list(lst):
    # если в списке 1 эл-т, его и возвращаем
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] < lst[1] :
            lst[1] = lst[0]
        return min_list(lst[1::])

def min_list_skillF(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list_skillF(L[1:]) else min_list_skillF(L[1:])

min = min_list([0, 4, 1, 5, -1])
print(min)

min = min_list_skillF([0, 4, 1, 5, -1])
print(min)

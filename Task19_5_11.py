def equal_skillF(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal_skillF(N // 10, S - N % 10)

print(equal_skillF(258, 15))

def equal(N, S):
    if S < 0:
        return False
    if N < 10 and N == S:
        return True
    elif N < 10 and N != S:
        return False
    else:
        return equal(N // 10, S - N % 10)

print(equal(258, 17))
# Нахождение НОД

def nodWhile(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

print(f"С помощью while: {nodWhile(75, 30)}")

def nodRec(a, b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return nodRec(a % b, b)
    else:
        return nodRec(b % b, a)

print(f"С помощью рекурсии: {nodWhile(75, 30)}")

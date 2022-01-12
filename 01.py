# Рекурсия
def req(n):
    print(n)
    if n > 0:
        req(n - 1)


req(5)

# Рекурсии и циклы

# ***** Вывести последовательность от 0 до 4 *****
for i in range(5):
    print(i)

print()
def req(n):
    print(n)
    if n < 4:
        req(n + 1)

req(0)
print()
# ***** Вывести последовательность от 0 до 4 и от 4 до 0 *****
for i in range(5):
    print(i)
for i in range(4, -1, -1):
    print(i)
print()
def req(n):
    print(n)
    if (n < 4):
        req(n + 1)
    print(n)
req(0)

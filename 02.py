# Изменение глубины рекурсии

import sys

# Получаем глубину рекурсии
dep = sys.getrecursionlimit()
print(f"Количество рекурсивных вызовов: {dep}")

# Устанавливаем другое значение
sys.setrecursionlimit(5000)
print(f"Количество рекурсивных вызовов: {sys.getrecursionlimit()}")



# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = int(input("Введите 3х значное число: "))

if a <= 1000 and a >= 99:
    result = a % 10 + a % 100 // 10 + a % 1000 // 100
    print(f"сумма цифр числа {a} = {result}")
else:
    print("Вы ввели не 3х значеное число")
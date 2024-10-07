first = input("Введите число 1: ")
second = input("Введите число 2: ")
third = input("Введите число 3: ")
if first == second and second == third:
    print("Совпадений:", 3)
elif first == second or second == third or first == third:
    print("Совпадений:", 2)
else:
    print("Совпадений:", 0)
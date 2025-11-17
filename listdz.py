operator = input("+, -, *, /: ")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if operator == "+":
    c = a + b
    print(c)
elif operator == "-":
    c = a - b
    print(c)
elif operator == "*":
    c = a * b
    print(c)
elif operator == "/":
    c = a / b
    print(c)
else:
    print("вы вели не верный оператор")

import random
list1 = []
list2 = []
po_list1 = []
po_list2 = []
neg_list1 = []
neg_list2 = []
none1 = []
none2 = []
for i in range(10):

    list1.append(random.randint(-30, 30))
    list2.append(random.randint(-30, 30))
for num in list1:
    if num > 0:
        po_list1.append(num)
for num in list2:
    if num > 0:
        po_list2.append(num)
for num in list1:
    if num < 0:
        neg_list1.append(num)
for num in list2:
    if num < 0:
        neg_list2.append(num)
for num in list1:
    if num == 0:
        none1.append(num)
for num in list2:
    if num == 0:
        none2.append(num)
min1 = min(list1)
max1 = max(list1)
min2 = min(list2)
max2 = max(list2)
print(f"лист 1 {list1}")
print(f"лист 2 {list2}")
print(f"мин лист 1: {min1}")
print(f"макс лист 1: {max1}")
print(f"мин лист 2: {min2}")
print(f"макс лист 2: {max2}")
print(f"позитивные числа list1: {po_list1}")
print(f"негативные числа list1: {neg_list1}")
print(f"позитивные числа list2: {po_list2}")
print(f"негативные числа list2: {neg_list2}")
print(f"нули list1: {none1}")
print(f"нули list2: {none2}")


import random
list1 = []
negative = []
evel1 = []
evel2 = []
not_evel = []
list2 = []
list3 = []
not_evel2 = []
negative2 = []
list4 = []
for i in range(10):
    list1.append(random.randint(-30, 30))
    list3.append(random.randint(-30, 30))
for i in list1:
    if i < 0:
        negative.append(i)
for i in list1:
    if i % 2 == 0:
        evel1.append(i)
for i in list1:
    if i % 2 != 0:
        not_evel.append(i)
for i in list1:
    if i % 3 == 0:
        list2.append(i)
min1 = min(list1)
max1 = max(list1)
list1.sort()
print("листы",list1)
print("Сумму отрицательных чисел",negative)
print("Сумму четных чисел",evel1)
print("Сумму нечетных чисел",not_evel)
print("Произведение элементов с индексами кратными 3",list2)
print("минимальным",min1)
print("максимальным",max1)
#2 задание
print(list3)
for num in list3:
    if num  %  2 == 0:
        evel2.append(num)
for num in list3:
    if num % 2 != 0:
        not_evel2.append(num)
for num in list3:
    if num < 0:
        negative2.append(num)
for num in list3:
    if num > 0:
        list4.append(num)
print(evel2)
print(not_evel2)
print(list4)
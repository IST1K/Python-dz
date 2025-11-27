"""
код номер 2
"""
import random

def prime_my_code(plz):
    list_str = plz.split()
    list_my = []

    for num in list_str:
        num1 = int(num)
        list_my.append(num1)
    list_my.sort()

    new_list_my = []

    for num2 in list_my:
        new = str(num2)
        new_list_my.append(new)

    final_code = " ".join(new_list_my)
    return final_code

list1 = []
for i in range(5):
    list1.append(random.randint(1,100))


random_string = " ".join(str(x) for x in list1)

print(list1)
print(prime_my_code(random_string))
"""
код номер 1
"""
def find_platon(plz5):
    if not plz5:
        return 0
    return plz5.index(min(plz5))
print(find_platon(list1))



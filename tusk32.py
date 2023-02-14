# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import*
n = int(input('введите размер массива n: '))
min = int(input('введите min: '))
max = int(input('введите max: '))
list1 = [randint(1,15) for i in range(n)]
print(list1)
list2 = []
for i in range(n):
    if list1[i] > min and list1[i] < max:
        list2.append(i)    
print(list2)

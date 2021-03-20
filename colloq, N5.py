#!/usr/bin/env python
# coding: utf-8

# In[15]:


a = 'ATGAGTCTATCCT'
b = 'CTGTCTCCTG'
d = 10
d_up = d
d_left = d 
# d_right и d_up надо часто менять с 10 на 0, 
# т.к. их обозначаем для гэпа с конца на верхней и правой строчках

first_row = [0 * i for i in range(len(a) + 1)]
# в оригинале:
# a_row = [-10 * i for i in range (len(a) + 1)]
# необходимо будет обнулить верхнюю строку, 
# т.к. она отвечает за гэпы в начале слов

route = []

# матрица штрафов
DNAfull = [[5, -4, -4, -4], [-4, 5, -4, -4], [-4, -4, 5, -4], [-4, -4, -4, 5]]
dDNA = {['C', 'T', 'A', 'G'][a]: a for a in range(4)}

# движение такое: фиксируем строку, итерируем по столбцам
for i in range(len(b)):
    # следующее условие: как счётчик дойдёт до нижней строки, заменим гэп на 0,
    # т.к. нижняя строка = последняя буква
    if i == len(b)-1: 
        d_right = 0    
    routerow = []
    sec_row = [0]
    # в оригинале sec_row = [-10 * (i + 1)],  
    # чтобы в каждой след.ячейке было на 10 больше, а нам нужно
    # занулить левый столбец
    for j in range(1, len(first_row)):
        # такая же логика для условия, но здесь последние буквы для второго слова
        if j == len(first_row)-1: 
            d_up = 0
        # стандартно выбираем через сравнение, как заполнить ячейку
        maxx = max(sec_row[j - 1] - d_left, 
                   first_row[j] - d_up, 
                   first_row[j - 1] + DNAfull[dDNA[a[j - 1]]][dDNA[b[i]]])      
        
        if maxx == first_row[j - 1] + DNAfull[dDNA[a[j - 1]]][dDNA[b[i]]]:
            routerow.append('D')  # переходим по-диагонали
        elif maxx == first_row[j] - d_up:
            routerow.append('U')  # сверху
        else:
            routerow.append('L')  # слева
        # меняем обратно на нормальный гэп, чтобы для середины было 10
        d_up = d        
        sec_row.append(maxx)

    print(sec_row)
    # сохраняем в основной массив для пути действие, которое совершили
    route.append(routerow)
    # записываем строку в переменную, чтобы не потерять, т.к. работаем
    # только с двумя строками
    first_row = sec_row

print(sec_row[-1])

# идём назад
import numpy as np

route = np.asarray(route)

res_a = ''
res_b = ''

while a != '' and b != '':
    if route[-1, -1] == 'V':
        res_a = '-' + res_a
        res_b = b[-1] + res_b
        b = b[:-1]
        route = route[:-1]
    elif route[-1, -1] == 'L':
        res_a = a[-1] + res_a
        a = a[:-1]
        res_b = '-' + res_b
        route = route[:, :-1]
    else:
        res_a = a[-1] + res_a
        a = a[:-1]
        res_b = b[-1] + res_b
        b = b[:-1]
        route = route[:-1, :-1]

print('-'*len(b)+a+res_a, '-'*len(a)+b+res_b, sep = '\n')


# In[ ]:





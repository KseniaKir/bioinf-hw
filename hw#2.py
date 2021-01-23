#!/usr/bin/env python
# coding: utf-8

# ###### Задача 1
# 
# Ввести список чисел (не обязательно целых), найти их медиану — серединное число при выстраивании по возрастанию, если число элементов нечетно, и среднее арифметическое двух серединных чисел, если число элементов четно.

# In[37]:


import random
n = 0
nums = []
size = int(input('Type the size of the list: '))
print ()

for i in range (size):
    n = random.random()
    nums.append(n)

nums.sort()
pos = size // 2
print ('Sorted list: ', nums, '\n')
if size % 2 != 0:
    print ('Median is: ', nums[pos+1])
else:
    me = ((nums[pos]+nums[pos+1])/2)
    print ('Arithmetic mean is: ', me)


# ###### Задача 2
# 
# Алиса загадала целое число в диапазоне от 0 до 100 (включительно). Угадать это число, используя минимальное количество вопросов вида “верно ли, что загаданное число меньше 𝑥?”.

# In[15]:


import random

Alisa = random.randint(0,100)
x=50
i=0
#print (Alisa)
if Alisa<x:
    x1 = 0
    x2 = 49
elif Alisa>x:
    x1 = 51
    x2 = 100

while i==0:
    if Alisa < x:
        print ("Alisa, is your number lower than {}? Answer yes or no.". format(x))
        print ('Yes', '\n')
        x2=x-1
    elif Alisa > x: 
        print ("Alisa, is your number lower than {}? Answer yes or no.". format(x))
        print ('No', '\n')
        x1=x+1
    else:
        print ("Alisa, is your number {}?". format(x))
        print ("Yes", '\n')
        print ('Gorgeous!')
        i=1
    x = x1+(x2-x1)//2
    #print (x1, x2)


# ###### Задача 3
# 
# Дана отсортированная последовательность из 𝑛 чисел. Придумать алгоритм, определяющий принадлежит ли последовательности заданное число, со сложностью 𝑜(𝑛).

# In[7]:


def num_in(x, num):
    med = len(x) // 2
    x1 = 0
    x2 = len(x) - 1
    while x[med] != num and x1 <= x2:
        if num > x[med]:
            x1 = med + 1
        else:
            x2 = med - 1
        med = (x1 + x2) // 2
    if x1 > x2:
        print("No")
    else:
        print("Yes")   

l = [1, 2, 5, 7, 8, 11, 16]
m = 7
k = 3
num_in (l, m)
num_in (l, k)


# ###### Задача 4
# 
# Ввести список чисел (не обязательно целых), отсортировать их алгоритмом пузырьковой сортировки.

# In[10]:


def bubble(x):
    for k in range (len(x)):
        for i in range (len(x)-1):
            if x[i]>x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return (l)
l = [1, 15, 5, 7, 3, 7, 9, 2]
print(bubble(l))


# ###### Задача 5
# 
# Ввести нуклеотидную последовательность, вывести ее reverse-complement.

# In[6]:


seq = str(input('Enter sequence: '))
seq = seq.upper()
new_seq = ''
p=0
for i in seq:
    if i == 'A':
        new_seq+=("T")
    elif i == 'T':
        new_seq+=("A")
    elif i == 'G':
        new_seq+=("C")
    elif i == 'C':
        new_seq+=("G")
    else:
        print ('Your sequence has the wrong letter!')
        i+=1
if p==0:
    print('Reverse-complement sequence is', new_seq[::-1])


# In[ ]:





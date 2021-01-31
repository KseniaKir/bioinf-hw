#!/usr/bin/env python
# coding: utf-8

# Модифицировать код задачи о платной лестнице, чтобы помимо оптимальной стоимости выводился и сам путь (в виде последовательности слов “одна ступенька”, “две ступеньки”).

# In[27]:


a = [1, 2, 3, 4, 5, 6]
S = [a[0], a[1]]
for i in range(2, len(a)):
    S.append(min(S[i-1], S[i-2]) + a[i])
    if S[i-1]+a[i]<S[i-2]+a[i]:
        print("Прыгаем на 1 ступеньку. Стоимость = ", S[i])
    else:
        print("Прыгаем на 2 ступеньки. Стоимость = ", S[i])

print("Стоимость всех ступеней = ", S)


# Написать программу, принимающую на вход две нуклеотидные последовательности, и вычисляющую score оптимального выравнивания с помощью алгоритма Нидлмана-Вунша, используя матрицу штрафов DNAfull и линейный штраф за гэп (𝑑= 10). Проверить работоспособность на последовательностях из задачи 1.
# К программе из задачи 4 добавить вывод оптимального выравнивания.

# In[3]:


import numpy as np

seq1 = 'CTGTCTCCTG'
seq2 = 'ATGAGTCTCT'

# Make matrices

main_matrix = np.zeros((len(seq1)+1, len(seq2)+1))
match_matrix = np.zeros((len(seq1), len(seq2)))

match_score = 5
mismatch_score = -4
d = 10

for i in range(len(seq2)):
    for j in range(len(seq1)):
        if seq2[i] == seq1[j]:
            match_matrix[j][i] = match_score
        else:
            match_matrix[j][i] = mismatch_score
# print (match_matrix)

# Filling first row and column

for i in range(len(seq1)+1):
    main_matrix[i][0] = -d*(i)
for j in range(len(seq2)+1):
    main_matrix[0][j] = -d*(j)

for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
        main_matrix[i][j] = max (main_matrix[i-1][j-1]+match_matrix[i-1][j-1],
                                 main_matrix[i-1][j]-d,
                                 main_matrix[i][j-1]-d)
print (main_matrix, '\n')

# Traceback

seq1_align = ''
seq2_align = ''
i_back=len(seq1)
j_back=len(seq2)


while(j_back > 0 and i_back > 0):
    score = main_matrix[i_back][j_back]
    score_diag = main_matrix[i_back-1][j_back-1]
    score_up = main_matrix[i_back-1][j_back]
    score_left = main_matrix[i_back][j_back-1]
    
    if score == score_diag+match_matrix[i_back-1][j_back-1]:
            seq1_align += seq1[i_back-1]
            seq2_align += seq2[j_back-1]
            i_back -=1
            j_back -=1
    elif score == score_up - d:
            seq1_align += seq1[i_back-1]
            seq2_align += '-'
            i_back -=1
    else:
        seq2_align += seq2[j_back-1]
        seq1_align += '-'
        j_back -=1

# As we go from the last symbol

print(seq2_align[::-1])
print(seq1_align[::-1])


# 

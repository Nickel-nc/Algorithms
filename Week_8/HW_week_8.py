
# coding: utf-8

# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

# In[18]:


import hashlib
S = str(input("Введите строку : "))
 
print(f" Строка {S} имеет длину {len(S)} сиволов.")
print()
print(f"Строка содержит следующие подстроки")
print()
 
subs_set = set()
# subs_dict = {}
for i in range(len(S)):
    for j in range(len(S)-1 if i == 0 else len(S), i, -1):
        subs_set.add(hash(S[i:j]))
        print(f"Подстрока {S[i:j]}")

 
print()
print("Всего подстрок:", len(subs_set))


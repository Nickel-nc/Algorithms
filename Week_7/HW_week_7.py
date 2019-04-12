
# coding: utf-8

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


# В рамках задания использованы несколько реализаций алгоритма и произведено сравнение их быстродействия 
import random
import timeit
import cProfile

# Создаем массив, задаем его длину
data_uns = []
m_len = 20

# Заполняем массив случайными числами
for i in range(m_len):
    buffer = random.randint(-100,100)
    data_uns.append(buffer)
print(f"Исходный массив: {data_uns}")
print()

# Для каждой реализации алгоритма создаем свою переменную, в которой будет произведена сортировка
d1 = data_uns
d2 = data_uns
d3 = data_uns
d4 = data_uns

# Первый метод заимствован из материалов урока
def bubble_sort1(a):
    a = d1
    for k in range(len(a) - 1, 0, -1):
        for i in range(k):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    # print(a)
    return a

# Во втором методе использовался цикл while. Время выполнения этого варианта, в среднем в 2 раза дольше, чем 1-го варианта
def bubble_sort2(a):
    a = d2
    i = 0
    while i < len(a) - 1:
        j = 0
        while j < len(a) - 1 - i:
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            j += 1
        i += 1
    return a

# В третьем варианте используется флаг завершения сортировки. По быстродействию на порядок быстрее первого 
def bubble_sort3(a):
    not_complete = True
    while not_complete:
        not_complete = False
        for i in range(len(a) - 1):
            if i == len(a)-1: i = 0
            elif a[i] > a[i+1]:                
                a[i], a[i+1] = a[i+1], a[i]
                not_complete = True
    return a

# Четвертый вариант представляет собой оптимизированный 3-й вариант и наиболее быстродейственнен. 
# В данном подходе внутренний цикл может не итерируется по последним n-1 элементам при запуске в течение n-го раза, т.к. они уже отсортированы
def bubble_sort4(a):
    for i in reversed(range(len(a))):
        finished = True
        for j in range(i):
            if a[j] > a[j + 1]:
                aq[j], a[j + 1] = a[j + 1], a[j]
                finished = False
        if finished:
            break
    return a

print(f"Сортированный массив #1: {bubble_sort1(d1)}")
print(f"Сортированный массив #2: {bubble_sort1(d2)}")
print(f"Сортированный массив #3: {bubble_sort3(d3)}")
print(f"Сортированный массив #4: {bubble_sort3(d4)}")
print()

"""В текущей конфигурации Cprofile не дал показательных результатов
def main():
    bubble_sort1(d1)
    bubble_sort2(d2)
    bubble_sort3(d3)
    bubble_sort4(d4)
    
cProfile.run("main()")
"""

t1 = timeit.timeit("bubble_sort1(d1)", setup="from __main__ import bubble_sort1, d1", number=10000)
print(f"Время выполнения 10 000 циклов алгоритма 1: {round(t1,3)} sec")

t2 = timeit.timeit("bubble_sort2(d2)", setup="from __main__ import bubble_sort2, d2", number=10000)
print(f"Время выполнения 10 000 циклов алгоритма 2: {round(t2,3)} sec")

t3 = timeit.timeit("bubble_sort3(d3)", setup="from __main__ import bubble_sort3, d3", number=10000)
print(f"Время выполнения 10 000 циклов алгоритма 3: {round(t3,3)} sec")

t4 = timeit.timeit("bubble_sort4(d4)", setup="from __main__ import bubble_sort4, d4", number=10000)
print(f"Время выполнения 10 000 циклов алгоритма 4: {round(t4,3)} sec")


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

data_uns2 = []
m_len = 20
t=0
# Заполняем массив случайными числами
for i in range(m_len):
    buffer = round(random.uniform(0,50), 1)
    data_uns2.append(buffer)
print(f"Исходный массив:\n{data_uns2}")
print()


def merge_sort(a):
    n = len(a)
    if n < 2:
        return a
    
    l = merge_sort(a[:n//2])
    r = merge_sort(a[n//2:n])
    
    i = j = 0
    result = []
    
    while i < len(l) or j < len(r):
        if not i < len(l):
            result.append(r[j])
            j += 1
        elif not j < len(r):
            result.append(l[i])
            i += 1
        elif l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    return result
                  
        
print(f"Сортированный массив:\n{merge_sort(data_uns2)}")
print()
t3 = timeit.timeit("merge_sort(data_uns2)", setup="from __main__ import merge_sort, data_uns2", number=10000)
print(f"Время выполнения 10 000 циклов алгоритма #3: {round(t3,3)} sec")


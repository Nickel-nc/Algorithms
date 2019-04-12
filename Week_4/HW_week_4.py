"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

from random import random
import timeit
import cProfile

# Для сравнения был использован алгоритм из задания 9 к 1-й недели.

a = int(random() * 50)
b = int(random() * 50)
c = int(random() * 50)


def exp_1():
    answer = ''
    if a > b and a > c:
        if b > c:
            answer = f"Среднее число 'b' {b}"
        else:
            answer = f"Среднее число 'c' {c}"
    elif a < b and a < c:
        if b > c:
            answer = f"Среднее число 'c' {c}"
        else:
            answer = f"Среднее число 'b' {b}"
    else:
        answer = f"Среднее число 'a': {a}"


def exp_2():
    # m = a
    answer = ''

    if a > b > c or c > b > a:
        # m = b
        answer = f"Среднее число 'b' {b}"
    elif a > c > b or b > c > a:
        # m = c
        answer = f"Среднее число 'c' {c}"
    else:
        answer = f"Среднее число 'a': {a}"


"""
Алгоритм 1 отрабатывает быстрее в среднем на 20-30%.
Однако, если средним числом является 'b', 2-я функция  отрабатывает на 0-10% быстрее первого
"""

t1 = timeit.timeit("exp_1()", setup="from __main__ import exp_1", number=100000)  # >>> 0.06981423533170528
t2 = timeit.timeit("exp_2()", setup="from __main__ import exp_2", number=100000)  # >>> 0.1074301988555817
print(t1)
print(t2)
print(f"D = {(t2 - t1) / t2 * 100} %")
print()
print(f"a - {a}")
print(f"b - {b}")
print(f"c - {c}")


def main():
    exp_1()
    exp_2()


"""
6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <ipython-input-161-db5e7dbae1dc>:12(exp_1)
        1    0.000    0.000    0.000    0.000 <ipython-input-161-db5e7dbae1dc>:29(exp_2)
        1    0.000    0.000    0.000    0.000 <ipython-input-161-db5e7dbae1dc>:58(main)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
cProfile.run("main()")



"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""

n = int(random()*60)
print(f"n = {n}")


def sieve_1(): # Алгоритм с использования Решета Эратосфена
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)

def sieve_2(): # Алгоритм без использования Решета Эратосфена
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    # printlst

# Первый алгорим обладает меньшей сложностью, причем, чем больше значение i-го числа, тем выше разница в их работе (при n = 60 разница составляет порядка 2 раз)

def main():
    print(timeit.timeit("sieve_1()", setup="from __main__ import sieve_1", number=100000)) # >>> 0.5963504520259448
    print(timeit.timeit("sieve_2()", setup="from __main__ import sieve_2", number=100000)) # >>> 0.89487622314482
main()

# cProfile.run("main()")
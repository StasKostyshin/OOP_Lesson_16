from datetime import datetime
import inspect

#
# def create_list():
#     start = datetime.now() # Нецелевой код
#     list = [] # целевой код
#     for _ in range(10 ** 5): # Целевой код
#         if _ % 2 == 0: # целевой код
#             list.append(_) # целевой код
#     print(datetime.now() - start) # не целевой код
#     return list
#
# def create_list_gen():
#     start = datetime.now() # не целевой код
#     list_= [i for i in range(100 ** 5) if i % 2 == 0] # целевой код
#     print(datetime.now() - start) # не целевой кож
#     return list_
#
# ex1 = create_list()
# ex2 = create_list_gen()

# def count_the_time(arg):
#     """
#     задаём блок инструкции для работы с аогументами из декоратора
#     """
#     print((f"{arg}- аргумент декоратора count_the_time "))
#
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             start = datetime.now()
#             result = func(*args, **kwargs)
#             print(datetime.now() - start)
#             return result
#         return  wrapper
#
#     return outer
#
# @count_the_time('aeadasdaweqweqedq')
# def creare_list_gen(k):
#     list_ = [i for i in range(k) if i % 2 == 0]
#     return list_

###################### Задание №1 #########################################################################
# Написать декоратор который будет считать количество раз вызываемой функции

# def counter(func):
#     def wrapper(*args):
#         wrapper.count += 1
#         return func(*args)
#
#     wrapper.count = 0
#     return wrapper
#
# @counter
# def f():
#     print("Количество раз")
# f()
# print(f.count)
############################ решение через класс ###############################################
# class Decorator:
#     count = 0
#
#     def __init__(self, fun):
#         self._fun = fun
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self._fun(*args, **kwargs)
#
#
# @Decorator
# def foo(a): ...
#
# foo('a')
# foo('a')
# print(foo.count)
###############_____________
def decor(func):
    def wrapped(arg):
        for i in func():
            for a in num_list:
                if i in a:
                    a.remove(i)
        return num_list
    return wrapped

@decor
def in_a():
    list_3 = []
    for i in num_list:
        for a in i:
            if a % 3 == 0:
              list_3.append(a)
    return list_3

num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(in_a(num_list))
###################################################

def debug(func):
    def wrapped(*args):
        print(f'name function {func.__name__}')
        print(b,"+", c)
        print(f'result {func.__name__}: {func()}')
    return wrapped

@debug
def in_debug():
    a = b + c
    return a
b = 3
c = 5

in_debug()



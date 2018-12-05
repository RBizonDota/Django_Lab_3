#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique
path = 'data_light.json'
#path = sys.argv[1]

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов
@print_result
def f1(arg):
    return sorted([a for a in unique([i["job-name"] for i in arg],ignore_case = 1)])
    #return [i["job-name"] for i in arg]
@print_result
def f2(arg):
    return list(filter(lambda x: (x.find("Программист")==0)or(x.find("программист")==0),arg))
@print_result
def f3(arg):
    return list(map(lambda x: x+" с опытом Python",arg))
@print_result
def f4(arg):
    return list(zip(arg,[i for i in gen_random(100000,200000,len(arg))]))
with timer():
    f4(f3(f2(f1(data))))

a = [1,2,3,4,5]
print([i*i for i in a])
print(list(map(lambda x: x*x, a)))
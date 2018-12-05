#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = [i for i in gen_random(1, 10, 10)]
a = Unique(data2, ignore_case = 0)
for i in a:
    print(i, end = "| ")
print('')


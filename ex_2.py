#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
a = Unique([i for i in data2], key = 1)
for i in a:
    print(i, end = "| ")
print('')
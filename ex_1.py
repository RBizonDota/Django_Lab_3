from librip import gens
goods = [
    {'title': None, 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]
for i in gens.field(goods,'title'): print(i, end ='| ')
print('')
for i in gens.gen_random(1,10,12): print(i, end ='| ')
print('')
[print(x) for x in gens.field(goods,'title')]
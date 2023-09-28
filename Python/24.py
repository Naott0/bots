cities = {'РФ': ['Ростов', 'Москва', 'СПб'],
          'Италия': ['Рим', 'Милан']}
s1 = {}
s2 = {}

for i in cities.get('РФ'):
    d = dict.fromkeys([i], 'РФ')
    s1.update(d)

for i in cities.get('Италия'):
    d = dict.fromkeys([i], 'Италия')
    s2.update(d)

s1.update(s2)
print(s1)

# Дано множество работников
workers = {'Вася', 'Коля', 'Маша', 'Вера'}
# И подмножества
fast_workers = {'Коля', 'Маша'} # работают быстро
quality_workers = {'Маша', 'Вера'} # работают качественно
cheap_workers = {'Коля',  'Вера'} # работают бюджетно
# кто работает быстро, хорошо и дешево?
# кто работает криво, медленно и дорого?

print('кто работает быстро, хорошо и дешево?', fast_workers.difference(quality_workers,cheap_workers))
print('кто работает криво, медленно и дорого?', workers.difference(fast_workers,cheap_workers,quality_workers))
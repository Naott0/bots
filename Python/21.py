votes = [('31 - ая весна', 100),
         ('Цунами', 28),
         ('Привет, ромашки', 79),
         ('Лондон', 121),
         ('Осень', 79)]

sort_votes = sorted(votes, key=lambda x: x[1])
print('Превое место: ', sort_votes[4], '\n''Второе место: ', sort_votes[3], '\n''Третье место:', sort_votes[2], )
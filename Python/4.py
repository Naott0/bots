l = [[1, 2, 3, -1, 5],
     [5, 4, 4, 6],
     [1, -3, 2, -3]]
sum = 0
for i in l:
    x = len(i)
    for x in i:
        if x > 0:
            sum += x
print(sum)

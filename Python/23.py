n = int(input(('n = ')))
doska = [['b' if (i + j) % 2 else 'w' for j in range(n)] for i in range(n)]
print(*doska, sep='\n')

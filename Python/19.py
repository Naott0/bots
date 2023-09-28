def print_list(l):
    for x in l:
        if type(x) == list:
            print_list(x)
        else:
            print(x, end='')


print_list([1, 2, [3, 4, [5, 6], 7], 8, [9, 10]])

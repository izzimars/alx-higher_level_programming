#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (i < j):
            if (i == 8 and j == 9):
                print('{}{}'.format(i, j))
                break
            print('{}{},'.format(i, j), end=' ')

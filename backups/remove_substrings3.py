a = ['one', 'two', 'one', 'three', 'four', 'one two', 'one', 'four', 'three', 'five', 'six']
a = set(a)
for i in a:
    print('\n i is {} '.format(i))
    b = a.copy()
    b.remove(i)
    for j in b:
        print('{} in {}: {},  '.format(i, j,  i in j), end=' ')
        if i in j:
            print('removing {} '.format(i))
            a.remove(i)
        else:
            if j in i:
                print('removing "{}" '.format(j))
                a.remove(j)
print(a)

        

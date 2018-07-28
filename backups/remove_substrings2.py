a = ['one', 'one', 'three', 'four', 'one two', 'one', 'two', 'four', 'three', 'five', 'six']
rejects = []
a = list(set(a))
print(a)

n = len(a)

for i in range(n):
    for j in range(n):
        if a[i] == a[j]:
            print(a[i], a[j])
        else:
            if a[i] in a[j]:
                rejects.append(a[i])
                print("'{}' in '{}'".format(a[i], a[j]))

for reject in rejects:
    a.remove(reject)
       
print(rejects)
print(a)

        

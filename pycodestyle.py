import os

ls = os.listdir()
for n in ls:
    if '.py' in n:
        if 'py.' not in n:
            print(n)
            os.system('pycodestyle {}'.format(n))
            print()

 ## a possible method for find_matches()
#a = 'a'
#while a in ['a', 'e']:
#    print('Yes')
#    a = input('Guess a letter: ')
#print('no')
#
# another possible idea
a = ['a', 'e']
b = ['a', 'e', 'u']
if a in b:
    print("['a', 'e'] is in ['a', 'e', 'u']")
else:
    print("['a', 'e'] is not in ['a', 'e', 'u']")
print('BUT')
if ' '.join(a) in ' '.join(b):
    print("' '.join(a) is in ' '.join(b)")

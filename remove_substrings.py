#! /usr/bin/env python3

    
def remove_substrings(duplicates):
    ''' Makes a list without supstrings. For example,
     ['the big dog', 'the big', 'the'] becomes ['the big dog']'''
    rejects = []
    duplicates = list(set(duplicates))  # Removes exact duplicates.
    print()
    n = len(duplicates)
    for i in range(n):  # Take every phrase.
        for j in range(n):  # Compare it with every phrase.
            if duplicates[i] == duplicates[j]:  # Avoid self reference.
                pass
            else:
                if duplicates[i] in duplicates [j]:
                    rejects.append(duplicates[i])  # Add substring to reject list.
                    break
    for reject in rejects: # Remove substrings from the original list.
        duplicates.remove(reject)
    print('\nHere are the phrases in the essay, taken from the reading pack:\n')
    print(duplicates)
    return duplicates
    pass

if __name__ == '__main__':
    remove_substrings(duplicates)

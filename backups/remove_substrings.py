def remove_substrings(duplicates):
    # makes a list without supstrings. For example,
    # ['the big dog', 'the big', 'the'] becomes ['the big dog']
    rejects = []
    duplicates = list(set(duplicates))#removes exact duplicates
    print()
    n = len(duplicates)
    for i in range(n):# take every phrase
        for j in range(n):# compare it with every phrase
            if duplicates[i] == duplicates[j]: # avoid self reference
                pass
            else:
                if duplicates[i] in duplicates [j]:
                    rejects.append(duplicates[i]) # add substring to reject list
                    break
    for reject in rejects:#remove substrings from the original list.
        duplicates.remove(reject)
    print('\nduplicates feturned by "remove_substrings()" = \n{}\n'.format(duplicates))#test only#               
    return duplicates
        
        

duplicates_list = ['this is the', 'this is the', 'this is the', 'dummy list of', 'duplicated strings', 'dummy', 'this is', 'dummy list of'
                , 'list of', 'this is the dummy list of duplicated strings', 'strings']

remove_substrings(duplicates_list)

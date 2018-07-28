def remove_substrings(duplicates):
    # makes a list without supstrings. For example,
    # ['the big dog', 'the big', 'the'] becomes ['the big dog']
    rejects = []
    duplicates = list(set(duplicates))#removes exact duplicates
    print('without doublese =\n', duplicates)
    print(type(duplicates))
    print()
    n = len(duplicates)
    for i in range(n):# take every phrase
        print('i = ', i, duplicates[i])
        for j in range(n):# compare it with every phrase
            if duplicates[i] == duplicates[j]: # avoid self reference
                print("'{}' = '{}'".format(duplicates[i], duplicates[j]))
            else:
                if duplicates[i] in duplicates [j]:
                    rejects.append(duplicates[i]) # add substring to reject list
                    print("'{}' in '{}' ".format(duplicates[i], duplicates[j]))#test only#
                    print('rejects = ', rejects)#
                    print()
                    break
    for reject in rejects:#remove substrings from the original list.
        duplicates.remove(reject)
    print('rejects = {}'.format(rejects))#test only#
    print('duplicates = {}'.format(duplicates))#test only#               
    return duplicates
        
        

duplicates_list = ['this is the', 'this is the', 'this is the', 'dummy list of', 'duplicated strings', 'dummy', 'this is', 'dummy list of'
                , 'list of', 'this is the dummy list of duplicated strings', 'strings']

remove_substrings(duplicates_list)

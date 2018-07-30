#! /usr/bin/env python3

def longest(rp, sa, rp_occur, sa_occur):
    '''if passed the index of a word in both
       the sa and the rp, it will find and return the 
       longest matching string begining at those points'''
    m = 1
    while sa[sa_occur:sa_occur + m] == rp[rp_occur:rp_occur + m]:
        match = sa[sa_occur:sa_occur + m]
        m += 1
        if match == sa[sa_occur:sa_occur + m]:
            break  # Avoid infinite loop at end of strings.
    return match
    
def find_occurrences(word, text):
    ''' finds the indexes for every
    occurrence of the word in the text, and
    retcurns them as a list'''
    occurrences = []
    n = text.count(word)
    m = 0
    for i in range(n):  # Only look n times.
        occurrence = text.index(word, m)  # Start at m.
        occurrences.append(occurrence)
        m = occurrence + 1
    return occurrences


rp = ['the', 'essay', 'with', 'repeated', 'phrases', 'has', 'repeated', 'phrases']
sa = ['some', 'repeated', 'phrases', 'in', 'essay']
wordset = ['some', 'repeated', 'phrases', 'in', 'essay']
rstart = 3  # 'repeated'
sstart = 1

def find_matches(rp, sa, sstart, rstart):
    for n in range(1, 4):  # Start = 1 to avoid '[]' as first term.
        sstop = sstart + n
        rstop = rstart + n
        print('sa = ', sa[sstart:sstop])
        print('rp = ', rp[rstart:rstop])


#    a, b = 0, 1  # Set counters.
#    duplicates_list = []
#    while b < len(sa)-2 and a < len(sa)-1:
#        word = sa[a:b]
#        print('word = ', word)
#        occurrences = find_occurrences(word, rp)
#        match = []
#        for i in occurrences:
#            while sa[a:b] == rp[m:m + (b-a)]:
#                print('sa[a:b] = ', sa[a:b])
#                match = sa[a:b]
#                b =+ 1
#            duplicates_list.append(match)
#        a += 1
#        b = a + 1
#    return duplicates_list

if __name__ == '__main__':
    find_matches(rp, sa, sstart, rstart)

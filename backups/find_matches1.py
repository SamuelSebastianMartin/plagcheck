#! python3

# early development of part of the
# find_matches() fn for the plagiarism
# checker.

word = 'quick'
text = 'the quick quick brown quick fox'

def find_occurrences(word, text): # working
    '''finds the string indexes for every
    occurrence of the word in the text, and
    returns them as a list'''
    occurrences = []
    n = text.count(word)
    m = 0
    for i in range(n): # only look n times
        occurrence = text.find(word, m) # start at m
        occurrences.append(occurrence)
        m = occurrence + 1
    return occurrences

sa_occurrences = find_occurrences(word, text)
print(sa_occurrences)

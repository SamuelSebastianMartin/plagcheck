#!/usr/bin/env python3

# to check for plagiarism between 2 documents:
#              reading_pack.txt and essay.txt

"""The main engine is the find_matches() function:
    for each unique word in essay:
        for each occurance of word in essay:
            for each occurance of word in reading pack:
                check for matches in texts.    """
# Still to do:
#   remove non-content words from unique_words
#   make the program work with pdf, doc and docx files

def main():
    level = welcome() #working
    rp, sa, unique_words, original_essay = get_texts() #working
    duplicates_list = find_matches(rp, sa, unique_words) #working
    duplicates = remove_substrings(duplicates_list) #working
    highlighted_essay = results(duplicates, original_essay)
    save_as(highlighted_essay)

def welcome(): #working
    print("""
        PLAGIARISM CHECKER
        
        This program finds snippets of text in an essay which have
        been copied from the reading pack. You can select the level
        of sensitivity between
        1.   'severe'
        2.   'medium'
        3.   'kind'.
        """)
##    level = input("What level will you use? Enter 1 , 2 or 3: ")
##    return level
    return 1

def get_texts():
    """This function and sub-functions opens and prepares the two texts,
    returning clean texts, a list of unique words, and the original essay"""

    def get_text_names(): # please develop to allow selection of text
        print("\nThe files being opened must be named\n'reading_pack.txt' and 'essay.txt'\n")
        texts = ['reading_pack.txt', 'essay.txt']
        return texts

    def open_text(text): # used to open files - txt only for now
        myfile = open(text, 'r')
        document = myfile.read()
        myfile.close()
        return document

    def prepare_text(text):#working
        import string
        # return without punctuation, lowercase, single spaced
        text = text.lower()
        text = " ".join(text.split()) #remove multispaces and \t etc
        text = "".join((char for char in text if char not in string.punctuation))
        return text

    def unique_token(text):
        # return a list of unique content words in essay
        unique_words = []
        all_essay_words = text.split()
        unique_essay_words = list(set(all_essay_words))
        # remove essay_words which aren't in rp
        for essay_word in unique_essay_words:
            if essay_word in rp:
                unique_words.append(essay_word)
        return unique_words
    
    texts = get_text_names()
    reading_pack = open_text(texts[0])
    original_essay = open_text(texts[1])
    rp = prepare_text(reading_pack)
    sa = prepare_text(original_essay)
    unique_words = unique_token(sa)
    #print("texts = {}\n\nreading_pack = {}\n\noriginal_essay = {}\n\nrp = {}\n\nsa = {}\n\nunique_words = \n{}\n"nunique_words.format(texts, reading_pack, original_essay, rp, sa, unique_words))#test only
    return rp, sa, unique_words, original_essay

def find_matches(rp, sa, unique_words):
    """ for each unique word:
           for each occurance of word in sa:
               for each occurance of word in rp:
                   check for matches in texts.    """
    
    def find_longest_match(rp, sa, rp_occur, sa_occur, str_length): # working
        '''if passed the string index of a word in both
           the sa and the rp, it will find and return the 
           longest matching string begining at those points'''
        while sa[sa_occur:sa_occur + str_length] == rp[rp_occur:rp_occur + str_length]:
            match = sa[sa_occur:sa_occur + str_length]
            str_length += 2 # should still catch whole words if not 1
            if match == sa[sa_occur:sa_occur + str_length]:
                break # avoid infinite loop at end of strings
        return match
    
    def find_occurrences(word, text): # working
        ''' finds the string indexes for every
        occurrence of the word in the text, and
        retcurns them as a list'''
        occurrences = []
        n = text.count(word)
        m = 0
        for i in range(n): # only look n times
            occurrence = text.find(word, m) # start at m
            occurrences.append(occurrence)
            m = occurrence + 1
        return occurrences

    duplicates_list = []
    for word in unique_words:
        sa_occurrences = find_occurrences(word, sa)
        for sa_occur in sa_occurrences:
            rp_occurrences = find_occurrences(word, rp)
            for rp_occur in rp_occurrences:
                match = find_longest_match(rp, sa, rp_occur, sa_occur, len(word))
            duplicates_list.append(match)
    return duplicates_list

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
    #print('\nduplicates feturned by "remove_substrings()" = \n{}\n'.format(duplicates))#test only#               
    print(duplicates)
    return duplicates

def results(duplicates, original_essay):
    # Takes the original essay (for now only as .txt) and highlights the strings which are
    # copied from the reading pack (for now as CAPS)
    highlighted_essay = original_essay #for now
    return highlighted_essay

def save_as(highlighted_essay):
    ''' Prompts for filename and saves the essay with results (for now as .txt)'''
    #filename = input('Saving results\nplease give the filename you want, including the .txt: ')
    #print (filename)
if __name__ == '__main__':
    main()


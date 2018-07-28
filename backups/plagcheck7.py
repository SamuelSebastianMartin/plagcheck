#/usr/bin/python3

# to check for plagiarism between 2 documents:
#              reading_pack.txt and essay.txt

"""The main engine is the find_matches() function:
    for each unique word in essay:
        for each occurance of word in essay:
            for each occurance of word in reading pack:
                check for matches in texts.    """
# Still to do:
#   make open and save doc and docx files
#   check unique_words are in both texts (save processing)
#   remove non-content words from unique_words

def main():
    level = welcome() #working
    rp, sa, unique_words, original_essay = get_texts() #working
    duplicates_list = find_matches(rp, sa, unique_words)
    duplicates = remove_substrings(duplicates_list)
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
    level = input("What level will you use? Enter 1 , 2 or 3: ")
    return level

def get_texts():
    """This function and sub-functions opens and prepares the two texts,
    returning clean texts, a list of unique words,, and the original essay"""
    def get_text_names(): # develop to allow selection or text
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
        all_words = text.split()
        unique_words = list(set(all_words))
        print('unique words =',unique_words)#
        return unique_words
    texts = get_text_names()
    reading_pack = open_text(texts[0])
    original_essay = open_text(texts[1])
    rp = prepare_text(reading_pack)
    sa = prepare_text(original_essay)
    unique_words = unique_token(sa)
    print("texts = {}\nreading_pack = {}\noriginal_essay = {}\nrp = {}\nsa = {}\nunique_words = {}"
          .format(texts, reading_pack, original_essay, rp, sa, unique_words))#test only
    return rp, sa, unique_words, original_essay

def find_matches(rp, sa, unique_words):
    #nested 'for' loops, to run through every occurrance of every content word in the essay
    #and check against every occurrance of the same word in the reading pack.
    # If a match is found, the next word/character is added, and the comparison is repeated.
    # once the match fails, the longest matching string is stored in 'duplicate_list'.
    return ['this is the', 'dummy list of', 'duplicated strings', 'dummy', 'this is', 'dummy list of'
                , 'list of', 'this is the dummy list of duplicated strings', 'strings']

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

def results(duplicates, original_essay):
    # Takes the original essay (for now only as .txt) and highlights the strings which are
    # copied from the reading pack (for now as CAPS)
    highlighted_essay = original_essay #for now
    return highlighted_essay

def save_as(highlighted_essay):
    # Prompts for filename and saves the essay with results (for now as .txt)
    filename = input('Saving results\nplease give the filename you want, including the .txt: ')
    print (filename)
if __name__ == '__main__':
    main()


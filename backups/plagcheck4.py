#! python3

# to check for plagiarism between 2 documents:
# reading_pack.txt and essay.txt

"""The principle is:

    for each unique word in essay:
        for each occurance of word in essay:
            for each occurance of word in reading pack:
                check for matches in texts.

    """
# Still to do:

def main():
    level = welcome()
    rp, sa, unique_words, original_essay = get_texts()
##    duplicates_list = find_matches(rp, sa, unique_words)
##    duplicates = remove_substrings(duplicates_list)
##    highlighted_essay = results(duplicates, original_essay)
##    save_as()

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
    def prepare_text(original_text):
        # return without punctuation, lowercase, single spaced
        prepared_text = original_text #
        return prepared_text
    def unique_token(prepared_text):
        # return a list of unique content words in essay
        unique_words = [] #
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

def main():
    level = welcome()
    rp, sa, unique_words, original_essay = get_texts()

if __name__ == '__main__':
    main()


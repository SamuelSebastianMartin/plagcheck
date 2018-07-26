#!/usr/bin/env python3

# Must be in same folder as the essay, reading_pack and
# filepicker.py (my own module)
#
# to check for plagiarism between 2 documents:
#              reading_pack.txt and essay.txt

"""The main engine is the find_matches() function:
    for each unique word in essay:
        for each occurance of word in essay:
            for each occurance of word in reading pack:
                check for matches in texts.    """


def main():
    level = welcome()  # Working.
    rp, sa, unique_words, original_essay = get_texts()  # Working.
    duplicates_list = find_matches(rp, sa, unique_words)  # Working.
    duplicates = remove_substrings(duplicates_list)  # Working.
    highlighted_essay = results(duplicates, original_essay)
    save_as(highlighted_essay)


def welcome():  # Working.
    print("""
        PLAGIARISM CHECKER
        
        This program finds snippets of text in an essay which have
        been copied from the reading pack. You can select the level
        of sensitivity between
        1.   'severe'
        2.   'medium'
        3.   'kind'.
        """)
#    level = input("What level will you use? Enter 1 , 2 or 3: ")
#    return level
    return 1


def get_texts():
    """This function and sub-functions opens and prepares the two texts,
    returning clean texts, a list of unique words, and the original essay"""

    def get_text_names():  # Please develop to allow selection of text.
        import filepicker  # My own module. Must be in the same directory.
        reading_pack = filepicker.filepicker('reading pack')  # User input.
        essay = filepicker.filepicker('essay')  # User input.
        texts = [reading_pack, essay]
        return texts

    def open_text(text):  # Used to open files - txt only for now.
        myfile = open(text, 'r')
        document = myfile.read()
        myfile.close()
        return document

    def prepare_text(text):  # Working.
        import string
        # Return without punctuation, lowercase, single spaced.
        text = text.lower()
        text = " ".join(text.split())  # Remove multispaces and \t etc.
        text = "".join((char for char in text if char not in string.punctuation))
        return text

    def unique_token(text):
         # Return a list of unique content words in essay.
        unique_words = []
        all_essay_words = text.split()

         # Remove common words to save processing.
        stoplist = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
        for stop in stoplist:
            while stop in all_essay_words:
                all_essay_words.remove(stop)
        unique_essay_words = list(set(all_essay_words))
        # Remove Essay_words which aren't in rp.
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
    return rp, sa, unique_words, original_essay


def find_matches(rp, sa, unique_words):
    """ for each unique word:
           for each occurance of word in sa:
               for each occurance of word in rp:
                   check for matches in texts.    """
    
    def find_longest_match(rp, sa, rp_occur, sa_occur, str_length):  # Working.
        '''if passed the string index of a word in both
           the sa and the rp, it will find and return the 
           longest matching string begining at those points'''
        while sa[sa_occur:sa_occur + str_length] == rp[rp_occur:rp_occur + str_length]:
            match = sa[sa_occur:sa_occur + str_length]
            str_length += 2  # Should still catch whole words if not 1.
            if match == sa[sa_occur:sa_occur + str_length]:
                break  # Avoid infinite loop at end of strings.
        return match
    
    def find_occurrences(word, text):  # Working.
        ''' finds the string indexes for every
        occurrence of the word in the text, and
        retcurns them as a list'''
        occurrences = []
        n = text.count(word)
        m = 0
        for i in range(n):  # Only look n times.
            occurrence = text.find(word, m)  # Start at m.
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
    # Makes a list without supstrings. For example,
    # ['the big dog', 'the big', 'the'] becomes ['the big dog']
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


def results(duplicates, original_essay):
    # Takes the original essay (for now only as .txt)
    # and highlights the strings which are
    # copied from the reading pack (for now as CAPS)
    highlighted_essay = original_essay  # For now.
    return highlighted_essay


def save_as(highlighted_essay):
    ''' Prompts for filename and saves the essay with results (for now as .txt)'''


if __name__ == '__main__':
    main()

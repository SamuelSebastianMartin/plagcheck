import re
import CheckMatch as Cm

orig = "the quick brown fox"
para = "quick brown" # one paragraph (précis of the original text).
#i = 0 # the index that will work slowly through the paragraph.
#para_unfinished = True
#
#def build_run(para, orig, i):
#    next_white_space = re.search(r'\W+', para, i).span()[1]
#    print(next_white_space)
#    i = next_white_space
#    if i < len(para):
#        build_run(para, orig, i)
#    else:
#        break
#
#build_run(para, orig, i)

class BuildRun:
    def __init__(orig, para, start_index):
        self.orig = orig
        self.para = para
        self.i = start_index
        self.j = self.next_whitespace()
        self.category = []

    def next_whitespace(self):

        """
        Finds the index of the next gap between words.
        This will include all punctuation, so effectively
        stops just before the next word.
        `para` is sliced from the start index to the end,
        and the index of the end of the whitespace returned.
        """
        return(re.search(r'\W+', para[self.i:]).span()[1]

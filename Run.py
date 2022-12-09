#! /usr/bin/env/ python3

import re


class Run:
    def __init__(self, orig, para, start_index):
        self.orig = orig
        self.para = para
        self.i = start_index
        self.j = self.i # end of run index
        self.lastWordLen = 0
        self.truthlist = []
        self.currentRegex = r"\W+"

    def add_word(self):

        """
        add_word performs 2 functions:
        1. It adds the next text word to the currentRegex search sting.
        2. It records the length of the last-added word
        """
        new_word = re.search(r'\w+', self.para[self.j:])
        if new_word: # prevents overrunning
            self.lastWordLen =  new_word.span()[1]
            next_word = new_word.group()
            self.currentRegex = self.currentRegex + next_word + r'\W+'
        else:
            self.terminate_run()

    def search_for_match(self):
        """
        Performs a regex search, ignoring case,
        punctuation and multiple spaces.
        """
        srch = re.compile(self.currentRegex, re.IGNORECASE)
        return re.search(srch, self.orig)

    def build_run(self):
        """
        Finds the longest string in self.para starting as index self.i
        which is either all in the orig or all not in the orig.
        Words are added to the search one by one, and each time the 
        True or False of the match is recorded in truthlist.
        If the latest addition does not match the others, the run is
        terminated. E.g., if the truthlist = [T, T, T], and the next
        search returns False [T, T, T, F], the run ends and the last
        word is removed. Similarly, [F, F, F, T] would end the run.
        """
        # Add one word to the search string/regex
        self.add_word()
        # Record if it is a match or not
        if self.search_for_match():
            self.truthlist.append(True)
        else:
            self.truthlist.append(False)

        # For runs of only one word, go again.
        if len(self.truthlist) < 1:
            self.j += self.lastWordLen
            self.build_run()
        # If latest value differs from the first, end the process
        if self.truthlist[-1] == self.truthlist[0]:
            self.j += self.lastWordLen
            self.build_run()
        else:
            self.terminate_run()

    def terminate_run(self):
        self.run = self.para[self.i: self.j]
        self.plagStatus = self.truthlist[0]

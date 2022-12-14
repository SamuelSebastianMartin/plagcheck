#! /usr/bin/env/ python3

import re


class Run:
    def __init__(self, orig, para, start_index):
        self.orig = orig
        self.para = para
        self.i = start_index
        self.j = self.i # end of run index
        self.lastWordLen = 0
        self.category = []
        self.currentRegex = r"\W+"
        self.allowRecursion = True

    def add_word(self):
        """
        add_word performs 2 functions:
        1. It adds the next text word to the currentRegex search sting.
        2. It records the length of the last-added word
        """
        nextWord = re.search(r'\w+', self.para[self.j:])
        if nextWord: # prevents overrunning
            self.lastWordLen =  nextWord.span()[1]
            word = nextWord.group()
            self.currentRegex = self.currentRegex + word + r'\W+'
        else:
            self.terminate_run()

    def search_for_match(self):
        """
        Performs a regex search, ignoring case,
        punctuation and multiple spaces.
        returns an re.match object
        """
        srch = re.compile(self.currentRegex, re.IGNORECASE)
        return re.search(srch, self.orig)

    def build_run(self):
        """
            Starting at index self.i of self.para, this builds
            a single run of consecutive words. The entire run
            is either
              a) a direct word-for-word of text in self.orig
              b) a string of words none of which appear in
              self.orig
            Each loop of this recursive method adds one word
            to the string, and tests for a match in self.orig
            The True/False status of the match is saved in
            self.category. If the latest addition does not
            match the others, the run is terminated.
            E.g., if the category = [T, T, T], and the next
            search returns False [T, T, T, F], the run ends
            and the last word is removed. Similarly,
            [F, F, F, T] would end the run.
        """
        while self.allowRecursion:
            # Add one word to the search string/regex
            self.add_word()
            # Record if it is a match or not
            if self.search_for_match():
                self.category.append(True)
            else:
                self.category.append(False)

            # If latest value differs from the first, end the process
            if self.category[-1] == self.category[0]:
                self.j += self.lastWordLen
                self.build_run()
            else:
                self.terminate_run()

    def terminate_run(self):
        self.allowRecursion = False
        self.run = self.para[self.i: self.j]
        self.plagStatus = self.category[0]
        print('terminating run')

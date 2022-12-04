import re
import string


class CheckMatch:
    def __init__(self, needle, haystack):
        self.needle = self.string_to_regex(needle)
        self.haystack = haystack

    def string_to_regex(self, text: str) -> str:
        """
        Takes a string and returns a lowercase list of words, separated by
        a regular expression that matches any punctuation or spaces
        """
        text = text.lower()
        text = "".join((char for char in text
                        if char not in string.punctuation))
        text_words = text.split()
        return r"\W+".join(text_words)

    def text_match(self, needle: str, haystack: str) -> bool:
        """
        Performs a regex search, ignoring case,
        punctuation and multiple spaces.
        """
        srch = re.compile(self.needle, re.IGNORECASE)
        return re.search(srch, haystack)

#! /usr/bin/env python3

class Match:

    def __init__(self, list_span, rp, para_words, text):
        self.list_span = list_span
        self.text_span = get_text_span(list_span, para_words, text)
        regex = get_regex(self.span, para_words)

    def get_regex(self, list_span, para_words):
        """produces the regex search for any span in para_words"""
        str = r'\W+'.join(para_words[self.span[0]: self.span[1]])
        expr = re.compile(str, re.IGNORECASE)
        return expr

    def set_list_span(self):
        self.list_span = (a, b)

    def get_text_span(self, list_span, para_words, text):
        return (0, 0)


def test():
    pass


if __name__ == '__main__':
    test()

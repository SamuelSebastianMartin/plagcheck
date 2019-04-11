#! /usr/bin/env python3

class TextSpan:
    def __init__(self, span, plagiarism_status):
        self.i = span[0]
        self.j = span[1]
        self.plag = plagiarism_status  # Bool.


def build_document(text, sa_spans):
    # Change spans into TextSpan objects with 'Plagiarism = True'.
    sps = spans_to_textspans(sa_spans)
    outspans = []
    # add initial run, if the first plagiarised span does
    # not occur at the beginning of the text.
    if sps[0].i != 0:
        first_sp = TextSpan((0, sps[0].i), False)
        outspans.append(first_sp)

    for n in range(len(sa_spans)):
        # The last entry is a special case, to be added later.
        if n >= len(sa_spans)-1:
            break
        else:
            # For all the internal spans...
            spn = spans[n]
            nxt = spans[n+1]
            if spn.j == nxt.i:
                # Dean with consecutive span runs.
                outspans.append(spn)
            else:
                # Where there is a gap between plagerised text spans
                new_spn = TextSpan(spn.j, nxt.i, False)  # Plag = False.
                outspans.append(spn)
                outspans.append(new_spn)

    # Append the last span, and any remainder.
    outspans.append(sps[-1])
    if sps[-1] == len(text):  # NB not -1, to include the final letter.
        last_sp = TextSpan((sps[-1].j, len(text)), False)

    return outspans


def spans_to_textspans(sa_spans):
    """
    Turns all positive  plagiarised spans into TextSpan objects,
    marked 'True' for plagiarism.
    """
    sps = [TextSpan(span, True) for span in sa_spans]
    return sps

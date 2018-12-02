#!/usr/bin/env python3

#              reading_pack.txt and essay.txt

"""
This finds text in an essay.docx, which has bee copied from reading-pack.docx.
You will be asked to select, first a reading-pack document, then the essay.
The essay is processed by paragraph for matches.
Output is a new MS Word document with copied text in bold type.
"""

import get_texts
import find_matches
import prune_matches
import docx
import os


def main():
    rp_doc, rp, rp_path = get_texts.get_texts()
    sa_doc, sa, sa_path = get_texts.get_texts()

    #  Create final out document.
    out_doc = docx.Document()

    #  Loop through paragraphs, finding index of plagiarised text.
    for para in sa_doc.paragraphs:
        matches = find_in_rp(rp, para)
        sa_indices = find_in_sa(matches, para.text)
        indices = prune_matches.prune_indices(sa_indices)
        out_doc = write_para(out_doc, para.text, indices)

    out_doc.save('OUT.docx')
    os.system('libreoffice OUT.docx')


def find_in_rp(rp, para):
    text = para.text
    para_words = get_texts.prepare_text(text)
    para_words.append('_dummy_final_word_')
    para_words.insert(0, '_dummy_first_word_')

    matches = find_matches.find_matches(rp, para_words)
    return matches

def find_in_sa(matches, sa):
    spans = []
    n = 0  # Start point for search.
    for match in matches:
        srch = match.search(sa, pos=n)
        if srch != None:
            span = srch.span()
            n = span[0] +1  # To not re-search the same text. Matches are in order.
            spans.append(span)

    return spans

def write_para(out_doc, text, indices):
    p = out_doc.add_paragraph()

    i = 0
    j = 0
    for span in indices:
        j = span[0]  # End of unplagiarised section.
        p.add_run(text[i: j])
        p.add_run(text[span[0]: span[1]]).underline = True
        if span[1] < len(text):
            i = span[1]

    p.add_run(text[i: len(text)])  # Tail end of good text.

    return out_doc


    pass

if __name__ == '__main__':
    main()

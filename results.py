#! /usr/bin/env/ python3

import docx
import os
import get_texts
import shutil


# Make new .docx file to open for testing.
doc = docx.Document()
doc.add_paragraph('This is the good text.')
doc.add_paragraph('This, however, is the plagerised text - to be highlighted')
doc.add_paragraph('This is good text')
doc.save('deleteme_results_testfile.docx')

shortlist = [['this', 'however', 'is', 'the', 'plagiarised', 'text', 'to', 'be', 'highlighted']]



def results(shortlist):
    for result in shortlist:
        print(' '.join(result))

#os.remove('deleteme_testfile.docx')  # Clean up directory.

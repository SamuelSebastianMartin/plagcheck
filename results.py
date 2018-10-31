#! /usr/bin/env/ python3

'''This is a test module, to present the results from the plagiarism.py
program. It first sets up a dummy doc object, as if it had been produced by
plagiarism.py. It should then save the output as a FORMATTED Word document,
with the plagiarised text highlighted'''
import docx
import os
import get_texts
import shutil


###########################################
# Make new dummy docx.Document object, and shortlist to use for testing.
doc = docx.Document()
doc.add_paragraph('This is the good text.')
doc.add_paragraph('This, however, is the plagerised text - to be highlighted.')
doc.add_paragraph('This is good text.')
doc.save('deleteme_results_testfile.docx')


shortlist = [['this', 'however', 'is', 'the', 'plagiarised',
              'text', 'to', 'be', 'highlighted']]


###########################################
# Read and process the text
def main():
    doc = docx.Document('deleteme_results_testfile.docx')
    #  Here, doc represents the original essay submitted by the student
    #  and 'shortlist' is the output of 'plagcheck.py' from that same essay.
    full_text = [para.text for para in doc.paragraphs]
    original_essay = ' '.join(full_text)
    results(shortlist, original_essay)


def results(shortlist, original_essay):
    '''For now, this does nothing put print the text to standard out,
    but it is exactly here that the work will be done'''
    for result in shortlist:
        print(' '.join(result))
    print(original_essay)


if __name__ == '__main__':
    main()


###########################################
#  Clean up the directory
os.remove('deleteme_results_testfile.docx')  # Clean up directory.

'''notes on docx module from 'automate the boring stuff'''
#    import docx
#    doc = docx.Document()
#    doc.add_paragraph('Hello world!')
#    paraObj1 = doc.add_paragraph('This is a second paragraph.')
#    paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
#    paraObj1.add_run(' This text is being added to the second paragraph.')
#    doc.save('multipleParagraphs.docx')

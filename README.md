## Me learning Python.

This program relates to my work, where students write an essay based on a series of academic texts given to them in a reading pack. 
The program looks for words or phrases in the essay which are taken directly from the reading pack.

In order to facilitate the running of python's 'unittest', I have also decided to build the project with few or no nested functions, but to use modules to group functions together. Detailed test can then be run on modules, and more general tests can be run on the main program.

## THIS VERSION.

I am changing the flow so that it processes paragraph objects. This way I can create an output document that looks quite like the original.

I am finding matches using regex. This means that double spaces, captial letters and punctuation in the original essay can be preserved when printing the results. It also allows the possibility of skipping words that the student has added.

The basic functioning will be the same, but now the sa text will consist of only one paragraph of the essay at a time.

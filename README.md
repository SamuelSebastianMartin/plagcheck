## Me learning Python
This is my first serious program, (as in not an exercise), and this branch represents my fourth serious rewrite!

I am learning about using functions, instead of having one long process.
I am also making as much as possible myself; I want to learn about  the algorithms now, and explore various modules later, when I understand more.

This program relates to my work, where students write an essay based on a series of academic texts given to them in a reading pack. 
The program looks for words or phrases in the essay which are taken directly from the reading pack.

In order to facilitate the running of python's 'unittest', I have also decided to build the project with few or no nested functions, but to use modules to group functions together. Detailed test can then be run on modules, and more general tests can be run on the main program.

## THIS VERSION

I am changing the flow so that it processes paragraph objects. This way I can create an output document that looks quite like the original. See `save_by_para.py` for the paragraph process in shell form.

I am finding matches using regex, and saving the results with regex, too. This means that double spaces, captial letters and punctuation in the original essay can be preserved when printing the results. It also allows the possibility of skipping words that the student has added. See regex.py for progress in this. One result of this is that the 'matches' list can now be a list of regex objects, making saving easier.

The basic functioning will be the same, but now the sa text will consist of only one paragraph of the essay at a time.

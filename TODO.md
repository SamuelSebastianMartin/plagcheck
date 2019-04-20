#To-do list for plagcheck.py


##FUNCTION

- Add second level of `find_in_essay()`, replacing all `\\W+?` with `\\W+w?` to allow inserted words. This would have to integrate with both `prune_matches()` and `add_paragraph()`.

- Incorporate a sensitivity level.
remove sources from prepared text. This could be remove all `'(....... \d\d\d\d)'`, or `'Camel Case (\d\d\d\d)'`

- Strip sa of references and bibliography before making `para_words` list. This would deal with bibliographies and title pages, too, but not empy phrases (*'it would seem that'* etc) or number of words.


##USEABILITY

- Improve `filepicker` to give instructions on the GUI.
- Process multiple essays.
- Package for colleagues to use on MS Windows.

##PROBLEMS

Still missing the first and last word of some quotations.

some words crash into each other - check that this is not problem with the original essays being already corrected.

Failing one `test_find_matches.py`

References are highlighted (smaller problem)

##SOLUTIONS

- Have a re.group within `find_in_sa()`, which compares with a regex from of a citation and rejects matches. This could also be used for bibliographies and runs like 'in the same' or 'it would seem that'. The sensitivity/number of words could be checked here too.

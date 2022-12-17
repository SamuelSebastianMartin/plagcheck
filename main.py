from DocumentUtil import DocumentReader


def main():
    """
    The main loop for the program: works
    through all paragraphs is a text, and
    converts each into a list of Run objects
    """
    # does the method need a 'return' statement?
    orig = DocumentReader.get_text('Original Text')
    paraphrase = DocumentReader.get_paragraphs('Paraphrase')
    ParasInParaphrase = [] # for all paragraphs

    for paragraph in paraphrase:
        paragraphs = to_match_runs(paragraph)


def to_match_runs(para):
    """
    Turns a single paragraph into a series
    of runs, each labelled as to whether
    its text is in the original (T) or not (F)
    """
    start_index = 0
    runs_in_para = [] # for one paragraph
    while start_index < len(para):
        run = Run(orig, para, start_index)
        run.build_run()
        runs_in_para.append(run)
        start_index = run.j


if __name__ == '__main__':
    main()

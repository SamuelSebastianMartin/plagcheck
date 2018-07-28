#!/bin/python3

##################################################
##  loop to find word from one text in another  ##
##    this is part of the plagiarism checker    ##
##################################################

## Set up text files
original_text = str('this is the original text')
student_text = str('this is the student text')

## student file to list
student_list = student_text.split(' ')

## Set up variables ##########################
## snippet bank to hold all the plagiarised chunks.
snippet_bank = []
## number_of_words_in_plagiarised_string 
## could be set up as start-up dialogue.
number_of_words_in_plagiarised_string = int(2)
## variables 'placeholder' and 'successive_words'
## will be set up in the program.


while len(original_list) != 0:
    # add code to make student/word/s into string to check
    successive_words = int(0)
    if student_list[:successive_words] in original_list:
        successive_words += 1
    else:
       
## code to check if target phrase is in string 
if original_text.find('TARGET PHRASE') != -1: # -1 is error code if not found

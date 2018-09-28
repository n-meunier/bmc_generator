#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            Nicolas Meunier
# =============================================================================
# PROJECT : BMC Generator
# FILE : cah_generator.py
# DESCRIPTION :
"""
Generate a funny sentence combining a gapped sentence and expressions or words.

How to use it : python bmc_generator.py
Requirements:
- None

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.1.0     2018/09/28     Initial version
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import sys
import os
import csv
import random
import re
from difflib import SequenceMatcher

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'nmeunier'
__date__ = '2018/09/28'
__version__ = '0.1.0'
__url__ = 'https://github.com/n-meunier/bmc_generator'

# [GLOBAL & CONSTANT VARIABLES]------------------------------------------------
blank_pattern = '(____)'
line = 'No result'

PATH = os.path.dirname(os.path.realpath(__file__))
wfile = PATH + '/whitelist.csv'
bfile = PATH + '/blacklist.csv'


# [FUNCTIONS]------------------------------------------------------------------
def answer_getter(nb_blanks, word_list):
    """ Get answers from the whitelist.
    :param nb_blanks: number of answers to get
    :return: list of answers
    """
    seen_answers = {}
    answers_list = list()
    while len(answers_list) < nb_blanks:
    # for n in range(nb_blanks):
        rand_answer = random.choice(word_list)
        if seen_answers.has_key(rand_answer):
            # print('Already seen: %s' % str(rand_answer))
            seen_answers[rand_answer] += 1
        else:
            # print('New answer: %s' % str(rand_answer))
            answers_list.append(rand_answer)
            seen_answers[rand_answer] = 1
    return answers_list


def add_to_list(input, filelist):
    """ Add a word to the list.
    :param input: word to add
    :param filelist: list of words
    :return: True if added, False if it was already in the list
    """
    exist = False
    _cpt = 0
    max_ratio = 0
    max_match = 'nothing'
    for line in filelist:
        _cpt += 1
        ratio = SequenceMatcher(a=str(line).lower(),
                                b=str(input).lower()).ratio()
        if ratio > max_ratio:
            max_ratio = ratio
            max_match = line
        if ratio > 0.7:
            exist = True
            match = line
            break
    # print('Stopped at %s' % str(_cpt))
    # print('Already exists? %s' % str(exist))
    if exist:
        # print('Match: %s (%0.2f)' % (str(match), ratio))
        return False
    else:
        # print('No match (Closest: %s with %0.2f), thank you for your input!' %
        #       (str(max_match), max_ratio))
        return True


# [MAIN]-----------------------------------------------------------------------
def main():
    """ Main function
    :return: funny sentence
    """
    # Read the sentences list
    with open(bfile, 'rb') as f:
        reader = csv.reader(f, delimiter='\n')
        blist = [item for sublist in list(reader) for item in sublist]
    nb_blist = len(blist)

    # Read the words list
    with open(wfile, 'rb') as f:
        reader = csv.reader(f, delimiter='\n')
        wlist = [item for sublist in list(reader) for item in sublist]
    nb_wlist = len(wlist)

    # Get a sentence
    sample = random.choice(blist)
    # print('Sample: %s (%s)' % (sample, str(type(sample))))

    # Find the number of words to fill
    match = re.findall(blank_pattern, sample)
    if match:
        nb_blanks = len(match)
        # print('Found %s match(es).' % str(nb_blanks))

        words = sample.split('____')

        # Get the correct number of missing words
        answers = answer_getter(nb_blanks, wlist)

        # print('Answers:')
        # for a in answers:
        #     print a

        # Complete the sentence
        line = sample
        for an in answers:
            line = line.replace('____', an, 1)

        print line
        return line


    # print(sample)


if __name__ == '__main__':
    main()

import csv
import random
import re
from difflib import SequenceMatcher

def answer_getter(nb_blanks):
    """
    Get answers from the whitelist.
    :param nb_blanks: number of answers to get
    :return: list of answers
    """
    seen_answers = {}
    answers_list = list()
    while len(answers_list) < nb_blanks:
    # for n in range(nb_blanks):
        rand_answer = random.choice(wlist)
        if seen_answers.has_key(rand_answer):
            print('Already seen: %s' % str(rand_answer))
        else:
            print('New number: %s' % str(rand_answer))
            answers_list.append(rand_answer)
            seen_answers[rand_answer] = 1
    return answers_list

def add_to_list(input, filelist):
    """"""
    exist = False
    _cpt = 0
    max_ratio = 0
    max_match = 'nothing'
    for line in filelist:
        _cpt += 1
        ratio = SequenceMatcher(a=line, b=input).ratio()
        if ratio > max_ratio:
            max_ratio = ratio
            max_match = line
        if ratio > 0.7:
            exist = True
            match = line
            break
    print('Stopped at %s' % str(_cpt))
    print('Already exists? %s' % str(exist))
    if exist:
        print('Match: %s (%0.2f)' % (str(match), ratio))
    else:
        print('No match (Closest: %s with %0.2f), thank you for your input!' %
              (str(max_match), max_ratio))

blank_pattern = '(____)'

wfile = 'whitelist.csv'
bfile = 'blacklist.csv'

with open(bfile, 'rb') as f:
    reader = csv.reader(f, delimiter='\n')
    blist = [item for sublist in list(reader) for item in sublist]
nb_blist = len(blist)

with open(wfile, 'rb') as f:
    reader = csv.reader(f, delimiter='\n')
    wlist = [item for sublist in list(reader) for item in sublist]
nb_wlist = len(wlist)

sample = random.choice(blist)
print('Sample: %s (%s)' % (sample, str(type(sample))))

match = re.findall(blank_pattern, sample)
if match:
    nb_blanks = len(match)
    print('Found %s match(es).' % str(nb_blanks))

    words = sample.split('____')

    answers = answer_getter(nb_blanks)

    print('Answers:')
    for a in answers:
        print a

    line = sample
    for an in answers:
        # line = re.sub(blank_pattern, an, line)
        line = line.replace('____', an, 1)

    print line

add_to_list('sa bite', wlist)
add_to_list('toto', wlist)

print(sample)

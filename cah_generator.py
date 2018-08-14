import csv
import random
import re


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


blank_pattern = '(____)'

wfile = 'whitelist.csv'
bfile = 'blacklist.csv'

with open(bfile, 'rb') as f:
    reader = csv.reader(f, delimiter='\n')
    blist = [item for sublist in list(reader) for item in sublist]

with open(wfile, 'rb') as f:
    reader = csv.reader(f, delimiter='\n')
    wlist = [item for sublist in list(reader) for item in sublist]

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

print(sample)

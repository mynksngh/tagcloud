import string
import re
from operator import itemgetter
item1 = itemgetter(1)


def get_words(input_file):
    list_data = []
    print input_file
    # with open("myfile.txt") as f:
    file_path = 'media/'
    with open('media/'+input_file) as f:
        for line in f:
            for word in re.findall(r'\w+', line):
                    list_data.append(word)

    # data_more = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in list_data]
    # data_more = [re.sub(r'[^A-Za-z]+', '', x) for x in list_data]
    data_more = [''.join(x for x in par if x not in string.punctuation) for par in list_data]
    # string.punctuation
    # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    words = data_more

    # remove 's
    words = [word[:-2] if word.lower().endswith("'s") else word
                     for word in words]

    # remove numbers
    words = [word for word in words if not word.isdigit()]

    words = [s.lower() for s in words if s]
    print words
    noise_list = set([x.strip() for x in open('media/noise_words.txt').read().split('\n')])
    stopwords = set([i.lower() for i in noise_list])
    words = [word for word in words if word.lower() not in stopwords]
    from collections import Counter
    c = Counter(words)
    # print c
    # print type(c)
    # print c.get('a')

    # print Counter(words).keys() # equals to list(set(words))
    # print Counter(words).values() # counts the elements' frequency
    # print zip(Counter(words).keys() , Counter(words).values()

    # print dict((k,dict(c)[k]) for k in noise_list)
    dict_data = dict(c)

    print dict_data

    # def remKeys(dictionary, list):
    #     for i in list:
    #         if i in dictionary.keys():
    #             dictionary.pop(i)
    #     return dictionary

    # make sure frequencies are sorted and normalized
    frequencies = dict(c)
    frequencies = sorted(frequencies.items(), key=item1, reverse=True)

    # largest entry will be 1
    max_frequency = float(frequencies[0][1])

    frequencies = [(word, freq / max_frequency) for word, freq in frequencies]

    return frequencies


def list_dictionary(filename):
    # Pass the function a filename (string)

    # set up a dict to hold the results

    result = dict()

    # open the file and pass it to enumerate
    # this combination returns something like a list of
    # (index i.e. line number, line) pairs, which you can
    # iterate over with the for-loop
    # with open('media/' + input_file)
    for idx, line in enumerate(open('media/'+filename)):

        # now take each line, strip any whitespace (most notably,
        # the trailing newline character), then split the
        # remaining line into a list of words contained in that line

        words = line.strip().split()

        # now iterate over the list of words

        for w in words:

            # if this is the first time you encounter this word,
            # create a list to hold the line numbers within
            # which this word is found

            if w not in result:
                result[w] = []

            # now add the current line number to the list of results for this word

            result[w].append(idx)

    # after all lines have been processed, return the result
    return result
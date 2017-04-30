import re


def get_words(input_file):
    list_data = []
    with open('media/'+input_file) as f:
        for line in f:
            for word in re.findall(r'\w+', line):
                    list_data.append(word)

    return list_data


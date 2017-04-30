import re


def find_word(text_file, word):
    word_count = 0
    line_list = []
    with open('media/' + text_file) as db_file:
        for line_no, line in enumerate(db_file):
            line = line.lower()
            word = word.lower()
            r = re.compile(r'\b%s\b' % word, flags=re.I | re.X)
            if r.findall(line):
                line_list.append(line)
                word_count += 1
            else:
                pass
    return {'line_contains_word': line_list, 'word_count': word_count}
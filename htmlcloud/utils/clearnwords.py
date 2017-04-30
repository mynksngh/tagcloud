import re
import sys


def do_clean_text(text):
    """ It simple takes the Input Text and remove the Noise word i.e. english words"""

    noisewords = set([x.strip() for x in open('media/noise_words.txt').read().split('\n')])
    print noisewords
    stopwords = set([i.lower() for i in noisewords])

    flags = (re.UNICODE if sys.version < '3' and type(text) is unicode
             else 0)
    regexp = r"\w[\w']+"

    words = re.findall(regexp, text, flags)
    # remove stopwords
    words = [word for word in words if word.lower() not in stopwords]
    # remove 's
    words = [word[:-2] if word.lower().endswith("'s") else word
             for word in words]
    # remove numbers
    words = [word for word in words if not word.isdigit()]
    return words
import re
import sys


def do_clean_text(text):
    """ It simple takes the Input Text and remove the Noise word i.e. english words"""
    noise_words = set([x.strip() for x in open('media/noise_words.txt').read().split('\n')])
    stopwords = set([i.lower() for i in noise_words])
    # remove stopwords
    words = text
    words = [word for word in words if word.lower() not in stopwords]
    # remove numbers
    words = [word for word in words if not word.isdigit()]
    # Lowers The Remaining tokens in lower format
    words = [s.lower() for s in words if s]
    return words

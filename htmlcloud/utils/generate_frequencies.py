from operator import itemgetter
item1 = itemgetter(1)


def generate_frequencies(words_list):
    """Create a word_cloud from words and frequencies.
       Parameters
       ----------
       words_list : It will the list of all tokens after perfroming all operation like clean, noise data removal
       Returns
       -------
       It will return the dict of unique words as key and number of occurance as value
       """
    max_frequency_allowed = 10  # Set this for not making to much bigger font size on html page
    from collections import Counter
    c = Counter(words_list)
    # Sort the dict of all keys based on there occurance
    frequencies = dict(c)
    frequencies = sorted(frequencies.items(), key=item1, reverse=True)
    # largest entry will be 1

    max_frequency = float(frequencies[0][1])
    if max_frequency > max_frequency_allowed:
        max_frequency = max_frequency_allowed
    frequencies = [(word, freq / max_frequency) for word, freq in frequencies]
    return frequencies

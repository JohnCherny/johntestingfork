# Longest Word in a Sentence
# Write a function that takes a sentence as input and returns
# the longest word in the sentence. If multiple words are tied
# for longest, return the first one. Punctuation should not be
# considered part of a word.

def longest_word(sentence):
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")

    if sentence.strip() == "":
        return ""

    words = []
    for raw in sentence.split():
        # Remove punctuation from start/end
        cleaned = raw.strip(".,!?;:\"'()[]{}")
        if cleaned:
            words.append(cleaned)

    if not words:
        return ""

    return max(words, key=len)

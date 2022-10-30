import re
from collections import Counter


class WordCount(object):

    def __init__(self, sentences):
        self.sentences = sentences

    def cleanup_sentences(self):
        lowered_sentences = self.sentences.lower()
        sentences = re.sub(r'[.!?,:;]', '', lowered_sentences)
        return sentences.strip()

    def count_words(self):
        sentences = self.cleanup_sentences()
        words = sentences.split(' ')

        return Counter(words)


if __name__ == '__main__':
    sentences = "Hi how are things? How are you? Are you a developer? I am also a developer"
    counter = WordCount(sentences)
    result = counter.count_words()

    for word, count in result.items():
        print("%s: %d" % (word, count))

import unittest
from word_counts import WordCount

class TestWordCount(unittest.TestCase):
    def test_count_words(self):
        sentences = "Hello world for hello world"
        expected_result = {
            'hello': 2,
            'world': 2,
            'for': 1
        }

        counter = WordCount(sentences)
        result = counter.count_words()
        assert len(result) == len(expected_result)
        assert result == expected_result
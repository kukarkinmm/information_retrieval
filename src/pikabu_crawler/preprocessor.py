"""
Module for processing Pikabu Article
"""
import re


class PikabuPreprocessor:
    """This class represents processing
    """

    def __init__(self, stop_words=None, remove_punctuation=True, remove_links=True):
        """The constructor
        @:param stop_words: list
        @:param remove_punctuation: boolean
        @:param remove_links: boolean
        """
        self.stop_words = stop_words
        self.remove_punctuation = remove_punctuation
        self.remove_links = remove_links

    def __call__(self, text):
        """Applies all of processing methods to text
        @:param self: the object pointer
        @:param text: str
        """
        text = text.lower()
        return self.__remove_spaces(self.__stop_words_removal(self.__punctuation_removal(self.__links_removal(text))))

    def __punctuation_removal(self, line):
        if self.remove_punctuation:
            return re.sub(r'[^\w\s]', '', line)
        else:
            return line

    def __links_removal(self, line):
        if self.remove_links:
            return re.sub(
                r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s(
                )<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
                " ", line)
        else:
            return line

    def __stop_words_removal(self, line):
        if self.stop_words is not None:
            return " ".join([word for word in line.split() if word not in self.stop_words])
        else:
            return line

    @staticmethod
    def __remove_spaces(line):
        return re.sub(r'\s+', ' ', line)

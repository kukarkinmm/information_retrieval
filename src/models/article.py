"""Article model
"""

class Article:
    """This class represents Pikabu article model
    """
    __slots__ = ["date", "title", "text", "author", "tags", "rating", "n_comments", "n_views"]

    def __init__(self, date, title, text, author, tags, rating, n_comments, n_views):
        """The constructor
        @:param date:
        @:param title:
        @:param text:
        @:param author:
        @:param tags:
        @:param rating:
        @:param n_comments:
        @:param n_views:
        """
        self.date = date
        self.title = title
        self.text = text
        self.author = author
        self.tags = tags
        self.rating = rating
        self.n_comments = n_comments
        self.n_views = n_views

    def __str__(self):
        return str(self.date) + "\t" + str(self.title) + "\t" + str(self.text) + "\t" + str(self.author) + "\t" + str(
            self.tags) + "\t" + str(self.rating) + "\t" + str(self.n_comments) + "\t" + str(self.n_views)

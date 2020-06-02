

class Article:

    __slots__ = ["title", "text", "author", "tags", "rating", "n_comments"]

    def __init__(self, title, text, author, tags, rating, n_comments):
        self.title = title
        self.text = text
        self.author = author
        self.tags = tags
        self.rating = rating
        self.n_comments = n_comments

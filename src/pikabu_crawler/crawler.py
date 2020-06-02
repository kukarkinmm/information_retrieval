"""Crawler module
"""
import requests
import os
from bs4 import BeautifulSoup


class PikabuCrawler:
    """This class represents crawler for pikabu.ru"""
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.1.197 Yowser/2.5 Safari/537.36"
    }

    POST_TYPES = {"text": 2, "picture": 4, "video": 8}
    DATE_RANGE = range(3000, 4200, 1)
    PATH = "../../data/"

    def __init__(self, post_type="text", filename="pikabu.csv", verbose=True):
        """The constructor
        @:param post_type: string
        @:param filename: string
        @:param verbose: boolean
        """
        self.url = f"https://pikabu.ru/search?n={self.POST_TYPES[post_type]}&r=3" + "&d={}&D={}&page={}"
        self.dataset = set()
        self.output_file = open(self.PATH + filename, 'w', encoding='utf-8')
        self.verbose = verbose

    def download(self, pages=10):
        """Download method

        Downloads 10 pages of content by default
        @:param pages: int
        """
        article_counter = 0
        for date_range in self.DATE_RANGE:
            for i in range(pages):
                if self.verbose:
                    print(f"Date: {date_range}\tPage: {i}\tArticles loaded: {article_counter}")
                response = requests.get(self.url.format(date_range, date_range, i + 1), headers=self.HEADERS)
                soup = BeautifulSoup(response.text, "lxml")
                articles = soup.findChildren("article")

                for article in articles:
                    title = self.__get(article, "h2", {"class": "story__title"})
                    text = self.__get(article, "div", {"class": "story__content-inner"})
                    author = self.__get(article, "div", {"class": "user__info-item"})
                    tags = self.__get(article, "div", {"class": "story__tags tags"})
                    rating = self.__get(article, "div", {"class": "story__rating-count"})
                    n_comments = self.__get(article, "span", {"class": "story__comments-link-count"})
                    n_views = self.__get(article, "div", {"class": "story__views hint"})
                    date = [item["datetime"] for item in article.select("time")]

                    if tags is not None:
                        tags = tags.split()
                    # self.dataset.add(Article(title, text, author, tags, rating, n_comments))
                    self.output_file.write(
                        str(date) + "\t" + str(title) + "\t" + str(text) + "\t" + str(author) + "\t" + str(
                            tags) + "\t" + str(rating) + "\t" + str(n_comments) + "\t" + str(n_views) + "\n")

                    article_counter += 1
        self.output_file.close()

    def save_to_csv(self, filename="pikabu.csv"):
        if len(self.dataset) == 0:
            return

        if not os.path.exists(self.PATH):
            os.makedirs(self.PATH)

        with open(self.PATH + filename, 'w', encoding='utf-8') as out:
            for datum in self.dataset:
                out.write(str(datum.title) + "\t" + str(datum.text) + "\t" + str(datum.author) + "\t" + str(
                    datum.tags) + "\t" + str(datum.rating) + "\t" + str(datum.n_comments) + "\n")

    @staticmethod
    def __get(article, tag, args):

        try:
            title = article.find(tag, args).text
            return title.strip().replace('\n', '').replace('\t', ' ')
        except AttributeError:
            return None

"""Demo script

"""
from crawler import PikabuCrawler
from preprocessor import PikabuPreprocessor
from src.models.article import Article

if __name__ == "__main__":
    # crawler = PikabuCrawler()
    # crawler.download()

    preprocessor = PikabuPreprocessor()
    error_counter = 0
    writes_counter = 0
    short_articles_counter = 0

    with open("../../data/pikabu_clear.csv", 'w', encoding='utf-8') as f:
        with open("../../data/pikabu.csv", 'r', encoding='utf-8') as g:
            for line in g:
                try:
                    article = Article(*line.replace('\n', '').split('\t'))
                except TypeError:
                    print("TypeError due to splitting: will be fine with new version of dataset")
                    error_counter += 1
                    continue
                article.text = preprocessor(article.text)
                if len(article.text) < 2000:
                    short_articles_counter += 1
                    continue
                f.write(str(article) + "\n")
                writes_counter += 1
    print(f"TypeErrors: {error_counter}\nClean Articles: {writes_counter}\nShort articles: {short_articles_counter}")

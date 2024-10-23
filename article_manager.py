import json
import os

class ArticleManager:
    def __init__(self, articles_dir='articles'):
        self.articles_dir = articles_dir
        if not os.path.exists(articles_dir):
            os.makedirs(articles_dir)

    def get_all_articles(self):
        articles = []
        for filename in os.listdir(self.articles_dir):
            if filename.endswith('.json'):
                with open(os.path.join(self.articles_dir, filename), 'r') as f:
                    articles.append(json.load(f))
        return articles

    def get_article(self, article_id):
        filename = f'article{article_id}.json'
        with open(os.path.join(self.articles_dir, filename), 'r') as f:
            return json.load(f)

    def add_article(self, title, content):
        article_id = len(self.get_all_articles()) + 1
        article = {
            'id': article_id,
            'title': title,
            'content': content,
            'date': '2023-10-01'  # Замените на текущую дату
        }
        with open(os.path.join(self.articles_dir, f'article{article_id}.json'), 'w') as f:
            json.dump(article, f)

    def edit_article(self, article_id, title, content):
        filename = f'article{article_id}.json'
        article = {
            'id': article_id,
            'title': title,
            'content': content,
            'date': '2023-10-01'  # Замените на текущую дату
        }
        with open(os.path.join(self.articles_dir, filename), 'w') as f:
            json.dump(article, f)

    def delete_article(self, article_id):
        filename = f'article{article_id}.json'
        os.remove(os.path.join(self.articles_dir, filename))
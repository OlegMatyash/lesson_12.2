import json

from exceptions import DataLayerError

class PostsHandler:

    def __init__(self, path):

        self.path = path

    def load_posts_from_json(self):

        try:
            with open(self.path, "r", encoding="utf-8") as file:
                posts = json.load(file)
            return posts
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataLayerError("Ошибка в файле")

    def search_posts_for_substring(self, substring):

        substring_lower = substring.lower()
        posts_found = []

        posts = self.load_posts_from_json()
        for post in posts:
            if substring_lower in post["content"].lower():
                posts_found.append(post)

        return posts_found

    def add_post(self, post):

        posts = self.load_posts_from_json()
        posts.append(post)
        self.save_posts_to_json(posts)

    def save_posts_to_json(self, posts):

        try:
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump(posts, file)
        except FileNotFoundError:
            raise DataLayerError

#posts_handler = PostsHandler("posts.json")
#posts_handler.add_post({"pic":1, "content":2})
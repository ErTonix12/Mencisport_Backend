
import pymysql
import os
from post import PostModel

class PostRepository(object):
    def __init__(self,host: str, port: int, user: str, password:str,database: str):
        self.connector = pymysql.connect(
            host=os.environ["DATABASE_HOST"],
            user=os.environ["DATABASE_USER"],
            port=os.environ["DATABASE_PORT"],
            password=os.environ["DATABASE_PASSWORd"],
            database=os.environ["DATABASE_NAME"]
        )
        self.cursor = self.connector.cursor()
    
    def get_daily_posts(self) -> list:
        posts = []
        self.cursor.execute(
            "SELECT post_title,post_date, post_content FROM wp_posts WHERE post_type='post'"
        )
        for raw_post in self.cursor.fetchall():
            posts.append(
                PostModel(
                    title=raw_post[0],
                    body=raw_post[2],
                    date=raw_post[1]
                ).return_json_format()
            )
        return posts
    
    def __del__(self):
        self.connector.close()
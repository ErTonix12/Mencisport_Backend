import datetime
import re
import json

class PostModel(object):

    def __init__(self,title: str, body: str, date: datetime.date):
        self.title = title
        self.body = self.remove_html_tags(body)
        self.date = date
    
    @staticmethod
    def remove_html_tags(body:str) -> str:
        clean_regex = re.compile('<.*?>')
        return re.sub(clean_regex, '', body)

    def return_json_format(self) -> dict:
        return {
            'title': self.title,
            'body': self.body,
            'date': self.date.strftime("%Y-%m-%d")
        }
import uuid
import datetime
from database import Database as db

class Post():

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.now(),id=None):
        current_time=datetime.datetime.now()
        date_f = current_time.strftime("%d/%m/%Y %H:%M:%S")
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.date = date_f
    
    def save_to_mongo(self):
        db.insert(collection='posts', data=self.json())

    def json(self):
        return{
            'id': self.id,
            'blog_id' : self.blog_id,
            'author': self.author,
            'created_date' : self.date,
            "title" : self.title,
            'content' : self.content
        }
    
    @classmethod
    def from_mongo(cls,id):
        post_data = db.find_one(collection='posts', query={'id': id})
        return cls(
            blog_id = post_data['blog_id'], 
            title = post_data['title'], 
            content = post_data['content'], 
            author = post_data['author'], 
            id=post_data['id'])

    @staticmethod
    def from_post(id):
        return [ post for post in db.find(collection='posts', query={'blog_id': id})]

    
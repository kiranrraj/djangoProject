import datetime, uuid
from .post import Post
from database import Database as db

class Blog():

    def __init__(self, title, author, desc, id=None):
        self.title = title
        self.author = author
        self.desc = desc
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        date_now = datetime.datetime.now()
        date_f = date_now.strftime("%d/%m/%Y %H:%M:%S")
        print(f'{"-"*10} Create a new post {"-"*10} ')
        title = input("Enter title for the post : ")
        content = input("Enter content for the post : ")
        author = input("Enter the author name for the post : ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date_f)
        post.save_to_mongo()

    def save_blog(self):
        db.insert(collection='blogs', data=self.json())

    def json(self):
        return{
            'author': self.author,
            'created_date' : self.date,
            "title" : self.title,
            'desc' : self.desc
        }

    def get_posts(self):
        return Post.from_post(self.id)
    
    @classmethod
    def get_from_mongo(cls, id):
         blog_data = db.find_one(collection='blogs', query={'id':id})
         return cls(
             author=blog_data['author'],
             title=blog_data['title'],
             id=blog_data['blog_id'],
             desc=blog_data['desc']
         )
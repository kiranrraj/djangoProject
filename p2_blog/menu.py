from database import Database
from models.blog import Blog


class Menu():

    def __init__(self):
        self.user = input("Enter your author name : ")
        self.user_blog = None
        if self._user_exist():
            print(f"Welcome, {self.user}")
        else:
            self._createUser()
        
    
    def _user_exist(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['id'])
            return True
        else:
            return False


    def _createUser(self):
        title = input("Enter a blog title : ")
        desc = input("Enter blog description : ")
        blog = Blog(
            author = self.user, 
            title = title, 
            desc = desc, 
            )
        blog.save_blog()
        self.user_blog = blog


    def run_menu(self):
        read_write = input("Do you want to read (R) or write (W) blogs ?")
        if read_write.lower() == 'r':
            self._list_blogs()
            self._view_blog()
        elif read_write.lower() == 'w':
            self.user_blog.new_post()
        else:
            print("Thank you")


    def _list_blogs(self):
        blogs = Database.find(
            collection='blogs',
            query={}
        )

        for blog in blogs:
            print(f"ID: {blog['id']}, Title: {blog['title']}, Author: {blog['author']}")


    def _view_blog(self):
        blog_id_v = input("Enter the blog id to view the blog : ")
        blog = Blog.get_from_mongo(blog_id_v)
        posts = blog.get_posts()
        for post in posts:
            print(f"Date: {post['created_date']}\n Title: {post['title']}\n Content : {post['content']}\n Author: {post['author']}")
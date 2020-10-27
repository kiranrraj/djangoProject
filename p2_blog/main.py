from database import Database
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()


# post = Post(1004, 'my fourth blog', 'my fourth blog content', 'kiran rr', None)
# post.save_to_mongo()
# import pymongo
# URI = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(URI)
# db = client['library']
# collection = db['books']
# book = collection.find({})
# for elem in book:
#     print(elem)
# post = Post("my post", "my post content", "kiran" )

# blog = Blog(
#     author='kiran rr',
#     title='my first blog',
#     desc='my content',
#     blog_id=1001
#     )

# blog.new_post()
# blog.save_blog()
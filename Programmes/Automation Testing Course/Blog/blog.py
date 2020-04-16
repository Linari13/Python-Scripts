from post import Post

class Blog():
    def __init__(self, title: str, author: str) -> object:
        self.title = title
        self.author = author
        self.posts = []

    # repr method that returning a simple identifier of the blog created
    def __repr__(self):
        #Returns string "Title" by "Author" ( "x" post(s)).
        #The word post takes its plural form automatically when needed
        return f'{self.title} by {self.author} ({len(self.posts)} post{"s" if len(self.posts)>1 else ""})'

    #Function creating a new post within the blog
    def create_post_in_blog(self, title, content):
        self.posts.append(Post(title, content))

    # Function returning json dictionary of the blog
    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }


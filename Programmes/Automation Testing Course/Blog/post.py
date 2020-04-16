class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    #Example of a repr method that returns a simple identifier of the object created
    def __repr__(self):
        return f'<{self.title}: {self.content}>'

    #Function returning json dictionnary
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }

#Salut = Post('Salut','Bonjour et Bienvenue sur mon Blog')
#print(Salut.json())
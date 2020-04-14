from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    #Function testing blog creation function
    def test_create_blog(self):
        #we create a fake blog
        b = Blog('Test','Test Author')

        #We test title, author, and posts list
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    # Function testing the repr function
    def test_repr(self):
        # we create blogs
        b = Blog('Test', 'Test Author')
        b2 = Blog('Mon Blog', 'Fred')
        b2.posts = ['post1', 'post2', 'post3']

        # We test the reprs generated
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 post)')
        self.assertEqual(b2.__repr__(), 'Mon Blog by Fred (3 posts)')
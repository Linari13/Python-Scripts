from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

    #Function testing the creation of a post within the blog
    def test_create_post_in_blog(self):
        #Creating new blog with a new post inside
        b = Blog('MonBlog', 'Fred')
        b.create_post_in_blog('Salut', 'coucou me voila')

        #Testing post creation
        self.assertEqual(b.posts[0].title, 'Salut')
        self.assertEqual(b.posts[0].content, 'coucou me voila')

        #Creating a 2nd post
        b.create_post_in_blog('Deuxieme message', 'De la baballe')
        # Testing post append
        self.assertEqual(b.posts[1].title, 'Deuxieme message')
        self.assertEqual(b.posts[1].content, 'De la baballe')

    #Function testing json with no post
    def test_json_no_post(self):
        #Blog creation
        b2 = Blog('Mon Blog', 'Fred')
        expected = {'title': 'Mon Blog', 'author': 'Fred', 'posts': []}

        self.assertDictEqual(expected, b2.json())

    #Function testing the json function
    def test_json(self):
        #Blog creation
        b2 = Blog('Mon Blog', 'Fred')
        #1st Post creation
        b2.create_post_in_blog('Post1','Content1')
        expected1 = {
                        'title': 'Mon Blog',
                        'author': 'Fred',
                        'posts': [ {'title': 'Post1', 'content': 'Content1'}]
                    }

        #Testing 1 unique post
        self.assertDictEqual(expected1, b2.json())

        #2nd and 3rd Post Creation
        b2.create_post_in_blog('Post2','Content2')
        b2.create_post_in_blog('Post3','Content3')
        expected2 = {'title': 'Mon Blog',
                     'author': 'Fred',
                     'posts': [
                                {'title' : 'Post1', 'content' : 'Content1'},
                                {'title' : 'Post2', 'content' : 'Content2'},
                                {'title' : 'Post3', 'content' : 'Content3'}
                              ]
                    }

        # Testing several posts
        self.assertDictEqual(expected2, b2.json())
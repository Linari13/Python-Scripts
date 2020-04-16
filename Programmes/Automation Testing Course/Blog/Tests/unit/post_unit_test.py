from unittest import TestCase
from post import Post

class PostTest(TestCase):
    #Function testing the post creation function
    def test_create_post(self):
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    #Function testing the repr function
    def test_repr(self):
        p = Post('Test', 'Test Content')

        self.assertEqual(p.__repr__(), '<Test: Test Content>')

    #Function testing the json function
    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, p.json())

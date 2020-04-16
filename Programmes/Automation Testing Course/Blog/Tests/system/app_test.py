from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class Apptest(TestCase):

    def setUp(self):
        blog = Blog('Test', 'Test Author')                                      #Create a new blog object
        app.blogs = {'Test' : blog}

    #Testing input function is called
    def test_menu_prints_prompt(self):
        # we patch the builtin input method (replace the input function with a mock)
        with patch('builtins.input', return_value = 'q') as mocked_input:
            app.menu()
            # We check that the input function has been called with the correct value
            mocked_input.assert_called_with(app.MENU_PROMPT)

    #Testing print blog function is called
    def test_menu_calls_print_blogs(self):
        # we patch the "print_blogs" method from tha app1 file (replacing it with a mock)
        with patch('app1.print_blogs') as mocked_print_blogs:

            #Patching input method (for the test to not wait for an user's input)
            # we simulate the input q as returned value
            with patch('builtins.input', return_value='q') as mocked_input:
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Blog Title', 'Blog Author', 'q')
            app.menu()

            self.assertEqual(app.blogs['Blog Title'].title, 'Blog Title')
            self.assertEqual(app.blogs[ 'Blog Title' ].author, 'Blog Author')

            """ #Another way to do it would be:
            with patch ('app1.ask_create_blog') as mocked_ask_create_blog:
                app1.menu()
                mocked_ask_create_blog.assert_called()
                
                                 -> but in that case no need for 'Blog Title', 'Blog Author' effects"""

    def test_menu_calls_list_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            with patch ('app1.print_blogs') as mocked_print_blogs:
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_read_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('r', 'q')
            with patch ('app1.ask_read_blog') as mocked_ask_read_blog:
                app.menu()
                mocked_ask_read_blog.assert_called()

    def test_menu_calls_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p','Test', 'Post Title', 'Post Content', 'q')

            self.assertEqual(app.blogs['Test'].title, 'Test')
            self.assertEqual(app.blogs[ 'Test' ].author, 'Test Author')

            """ #Another way to test it would be:
            
            with patch ('app1.ask_create_post') as mocked_ask_create_post:
                app1.menu()
                mocked_ask_create_post.assert_called()          
                                
                                -> but in this case no need for 'Blog Title', 'Post Title', 'Post Content', effects"""

    #Testing blog list is printed
    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:                           #Patching print method (replacing it with a mock)
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 post)')   #Checking print function call (with correct value)

    #Testing ask_create_blog is called
    def test_ask_create_blog(self):
        #Patch input method (for the test to not wait for input)
        #Simulating input "c" as returned value
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')                  #Simulating 2 inputs
            app.ask_create_blog()                                               #Calling function
            self.assertIsNotNone(app.blogs.get('Test'))                         #Checking "Test" key is paired with smtg

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value = 'Test') as mocked_input:
            with patch('app1.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post_in_blog('Test Post', 'Test Content')

        with patch('app1.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post Content')
        expected = '--- Post title ---\nPost Content'
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected)

    def test_ask_create_post_no_blog(self):
        #test no blog
        app.blogs =[]
        with patch('builtins.print') as mocked_print:
            app.ask_create_post()
            mocked_print.assert_called_with('there\'s no blog to update')

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Post Title', 'Post Content')
            with patch('blog.Blog.create_post_in_blog') as mocked_create_post_in_blog:
                app.ask_create_post()
                mocked_create_post_in_blog.assert_called_with('Post Title', 'Post Content')




from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class Apptest(TestCase):

    """#Testing ask_create_blog is called
    def test_calls_ask_create_blog(self):
        # we patch the "ask_create_blog" method from tha app file (replacing it with a mock)
        with patch('app.ask_create_blog') as mocked_ask_create_blog:
            # we patch the builtin input method for the test to not wait for an user's input
            # we simulate the input "c" as returned value
            with patch('builtins.input', return_value='c' ) as mocked_input:
                app.menu()
                mocked_ask_create_blog.assert_called()"""


    #Testing input function is called
    def test_menu_prints_prompt(self):
        # we patch the builtin input method (replace the input function with a mock)
        with patch('builtins.input') as mocked_input:
            app.menu()
            # We check that the input function has been called with the correct value
            mocked_input.assert_called_with(app.MENU_PROMPT)

    #Testing print blog function is called
    def test_menu_calls_print_blogs(self):
        # we patch the "print_blogs" method from tha app file (replacing it with a mock)
        with patch('app.print_blogs') as mocked_print_blogs:

            # we patch the builtin input method for the test to not wait for an user's input
            # we simulate the input q as returned value
            with patch('builtins.input', return_value='q' ) as mocked_input:
                app.menu()
                mocked_print_blogs.assert_called()

    #Testing blog list is printed
    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')              #Create a new blog object
        app.blogs = {'Test' : blog}                     #Sets the blog variable of the app file

        # we patch the builtin print method (replace the print function with a mock)
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            # We check that the print function has been called with the correct value
            mocked_print.assert_called_with('- Test by Test Author (0 post)')
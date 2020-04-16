from blog import Blog

MENU_PROMPT='Enter : \n- "c" to list blogs\n- "l" to list blogs\n- "r" to read one\n- "p" to create a post\n- "q" to quit'
POST_TEMPLATE = '--- {} ---\n{}'

blogs = dict() # blog_name : Blog object

def menu():
    """ Show the user the available blogs
        Let the user make  a choice
        Do something with that choice
        Eventually exit """

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():                                                 #Print the available blogs
        print(f'- {blog}')

def ask_create_blog():
    title = input('Please enter the blog\'s title: ')                               #Asks user for new blog title
    author = input('Please enter author name: ')                                    #Asks user for author name
    blogs[title] = Blog(title, author)                                              #Creates and append new blog

def ask_read_blog():
    if len(blogs) > 0:
        desired_blog = input('Which blog do you want to read?: ')                   #Asks user for desired blog
        while desired_blog not in blogs:                                            #While blog requested doesn't exists
            desired_blog = input('Please enter an existing blog: ')                 #Asks user for an existing blog
        print_posts(blogs[desired_blog])                                                   #Printing blog posts
    else :
        print('there\'s no blog to read')                                           #No existing blog message

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    if len(blogs) == 0:                                                             #If blog dict's empty : exit
        print('there\'s no blog to update')
    else:
        desired_blog = input('Which blog do you want to write your post in? : ')   #Asks user for blog to update
        #if requested blog doesn't exist ask for existing blog
        while desired_blog not in blogs:
            desired_blog = input('please enter an existing blog : ')                #Asks user for an existing blog

        post_title = input('Enter the post title: ')                                #Get post title
        post_content = input('Enter post content: ')                                #Get post content

        blogs[desired_blog].create_post_in_blog(post_title, post_content)           #Create post in blog
        #print(f'Your post has been added to {desired_blog}')                        #Confirmation message
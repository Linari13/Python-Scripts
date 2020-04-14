from blog import Blog

MENU_PROMPT='Enter : \n- "c" to list blogs\n- "l" to list blogs\n- "r" to read one\n- "p" to create a post\n- "q" to quit'
blogs = dict() # blog_name : Blog object

def menu():
    #Show the user the available blogs
    #Let the user make  a choice
    #Do something with that choice
    #Eventually exit

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
    #print the available blogs
    for key, blog in blogs.items():
        print(f'- {blog}')

def ask_create_blog():
    title = input('Please enter the blog\'s title: ')   #Asks user for new blog title
    author = input('Please enter author name: ')        #Asks user for author name
    blogs[title] = Blog(title, author)                  #Creates new blog object and adds it to blogs list

def ask_read_blog():
    desired_blog = input('which blog do you want to read? : ')  #Asks user for desired blog
    if len(blogs) > 0:
        while desired_blog not in blogs:
            desired_blog = input('please enter an existing blog : ')  # Asks user for an existing blog
        for post in desired_blog.posts:
            print(post.title)
            print(post.content)

def ask_create_post():
    pass
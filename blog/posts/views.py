from django.shortcuts import render  # Imports render(), which combines an HTML template with data. It is not used in this example.
from django.http import HttpResponse  # Imports HttpResponse, which lets a Django view send text or HTML back to the browser.

# This file contains views: functions that receive web requests and return responses.
posts = [  # Creates a variable called posts containing a list. Each item represents one blog post.
    {  # Starts a dictionary containing the first post's information as key-value pairs.
        'id': 1,  # The key 'id' stores the integer 1, used here to identify the first post.
        'title': 'Introduction to Python',  # The key 'title' stores the post's heading as a string.
        'content': 'Python is a simple and powerful programming language.'  # The key 'content' stores the post's main text.
    },  # Ends the first dictionary. The comma separates it from the next item in the list.
    {  # Starts the dictionary for the second post.
        'id': 2,  # Assigns the second post an ID of 2.
        'title': 'Getting started with Django',  # Stores the second post's title.
        'content': 'Django helps you build web applications using Python.'  # Stores the second post's main text.
    },  # Ends the second dictionary and separates it from the third.
    {  # Starts the dictionary for the third post.
        'id': 3,  # Assigns the third post an ID of 3.
        'title': 'Django the best web framework',  # Stores the third post's title.
        'content': 'Django is used to build powerful and scalable web applications.'  # Stores the third post's main text.
    }  # Ends the third dictionary. A comma after the final item is optional.
]  # Ends the list. All three post dictionaries are now stored in posts.

# Usecase1: helloworld
def helloworld(request):  # This function definition is commented out, so Python does not execute it.
    return HttpResponse('<h1>Hello, World!</h1>')  # If enabled, this would return a response displaying a heading.

## Usecase2: home with posts where the posts are stored in a list of dictionaries. The view loops through the list and generates HTML for each post.
def home(request):  # Defines a view named home. Django passes an HttpRequest object into request when this view is called.
    html = ""  # Creates an empty string that will gradually hold the HTML for all the posts.
    for post in posts:  # Loops through the posts list, assigning one dictionary at a time to the variable post.
        # += appends text to html; f allows expressions inside braces; triple quotes allow a string to span multiple lines.
        html += f'''
          <div>
            <h1>{post['id']}. {post['title']}</h1>
            <p>{post['content']}</p>
          </div>
        '''
        # The opening triple quotes above begin the multiline f-string.
        # <div> starts an HTML container that groups one post's heading and content.
        # <h1> creates a heading: post['id'] inserts the ID, and post['title'] inserts the title.
        # The period and space between the two expressions produce a heading such as "1. Introduction to Python".
        # <p> creates a paragraph, and post['content'] inserts the current post's main text.
        # </div> closes the container for the current post.
        # The closing triple quotes end the string. The loop then repeats for the next post.
    return HttpResponse(html)  # After the loop finishes, sends the accumulated HTML to the browser in an HTTP response.

def post(request, id):  # Defines a view named post that takes an additional parameter id.
    print(id)  # Prints the id to the console for debugging purposes.
    return HttpResponse(id)  # Sends the generated HTML to the browser.
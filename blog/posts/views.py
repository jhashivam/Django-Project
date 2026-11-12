from django.shortcuts import render  # Imports render(), which combines an HTML template with data. It is not used in this example.
from django.http import HttpResponse , HttpResponseNotFound  # Imports HttpResponse and HttpResponseNotFound, which let a Django view send text or HTML back to the browser.

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
        html += f''' # Generates HTML for each post using an f-string. The opening triple quotes allow the string to span multiple lines.
          <div> # Starts an HTML container that groups one post's heading and content.
            <a href="/post/{post['id']}/"> # Creates a hyperlink to the individual post's page. The href attribute specifies the URL, which includes the post's ID.
            <h1>{post['id']}. {post['title']}</h1> # Creates a heading for the post. The post's ID and title are inserted into the heading using expressions inside braces.
            </a> # Closes the hyperlink tag. The heading is now clickable, and clicking it will navigate to the individual post's page.
            <p>{post['content']}</p> # Creates a paragraph containing the post's main text. The content is inserted using an expression inside braces.
          </div> # Closes the container for the current post. The loop then repeats for the next post.
        ''' # The closing triple quotes end the multiline f-string. The loop then continues to the next post in the list.
        # The opening triple quotes above begin the multiline f-string.
        # <div> starts an HTML container that groups one post's heading and content.
        # <h1> creates a heading: post['id'] inserts the ID, and post['title'] inserts the title.
        # The period and space between the two expressions produce a heading such as "1. Introduction to Python".
        # <p> creates a paragraph, and post['content'] inserts the current post's main text.
        # </div> closes the container for the current post.
        # The closing triple quotes end the string. The loop then repeats for the next post.
    return HttpResponse(html)  # After the loop finishes, sends the accumulated HTML to the browser in an HTTP response.

def post(request, id):  # Defines a view named post that takes an additional parameter id.
    valid_Id = False  # Initializes a boolean variable validId to False. This will track whether a matching post ID is found.
    for post in posts:  # Loops through the posts list, assigning one dictionary at a time to the variable post.
        if post['id'] == id:  # Checks if the current post's ID matches the id parameter passed to the view.
            post_dict = post  # If a match is found, assigns the current post dictionary to post_dict.      
            valid_Id = True  # If a match is found, sets validId to True.
            break  # Exits the loop early since a matching post has been found.
    if valid_Id:  # Checks if validId is True, indicating a matching post ID was found.
            html = f''' # Generates HTML for the specific post using an f-string.
                <div> # Starts an HTML container for the post's heading and content.
                    <h1>{post_dict['id']}. {post_dict['title']}</h1> # Creates a heading with the post's ID and title.
                    <p>{post_dict['content']}</p> # Creates a paragraph with the post's main text.
                </div> # Closes the container for the post.
                ''' # The closing triple quotes end the multiline f-string. The generated HTML is now stored in the variable html.
            # If a match is found, generates HTML for that specific post using an f-string.
            return HttpResponse(html)  # Sends the generated HTML to the browser.
    else:  # If no matching post ID is found after the loop, executes the following block.
            return HttpResponseNotFound("Post not available \U0001F642")  # Sends   
  
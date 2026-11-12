from django.shortcuts import render  # Imports render(), which combines an HTML template with data. It is not used in this example.
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect  # Imports HttpResponse (what this HttpResponse do? ), HttpResponseRedirect (what this HttpResponseRedirect do?), and HttpResponseNotFound (what this HttpResponseNotFound do?), which let a Django view send text or HTML back to the browser.  
from django.urls import reverse  # Imports reverse(), which generates a URL from a view name and optional parameters. It is not used in this example.

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
def home(request, name):  # Defines a view named home. Django passes an HttpRequest object into request when this view is called.
    print(reverse('home', args=[name]))  # Generates the URL for the home view using its name and the provided name parameter. This is not used in this example, but it demonstrates how to create URLs dynamically.
    html = ""  # Creates an empty string that will gradually hold the HTML for all the posts.
    for post in posts:  # Loops through the posts list, assigning one dictionary at a time to the variable post.
        # += appends text to html; f allows expressions inside braces; triple quotes allow a string to span multiple lines.
        html += f'''
          <div>
            <a href="/post/{post['id']}/">
            <h1>{post['id']}. {post['title']}</h1>
            </a>
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
    valid_Id = False  # Initializes a boolean variable validId to False. This will track whether a matching post ID is found.
    for post in posts:  # Loops through the posts list, assigning one dictionary at a time to the variable post.
        if post['id'] == id:  # Checks if the current post's ID matches the id parameter passed to the view.
            post_dict = post  # If a match is found, assigns the current post dictionary to post_dict.      
            valid_Id = True  # If a match is found, sets validId to True.
            break  # Exits the loop early since a matching post has been found.
    if valid_Id:  # Checks if validId is True, indicating a matching post ID was found.
            html = f'''
                <div>
                    <h1>{post_dict['id']}. {post_dict['title']}</h1>
                    <p>{post_dict['content']}</p>
                </div>
                '''
            # If a match is found, generates HTML for that specific post using an f-string.
            return HttpResponse(html)  # Sends the generated HTML to the browser.
    else:  # If no matching post ID is found after the loop, executes the following block.
            return HttpResponseNotFound("Post not available \U0001F642")  # Sends an HTTP 404 response to the browser with a message indicating that the post is not available, along with a smiley face emoji.

def google(request):  # Defines a view named google that takes an HttpRequest object  as a parameter and parameter name request.
    return HttpResponseRedirect("https://www.google.com")  # Sends an HTTP response to the browser containing a heading with the text "Google".    

def redirect_to_id(request, id):  # Defines a view named redirect_to_id that takes an HttpRequest object and an integer parameter named id.
    return HttpResponseRedirect(f'/post/{id}/')  # Sends an HTTP response to the browser containing a heading with the text "Google".    
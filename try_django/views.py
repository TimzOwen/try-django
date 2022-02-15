from django.http import HttpResponse

HTML_STRING = """
<h1> This is DJango </h1>
<h1> Welcome to the world of django programming Timz</h1>
"""

def home_view(request):

    """
    takes in a request and returns a response
    """

    return HttpResponse(HTML_STRING)
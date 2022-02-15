from django.http import HttpResponse
import random 



def home_view(request):

    """
    takes in a request and returns a response
    """
    HTML_STRING = """
    <h1> This is DJango </h1>
    <h1> Welcome to the world of django programming Timz</h1>
    """

    name = "Timz"
    win = random.randint(10,1000)

    deatils = f"""<h2> "Hello {name} you just win {win}" </h2>"""



    return HttpResponse(deatils)
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Taking the data to the browser using HttpResponse
    :param request:
    :return: str --> Dummy string that we are sending to the browser
    """
    return HttpResponse("Hi, I am in index page.")


def home(request):
    """
    :param request:
    :return:
    """
    data = {"name": "siva", "age": 30, "nationality": "Indian",
            "education": [{"name": "Nagarjuna", "type": "Schooling", "marks": 86.6, "location": "Kadapa"},
                          {"name": "Narayana", "type": "+2", "marks": 86.1, "location": "Nellore"},
                          {"name": "KORM", "type": "BTech", "marks": 71.6, "location": "Kadapa"}]}
    return render(request, "polls/index.html", data)

from django.shortcuts import render

# Create your views here.

def index(request):
    Values = {
        "text": "hello world",
        "number": 100
    }

    return render(request, "basic_app/index.html", Values)

def other(request):
    return render(request, "basic_app/other.html")

def relative(request):
    return render(request, "basic_app/relative_url_templates.html")

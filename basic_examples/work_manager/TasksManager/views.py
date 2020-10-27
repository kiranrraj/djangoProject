from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    myName = "kiran raj r"
    city = "Trivandrum"
    nationality = "Indian"
    pLang = ["JavaScript", "Python", "C++"]
    return render(request, 'en/public/index.html', {
        "name":myName, 
        "city": city, 
        "nationality": nationality, 
        "pLang" : pLang
        }
    )

def about(request):
    return render(request, "en/public/about.html")


# def home(request):
#     return HttpResponse("Hello world")
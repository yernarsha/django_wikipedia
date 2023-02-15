from django.shortcuts import render, HttpResponse

import wikipedia

# Create your views here.

def index(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            result = wikipedia.summary(search, sentences = 10) # Number of sentences that you want as output
        except Exception as e:
            return HttpResponse(f"Wrong input. {e}")
        return render(request, "wikiapp/index.html", {"result": result})
    
    return render(request, "wikiapp/index.html")

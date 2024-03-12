from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    if request.method == "POST":
        text = request.POST['text']
        amount_of_words = len(text.split())
        context={
            'amount': amount_of_words,
            }
        return render(request, 'counter.html', context)
    else:
        return render(request, "counter.html")
from django.shortcuts import render_to_response, HttpResponse
from books.models import Book


# Create your views here.

def search_form(request):
    return render_to_response("search_form.html")

def search(request):
    if 'q' in request.GET and request.GET['q']:
        print request.GET['q']
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html', {'books':books, 'query': q})

    else:
        print 'abd'
        return render_to_response('search_form.html', {'error':True})

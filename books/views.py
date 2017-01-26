from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.object.filter(title__icontains=q)
        return render(request, 'search_results.html', {'books': books, 'query': q}
    else:
        return HttpResponse("Please submit a search term')
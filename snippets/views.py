from django.shortcuts import render, HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("Here's the first webpage.")
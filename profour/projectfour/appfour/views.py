from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world', 'numbers':100}
    return render(request, 'appfour/index.html', context_dict)

def other(request):
    return render(request, 'appfour/other.html')

def relative (request):
    return render(request, 'appfour/relative_url_templates.html')

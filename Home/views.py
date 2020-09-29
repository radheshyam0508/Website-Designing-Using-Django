from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

    #return HttpResponse ("This is Home Page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse ("This is About Page")



def services(request):
    return render(request, 'services.html')
    #return HttpResponse ("This is Service Page")


def contacts(request):
    return render(request, 'contacts.html')
    #return HttpResponse ("This is Contact Page")


from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    #  Note the key boldmessage is the same as {{ boldmessage }} in the template!
   # #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client. # We make use of the shortcut function to make our lives easier.
    #  Note that the first parameter is the template we wish to use.
    html = "Rango says here is the about page"   + '<br/> <a href="/rango/about/">About</a>'
   # #return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner!" <br/> <a href='/rango/about/'>About</a>)
    return HttpResponse(html)

# View corresponding to the about page
def about(request):
    htmlabout = "Rango says here is the about page" +'<a href="/rango/">Index</a>'
    return HttpResponse(htmlabout)
   #return HttpResponse("Rango says here is the about page")

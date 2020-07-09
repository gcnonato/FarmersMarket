from django.views.generic import TemplateView
import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class HomePage(TemplateView):
    """docstring for HomePage."""
    template_name = 'index.html'

# class TestPage(TemplateView):
#     template_name = 'test.html'
#
# class ThanksPage(TemplateView):
#     template_name = 'thanks.html'

class Register(TemplateView):
    """docstring for Register. """
    template_name = 'register.html'

class ThanksPage(TemplateView):
    """docstring for ThanksPage."""

    template_name = 'thanks.html'
    
    
@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("andylibs.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

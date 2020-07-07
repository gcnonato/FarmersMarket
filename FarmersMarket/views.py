from django.views.generic import TemplateView


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

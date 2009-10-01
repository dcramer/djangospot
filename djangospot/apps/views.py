from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from djangospot.utils.controller import *

from forms import SubmitAppForm
from models import App

class IndexController(Controller):
    def get(self, request):

        apps = App.objects.all()

        context = {
            'apps': apps,
        }

        return self.respond('apps/index.html', context, request)

class SubmitController(Controller):
    login_required = True
    
    def get(self, request):
        form = SubmitAppForm()

        context = {
            'form': form,
        }

        return self.respond('apps/submit.html', context, request)
    
    def post(self, request):
        form = SubmitAppForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.owner = request.user
            app.save()

            return HttpResponseRedirect(reverse('apps.index'))

        context = {
            'form': form,
        }

        return self.respond('apps/submit.html', context, request)

class ViewController(Controller):
    """
    Handling of the viewing of an app.
    """
    def get(self, request, app_id):
        app = App.objects.get(pk=app_id)

        context = {
            'app': app,
        }
        return self.respond('apps/view.html', context, request)
            

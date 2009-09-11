from djangospot.utils.controller import *
from forms import SubmitAppForm

class IndexController(Controller):
    def get(self, request):
        return self.respond('apps/index.html', {}, request)

class SubmitController(Controller):
    def get(self, request):
        form = SubmitAppForm()

        context = {
            'form': form,
        }

        return self.respond('apps/submit.html', context, request)
    
    def post(self, request):
        form = SubmitAppForm(request.POST)
        if form.is_valid():
            pass

        context = {
            'form': form,
        }
        return self.respond('apps/submit.html', context, request)
        

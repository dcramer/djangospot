from djangospot.utils.controller import *
from forms import AppForm

class IndexController(Controller):
    def get(self, request):
        return self.respond('apps/index.html', {}, request)

class SubmitController(Controller):
    def get(self, request):
        return self.respond('apps/submit.html', {}, request)
    
    def post(self, request):
        form = AppForm(request.POST)
        if form.is_valid():
            pass
        return self.respond('apps/submit.html', {}, request)
        
from djangospot.utils.controller import *
from djangospot.snippets.models import Snippet
from djangospot.snippets.forms import SnippetForm

class IndexController(Controller):
    def get(self, request):
        "Display a list of ``Snippet``s"
        
        snippets = Snippet.objects.filter()
        
        return self.respond('snippets/index.html', {'snippets': snippets}, request)
        

class SubmitController(Controller):
    def get(self, request):
        "Display submission form"
        
        form = SnippetForm()
        
        return self.respond('snippets/submit.html', {'form': form}, request)
        
    def post(self, request):
        "Process a submission"
        
        form = SnippetForm(request.POST)

        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            return self.redirect("snippets.index")
        else:
            return self.respond('snippets/submit.html', {'form': form}, request)
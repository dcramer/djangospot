from coffin.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect

class Controller(object):
    login_required = False
    
    def __call__(self, request, *args, **kwargs):
        method = request.method.lower()
        view = getattr(self, method, getattr(self, 'get'))
        if (self.login_required\
          or getattr(view, 'login_required', False))\
          and not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('auth_login'))
        return view(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.page_not_found(request)
    
    def page_not_found(self, request):
        raise Http404
    
    def respond(self, template, context={}, request=None, mimetype="text/html"):
        if request:
            req_context = RequestContext(request)
        else:
            req_context = None
        return render_to_response(template, context, req_context, mimetype)
        
    def redirect(self, redirect_to):
        from django.shortcuts import redirect
        return redirect(redirect_to)
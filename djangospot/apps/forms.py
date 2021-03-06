from django import forms

from models import App

class SubmitAppForm(forms.ModelForm):
    class Meta:
        model = App
        exclude = ('app_id', 'roles', 'owner', 'category_ids', )

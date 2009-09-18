from django import forms
from djangospot.snippets.models import Snippet, LANGUAGE_CHOICES

class SnippetForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea, help_text="ReST formatting is allowed")
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    
    class Meta:
        model = Snippet
        fields = ('title', 'description', 'language', 'raw_code', 'tags')
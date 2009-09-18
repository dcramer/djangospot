from django.contrib import admin
from djangospot.snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "language")
    list_filter = ("language", "date_added", "date_changed")
    search_fields = ("title", "tags")


admin.site.register(Snippet, SnippetAdmin)
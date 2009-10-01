from coffin.contrib.auth.models import User
from django.db import models
from djangoratings.fields import RatingField
from tagging.fields import TagField
from treebeard.mp_tree import MP_Node
from djangospot.utils.fields import *

LANGUAGE_CHOICES = (
    ("python", "Python"),
    ("javascript", "Javascript"),
    ("django", "Django/Jinja Template Code"),
    ("sql", "SQL"),
    ("apacheconf", "Apache Config"))


class Snippet(models.Model):
    """
    Details a snippet of code submitted by a `User`
    """
    snippet_id = UUIDField(auto=True)
    author = models.ForeignKey(User, related_name="snippet_set")
    title = models.CharField(max_length=128)
    slug = AutoSlugField(for_field="title", max_length=128)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=30)
    raw_code = models.TextField(verbose_name=u"Snippet", blank=True, null=True)
    highlighted_code = models.TextField(editable=False)
    tags = TagField()
    rating = RatingField(range=5)
    date_added = CreatedDateTimeField(editable=False)
    date_changed = ModifiedDateTimeField(editable=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name
        from pygments.formatters import HtmlFormatter

        self.highlighted_code = highlight(
            self.raw_code,
            get_lexer_by_name(self.language),
            HtmlFormatter())

        super(Snippet, self).save(*args, **kwargs)

from django import forms
from .models import Chapter


class ChapterCreateForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('title', 'body')

# the same form above
class ChapterEditForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('title', 'body')
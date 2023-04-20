from django import forms

from .models import Post, Team, Comment


class CreateForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=False, widget=forms.Select())
    content = forms.CharField(max_length=140)
    class Meta:
        model = Post
        fields = ['content', 'team', 'title']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

from django import forms
from .models import Post, Community

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','writer','pub_date','body','category','image']

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title','writer','pub_date','body', 'category','image']

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class CommunitySearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
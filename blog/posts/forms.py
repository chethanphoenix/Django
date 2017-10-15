from django import forms
from .models import post

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    article = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ("title", "article_type",  "content", "author", "post_image",)
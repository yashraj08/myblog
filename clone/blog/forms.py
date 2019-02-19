from django import forms
from blog.models import Post,comment

class postform(forms.ModelForm):
    class Meta():
        model= Post
        fields=('author','title','text')
        widgets={
        'title': forms.TextInput(attrs={'class':'textinputclass'}),
        'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class commentform(forms.ModelForm):
    class Meta():
        model= comment
        fields=('author','text')
        widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

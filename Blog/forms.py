from django import forms
from django.forms import ValidationError
from .models import Article,Category, Comment,Profile,Vote
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class CategoryForm(forms.Form):
#     cat_name=forms.CharField(max_length=30)
#     slug=forms.SlugField(max_length=30)

#     def save(self):
#         new_category=Category.objects.create(cat_name=self.cleaned_data['cat_name'],slug=self.cleaned_data['slug'])
#         return new_category


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model=Category
        fields='__all__'

    def clean_cat_name(self):
        return self.cleaned_data['cat_name'].lower()

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug=='create':
            raise ValidationError("Slug cannot be called 'create'")
        else: 
            return new_slug

class ArticleForm(forms.ModelForm):

    class Meta: 
        model=Article
        fields='__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Article Title'
                }),
            'slug': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Slug'
                }),
            'cat': forms.CheckboxSelectMultiple(attrs={
                'class': "form-check",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            
        }

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

# class AuthorForm(forms.ModelForm):

#     class Meta:
#         model=Author
#         fields='__all__'



class CommentForm(forms.ModelForm):

    class Meta: 
        model=Comment
        fields=['text',]
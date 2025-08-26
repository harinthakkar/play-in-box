from django import forms
from ..models import Category

#creating a format
class CategoryForm(forms.ModelForm):
#create meta class
      class Meta:
#specify model to be used
           model=Category
#specify fields to be used
           fields=[
       "title",
       "description",
        ]











from django.forms import ModelForm
from .models import *
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image' ,'description','demo_link','source_link','tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm , self).__init__(*args, **kwargs)
        
        # self.fields['title'].widget.attrs.update({'class':'input' , 'placeholder':"Enter the title of the project"})
        # self.fields['description'].widget.attrs.update({'class':'input' , 'placeholder':"Enter the description of the project"})

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input' , 'placeholder':"Enter the "})
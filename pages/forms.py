from django.forms import ModelForm
from .models import *
from django import forms
from project.models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name' , 'email' , 'username' , 'short_intro' , 'location' , 'bio' , 'profile_image' , 'social_github' , 'social_twitter' , 'social_linkedin' , 'social_youtube' , 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name' , 'description']


    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email' , 'subject', 'body']

    def __init__(self,*args,**kwargs):
        super(MessageForm , self).__init__(*args,**kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})
from django import forms
from app.models import *


class Topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic_name']

class Webpageform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','email','url']


class Accessrecordform(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields=['author','date']
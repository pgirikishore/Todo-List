#-*- coding: utf-8 -*-
from django import forms

class Form(forms.Form):
   item = forms.CharField(max_length = 100)
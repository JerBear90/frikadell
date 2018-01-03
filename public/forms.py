# -*- coding: utf8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class FeedbackForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Title')}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('First name')}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Last name')}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('Email')}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Comment')}))


class FranchiseForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Title')}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('First name')}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Last name')}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('Email')}))
    # company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Company Name')}))
    # website = forms.URLField(widget=forms.URLInput(attrs={'placeholder': _('Company Website')}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Telephone Number')}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Franchise location interest')}))
    ideas = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Don’t forget to tell us how you plan to make a positive contribution towards the Frikadell family!')}))

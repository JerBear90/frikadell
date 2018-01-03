# -*- coding: utf8 -*-
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls.base import reverse
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

from frikadell import settings
from public.forms import FeedbackForm, FranchiseForm


def robots(request):
    return render(request, 'public/robots.txt', content_type='text/plain')


def sitemap(request):
    return render(request, 'public/sitemap.xml', content_type='application/xml; charset=utf-8')


def index(request):
    return redirect(reverse('public:home'))


def home(request):
    return render(request, 'public/home.html', {'page_name': 'home'})


def locations(request):
    return render(request, 'public/locations.html', {'page_name': 'locations'})


def menu(request):
    return render(request, 'public/menu.html', {'page_name': 'menu'})


def contact(request):
    contact_errors = ''
    if request.method == 'POST' and 'feedback' in request.GET:
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            html_content = render_to_string('public/mail/feedback.html',
                                            feedback_form.cleaned_data)  # ...
            text_content = strip_tags(html_content)  # this strips the html, so people will have the text as well.
            send_mail(feedback_form.cleaned_data['title'], text_content, feedback_form.cleaned_data['email'],
                      settings.FORWARD_MESSAGES['feedback'],
                      html_message=html_content)
        contact_errors = feedback_form.errors
    else:
        feedback_form = FeedbackForm()

    if request.method == 'POST' and 'franchise' in request.GET:
        franchise_form = FranchiseForm(request.POST)
        if franchise_form.is_valid():
            html_content = render_to_string('public/mail/franchise.html',
                                            franchise_form.cleaned_data)
            text_content = strip_tags(html_content)  # this strips the html, so people will have the text as well.
            send_mail(franchise_form.cleaned_data['title'], text_content, franchise_form.cleaned_data['email'],
                      settings.FORWARD_MESSAGES['franchise'],
                      html_message=html_content)
        contact_errors = franchise_form.errors
    else:
        franchise_form = FranchiseForm()

    return render(request, 'public/contact-us.html',
                  {'page_name': 'contact', 'feedback_form': feedback_form, 'franchise_form': franchise_form,
                   'errors': contact_errors})


def fans(request):
    return render(request, 'public/fans.html', {'page_name': 'fans'})


def careers(request):
    return render(request, 'public/careers.html', {'page_name': 'careers'})


def privacy_policy(request):
    return render(request, 'public/privacy-policy.html', {'page_name': 'privacy-policy'})


def franchise(request):
    return render(request, 'public/franchise.html', {'page_name': 'franchise', 'franchise_form': FranchiseForm()})


def press(request):
    return render(request, 'public/press.html', {'page_name': 'press'})


def story(request):
    return render(request, 'public/story.html', {'page_name': 'story'})


def speak_frikadell(request):
    return render(request, 'public/speak-frikadell.html', {'page_name': 'speak-frikadell'})

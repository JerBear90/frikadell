from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from public import views

app_name = 'public'

public_site_patterns = [
    url(_(r'^$'), views.index, name='index'),
    url(_(r'^home/$'), views.home, name='home'),
    url(_(r'^locations/$'), views.locations, name='locations'),
    url(_(r'^menu/$'), views.menu, name='menu'),
    url(_(r'^contact-us/$'), views.contact, name='contact'),
    url(_(r'^frikadell-freaks/$'), views.fans, name='fans'),
    url(_(r'^join-the-team/$'), views.careers, name='careers'),
    url(_(r'^privacy-policy/$'), views.privacy_policy, name='privacy-policy'),
    url(_(r'^franchise/$'), views.franchise, name='franchise'),
    url(_(r'^press/$'), views.press, name='press'),
    url(_(r'^our-story/$'), views.story, name='story'),
    url(_(r'^do-you-speak-frikadell/$'), views.speak_frikadell, name='speak-frikadell'),
]

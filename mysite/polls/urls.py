
from django.conf.urls import url

from . import views

# The url() function is passed four arguments, two required: regex and view, 
# and two optional: kwargs, and name.
"""
Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the
requested page, or raising an exception such as Http404. The rest is up to you.
"""

# add namespace to urlconf to differentiate from other apps
app_name = 'polls'
# map views to a urlconf (using generic views)
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # DetailView generic view expects the primary key value captured from the URL to be called "pk" to pass to view
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


"""
When somebody requests a page from your website – say, “/polls/34/vote”, Django will load the mysite.urls Python module
because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the
regular expressions in order. After finding the match at '^polls/', it strips off the matching text ("polls/")
and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing.
There it matches r'^(?P<question_id>[0-9]+)/$', resulting in a call to the vote() view

Using parentheses around a pattern “captures” the text matched by that pattern and sends it as an argument to the
view function; ?P<question_id> defines the name that will be used to identify the matched pattern; and [0-9]+ is
a regular expression to match a sequence of digits (i.e., a number).
"""


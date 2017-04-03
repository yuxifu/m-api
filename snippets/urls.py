from django.conf.urls import url, include
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views0
from snippets import views1
from snippets import views2
from snippets import views3
from snippets import views4
from snippets import views

# API endpoints
urlpatterns = [
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^snippets/users/$',
        views.UserList.as_view(),
        name='snippets-user-list'),
    url(r'^snippets/users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='snippets-user-detail')
]

# different ways to create API
if settings.DEBUG:
    urlpatterns += [
        url(r'^exp_snippets0/$', views0.snippet_list),
        url(r'^exp_snippets0/(?P<pk>[0-9]+)/$', views0.snippet_detail),
        url(r'^exp_snippets1/$', views1.snippet_list),
        url(r'^exp_snippets1/(?P<pk>[0-9]+)/$', views1.snippet_detail),
        url(r'^exp_snippets2/$', views2.SnippetList.as_view()),
        url(r'^exp_snippets2/(?P<pk>[0-9]+)/$',
            views2.SnippetDetail.as_view()),
        url(r'^exp_snippets3/$', views3.SnippetList.as_view()),
        url(r'^exp_snippets3/(?P<pk>[0-9]+)/$',
            views3.SnippetDetail.as_view()),
        url(r'^exp_snippets4/$', views4.SnippetList.as_view()),
        url(r'^exp_snippets4/(?P<pk>[0-9]+)/$',
            views4.SnippetDetail.as_view()),
    ]


# support optional format suffixes
# urlpatterns = format_suffix_patterns(urlpatterns)

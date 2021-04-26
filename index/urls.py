from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01-test/$',test_views),
    url(r'01-tmp/?',tmp_views),
    url(r'03-var',var_views),
    url(r"04-add/$",add_views),
    url(r'05-query',query_views),
    url(r'06-authors',authors_views),
    url(r'07-wife',wife_views),
    url(r'08-mtm',mtm_views),
    url(r'09-request',request_views),
    url(r'04-form/$',form_views),
    url(r'10-setcookie',cookie_views),
    url(r'11-session/$',session_views),
    url(r"12-celery",celeryTest),
]

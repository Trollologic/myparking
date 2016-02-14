from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.feedback_list, name='feedback_list'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^$',views.post_new, name='post_new'),

]
from django.conf.urls import url
from django.urls import path
from .views import listAll, ratingAll, averageRating, rate, register, Login, Logout

urlpatterns = [
    path('listAll/', listAll, name="listAll"),
    path('ratingAll/',ratingAll, name='ratingAll'),
    url(r'averageRating/p(?P<p>\w+)m(?P<m>\w+)/$', averageRating, name='averageRating'),
    url(r'rate/p(?P<p>\w+)m(?P<m>\w+)y(?P<y>\d+)s(?P<s>\d+)r(?P<r>\d+\.\d+|\d+)/$', rate, name='rate'),
    path('register/', register, name = 'register'),
    path('login/', Login, name = 'login'),
    path('logout/', Logout, name = 'logout'),
    ]
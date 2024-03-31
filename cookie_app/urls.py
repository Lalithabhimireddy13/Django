from django.urls import path
from cookie_app import views

urlpatterns=[
    path('set_cookie/',views.set_cookie, name='set_cookie'),
    path('get_cookie/',views.get_cookie, name='get_cookie')
]

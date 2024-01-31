from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_view),
    path('java',views.java_view),
    path('python',views.python_view),
    path('csharp',views.csharp_view),
    path('logout',views.logout_view),
    path('signup',views.signup_view)
]
from django.urls import path
from . import views   # user/views 불러오기

urlpatterns = [
    path('sign/', views.sign_up_view, name='signup'),
]
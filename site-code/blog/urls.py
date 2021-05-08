from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), #home page boi :)
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # the <> thingy is to capture slugs(ASCII values) 
      
]
from django.urls import path

from . import views

app_name= "quotes"

urlpatterns = [
    path('', views.main, name = "root"),
    path('<int:page>', views.main, name = "root_paginate"),
    path('detail/<int:quote_id>', views.detail, name='detail'),
    path('tags/<int:tag_id>', views.tags, name='tags'),
    path('addtag/', views.addtag, name='addtag'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('addquote/', views.addquote, name='addquote'),
]
 
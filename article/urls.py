from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name = 'article.create'),
    #path('read', views.read, name = 'article.read'),
    path('update/<int:id>', views.update, name = 'article.update'),
    path('delete/<int:id>', views.delete, name = 'article.delete'),

]
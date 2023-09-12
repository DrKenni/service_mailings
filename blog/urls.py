from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    switch_publication

app_name = BlogConfig.name

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('', ArticleListView.as_view(), name='list'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('publication/<int:pk>/', switch_publication, name='switch_publication'),
]


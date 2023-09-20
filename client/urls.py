from django.urls import path

from client.apps import ClientConfig
from client.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = ClientConfig.name

urlpatterns = [
    path('client/list/', ClientListView.as_view(), name='list'),
    path('client/create/', ClientCreateView.as_view(), name='create'),
    path('client/view/<int:pk>', ClientDetailView.as_view(), name='view'),
    path('client/edit/<int:pk>', ClientUpdateView.as_view(), name='edit'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='delete'),
]

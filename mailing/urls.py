from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDeleteView, MailingCreateView, MailingUpdateView, MailingDetailView, \
    MailingView, contacts

app_name = MailingConfig.name

urlpatterns = [
    path('', cache_page(60)(MailingView.as_view()), name='mailing_main'),
    path('contacts/', contacts, name='contacts'),
    path('list/', MailingListView.as_view(), name='list_mailing'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('edit/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('view/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    # path('view/filter/', MailingDetailView.as_view(), name='view_mailing'),
]

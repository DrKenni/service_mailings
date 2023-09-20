from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDeleteView, MailingCreateView, MailingUpdateView, MailingDetailView, \
    MailingView, contacts, MessageListView, MessageCreateView, MessageDeleteView, MessageUpdateView, MessageDetailView

app_name = MailingConfig.name

urlpatterns = [

    path('', cache_page(60)(MailingView.as_view()), name='mailing_main'),
    path('contacts/', contacts, name='contacts'),

    # Mailing
    path('list/', MailingListView.as_view(), name='list_mailing'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('edit/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('view/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    # path('view/filter/', MailingDetailView.as_view(), name='view_mailing'),

    # Message
    path('message/list/', MessageListView.as_view(), name='list_message'),
    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),
    path('message/edit/<int:pk>', MessageUpdateView.as_view(), name='update_message'),
    path('message/view/<int:pk>', MessageDetailView.as_view(), name='view_message'),
]

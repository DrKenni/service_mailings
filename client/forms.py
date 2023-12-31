from django import forms

from client.models import Client
from mailing.forms import StyleFormMixin


class ClientForms(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'surname', 'comment', 'contact_email')

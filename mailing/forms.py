from django import forms

from client.models import Client
from config import settings
from mailing.models import Mailing, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['message'] = 'Не выбрано'

    class Meta:
        model = Mailing
        fields = ('frequency', 'status', 'message', 'client')
        # fields = '__all__'


class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = ('title', 'body')
        # fields = '__all__'

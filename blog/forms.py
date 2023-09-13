from django import forms

from blog.models import Article
from mailing.forms import StyleFormMixin


class ArticleForm(StyleFormMixin, forms.ModelForm):

    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Article
        fields = ('title', 'content', 'preview',)

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В названии есть запрещенные слова!')
        return cleaned_data

    def clean_content(self):
        cleaned_data = self.cleaned_data['content']
        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В описании есть запрещенные слова!')
        return cleaned_data

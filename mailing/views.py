from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import Article
from client.models import Client
from mailing.forms import MailingForm
from mailing.models import Mailing


class MailingView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_main.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing'] = len(Mailing.objects.all())
        context_data['active_mailing'] = len(Mailing.objects.filter(status=2))
        context_data['title'] = 'Главная'
        context_data['clients'] = len(Client.objects.all().distinct('email'))
        context_data['article'] = Article.objects.filter(is_published=True)[:3]
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=2)
        return queryset


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Список рассылок',
    }


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing/mailing_list.html')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing/mailing_list.html')

    def form_valid(self, form):
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing/mailing_list.html')


@login_required
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}: {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'mailing/contacts.html', context)
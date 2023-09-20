from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article
from client.models import Client
from mailing.cron import my_scheduled_job
from mailing.forms import MailingForm, MessageForm
from mailing.models import Mailing, Message
from mailing.services import get_log_list


class MailingView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailing/mailing_main.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing'] = len(Mailing.objects.all())
        context_data['active_mailing'] = len(Mailing.objects.filter(status=2))
        context_data['title'] = 'Главная'
        context_data['clients'] = len(Client.objects.all())
        context_data['article'] = Article.objects.filter(is_published=True).order_by('?')[:3]
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=2)
        return queryset


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    extra_context = {
        'title': 'Список рассылок',
    }


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['logs'] = get_log_list(self.object.pk)
        return context_data


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    # permission_required = 'mailing.delete_mailing'
    success_url = reverse_lazy('mailing:list_mailing')


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list_mailing')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        my_scheduled_job()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['message'].queryset = Message.objects.filter(user=self.request.user)
        context['form'].fields['client'].queryset = Client.objects.filter(user=self.request.user)
        return context


class MailingUpdateView(LoginRequiredMixin, UpdateView):
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


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mailing/message_list.html'
    extra_context = {
        'title': 'Список сообщений',
    }


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:list_message')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:list_message')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:list_message')


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

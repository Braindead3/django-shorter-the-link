from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Url
from .utils import generate_short_url


class UrlListView(LoginRequiredMixin, ListView):
    model = Url
    template_name = 'link/home.html'

    def get_queryset(self):
        return Url.objects.filter(user=self.request.user)


class UrlCreateView(CreateView):
    model = Url
    fields = ['url']
    template_name = 'link/create_short_url.html'
    success_url = reverse_lazy('home')
    success_message = 'Your successfully create short url!'

    def form_valid(self, form):
        if Url.objects.get(url=form.cleaned_data.get('url')):
            return redirect('home')
        form.instance.short_url = generate_short_url()
        form.instance.user = self.request.user
        return super().form_valid(form)


class UrlRedirectView(View):
    def get(self, request, *args, **kwargs):
        url = Url.objects.get(short_url=kwargs.get('url'))
        return redirect(url.url)

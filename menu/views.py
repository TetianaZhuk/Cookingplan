from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import datetime

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin, DeleteView

from ingredients.models import Ingredient

from menu.forms import DateForm, BreakfastForm, LaunchForm, DinnerForm
from menu.models import Day


def index(request):
    template_name = 'index.html'
    context = {'title': 'Главная'}
    return render(request, template_name, context)


class DayListView(ListView):
    model = Day
    template_name = 'menu/list.html'
    context_object_name = 'days'


class DayCreateView(CreateView, FormMixin):
    model = Day
    fields = '__all__'
    template_name = 'menu/create.html'
    context_object_name = 'days'
    success_url = 'menu:list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DateForm()
        return context

    def post(self, request, *args, **kwargs):
        form = DateForm(self.request.POST)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        start = form.cleaned_data['start']
        end = form.cleaned_data['end']
        while start <= end:
            try:
                Day.objects.get(date=start, author=self.request.user)
            except Day.DoesNotExist:
                Day.objects.create(date=start, author=self.request.user)
            start += datetime.timedelta(days=1)
        return redirect("menu:list")


class LaunchCreateView(LoginRequiredMixin, CreateView):
    model = Day
    template_name = 'menu/create_day.html'
    form_class = LaunchForm
    success_url = reverse_lazy('menu:list')


class DinnerCreateView(CreateView):
    model = Day
    template_name = 'menu/create_day.html'
    form_class = DinnerForm
    success_url = reverse_lazy('menu:list')


class BreakfastCreateView(CreateView):
    model = Day
    template_name = 'menu/create_day.html'
    form_class = BreakfastForm
    success_url = reverse_lazy('menu:list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        day = Day.objects.get(slug=kwargs['slug'])
        day.breakfast = form.cleaned_data['breakfast']
        day.save()
        return redirect("menu:list")


class LaunchCreateView(CreateView):
    model = Day
    template_name = 'menu/create_day.html'
    form_class = LaunchForm
    success_url = reverse_lazy('menu:list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        day = Day.objects.get(slug=kwargs['slug'])
        day.launch = form.cleaned_data['launch']
        day.save()
        return redirect("menu:list")


class DinnerCreateView(CreateView):
    model = Day
    template_name = 'menu/create_day.html'
    form_class = DinnerForm
    success_url = reverse_lazy('menu:list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        day = Day.objects.get(slug=kwargs['slug'])
        day.dinner = form.cleaned_data['dinner']
        day.save()
        return redirect('menu:list')


class DayDeleteView(DeleteView):
    model = Day
    template_name = 'menu/list.html'
    success_url = reverse_lazy('menu:list')


class ShoppingListView(ListView):
    model = Ingredient
    template_name = 'menu/list.html'
    context_object_name = 'shopping_list'

from django.shortcuts import render, redirect
from cofe.models import Res, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CategoryForm
from django.contrib import messages

# Create your views here.


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_of_reserves(request):
    reserver = Res.objects.filter(timi_proc=False).order_by('date_reg')
    paginator = Paginator(reserver, 2)
    page = request.GET.get('page')
    reserver = paginator.get_page(page)
    return render(request, 'reserves.html', context={'reserves': reserver})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reserve(request, pk):
    Res.objects.filter(pk=pk).update(timi_proc=True)
    return redirect('/manager/reserve')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_of_categories(request):
    items = Category.objects.all().order_by('cat_order')
    return  render(request, 'categories.html', context={'categories': items})


class CategoryAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager']
    model = Category
    success_url = reverse_lazy('list_of_categories')
    succsess_message = 'Успешно дбавлена!'
    form_class = CategoryForm
    template_name = 'category_add.html'

class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager']
    model = Category
    success_url = reverse_lazy('list_of_categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена!')
        return  self.post(request, *args, **kwargs)



class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager']
    model = Category
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Успешно обновлена!'
    form_class = CategoryForm
    template_name = 'category_update.html'
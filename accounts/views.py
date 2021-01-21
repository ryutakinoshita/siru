from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView
from .forms import UserCreateForm, UserChangeForm
from .models import User


class UserChangeTextView(TemplateView):
    template_name = 'account/user_change_page.html'

#ユーザ登録用View
def signup(request):
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreateForm
    return render(request,'account/user.html',{'form':form})


#ユーザー情報変更View
class UserChangeView(LoginRequiredMixin,FormView):
    template_name = 'account/user_text_change.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'username': self.request.user.username,
            'profile': self.request.user.profile,
        })
        return kwargs


class MyPageView(LoginRequiredMixin,DetailView):
    template_name = 'account/user_my_page.html'
    model = User
    slug_field = 'username','profile'
    slug_url_kwarg = 'username','profile'


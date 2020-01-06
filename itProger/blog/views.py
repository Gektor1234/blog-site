from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Posts



def home(request):
    data = {
        "news": Posts.objects.all(),
        "title":'Главная страница блога'
    }
    return render(request, 'blog/home.html',data)

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.avtor:
            return True
        return False

class ShowNewsView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = "news"
    ordering = ['-date']
    paginate_by = 5


    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница блога'
        return ctx

class UserAllNewsView(ListView):
    model = Posts
    template_name = 'blog/user_posts.html'
    context_object_name = "news"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(avtor=user).order_by('-date')


    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)
        ctx['title'] = f"Все посты от пользователя {self.kwargs.get('username')}"
        return ctx

class NewsDetailView(DetailView):
    model = Posts

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = Posts.objects.filter(pk=self.kwargs['pk']).first()
        return ctx

class CreateNewsView(LoginRequiredMixin,CreateView):
    model = Posts
    fields = ["title", "text"]

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ["title", "text"]

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.avtor:
            return True
        return False



def contacti(request):
    return render(request, 'blog/contacti.html',{'title':'страница про нас'})

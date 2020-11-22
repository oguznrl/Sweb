from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Vpost
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy 
from .forms import PostForm

def ihome(request):
    argv={
        'posts':Vpost.objects.all()
    }    
    return render(request,'vpost/vpost_home.html',argv)

class PostListView(ListView):
    model=Vpost
    template_name='vpost/vpost_home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=4

class PostDetailView(DetailView):
    model=Vpost
    template_name='vpost/vpost_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Vpost
    fields=['text','cover']
    template_name = 'vpost_form.html'
    success_url = '/'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Vpost
    fields=['text','cover']
    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Vpost
    success_url='/'
    template_name='vpost/vpost_confirm_delete.html'
    
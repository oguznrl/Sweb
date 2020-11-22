from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUptadeForm,ProfileUptadeForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
       u_form=UserUptadeForm(request.POST,instance=request.user)
       p_form=ProfileUptadeForm(request.POST , request.FILES , instance=request.user.profile)
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, f'Your account has been uptade! You can login.')
           return redirect('profile')
    
    else:
        u_form=UserUptadeForm(instance=request.user)
        p_form=ProfileUptadeForm(instance=request.user.profile)
    
    argv={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',argv)
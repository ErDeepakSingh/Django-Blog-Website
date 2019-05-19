from django.shortcuts import render,redirect
from  . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required




def register(request):
    form=forms.Sign_Up_Form()
    if request.method=='POST':
        form=forms.Sign_Up_Form(data=request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'Your account has been created! as  { username } you can now Login')
            return redirect('login')
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form=forms.UserUpdateForm(request.POST,instance=request.user)
        p_form=forms.ProfileUpdateForm(data=request.POST,files=request.FILES,
                                       instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your profile has been updated !')
            return redirect('profile')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)
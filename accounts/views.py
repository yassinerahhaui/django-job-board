from django.shortcuts import render,redirect
from .forms import SignupUserForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('accounts:profile')

    else:
        form = SignupUserForm()

    context = {
        'form': form,
    }
    return render(request,'registration/signup.html',context)

#####################################################################
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile':profile,
    }
    return render(request,'accounts/profile.html',context)

#####################################################################
@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('accounts:profile')
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    context = {
        'userform': userform,
        'profileform': profileform,
    }
    return render(request,'accounts/profile_edit.html',context)
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect



def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('new_avaliacao')
    else:
        user_form = UserCreationForm(request.POST)
    return render(request,
                  'register.html',
                  {'user_form':user_form})

def login_view(request):
    form= AuthenticationForm()
    return render(request, 
                  'login.html',
                  {'form':form})
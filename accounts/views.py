from django.shortcuts import render, redirect
from django.contrib.auth.models import User #User object
from django.contrib import auth
from store.models import Customer

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']: #access form information by passing request.POST[form_field]
            if '@' in request.POST['email']:
                try:
                    user = User.objects.get(username=request.POST['username']) #query through the User objects to see if there is already a username that matches the entered username
                    return render(request, 'accounts/signup.html', {'error':'Username has already been taken'}) #pass error message to be rendered to the template
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    email = request.POST['email']
                    name = request.POST['name']
                    customer, created = Customer.objects.get_or_create(user = user, email = email, name = name)
                    auth.login(request,user)
                    return redirect('store')
            else:
                return render(request, 'accounts/signup.html', {'error':'Please enter a valid email'})
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('store')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('store')
    return redirect('store')

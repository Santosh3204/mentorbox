from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages

from home.models import Accounts

# Create your views here.




def home(request):
    return render(request, 'home.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method == "POST":
        user = Accounts()

        user.image = request.POST['image']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.age = request.POST['age']
        user.unique_id = request.POST['unique_id']
        user.email_id = request.POST['email_id']
        user.password = request.POST['password']
        conform_password = request.POST['conform_password']

        user.save()


        if user.password == conform_password:
            if User.objects.filter(username=user.email_id).exists():
                messages.info(request, "Username already exits")
                return redirect('signup_page')
            elif User.objects.filter(email=user.email_id).exists():
                messages.info(request, "Email already exits")
                return redirect('signup_page')
            else:
                user = User.objects.create_user(username = user.email_id, password = user.password, email= user.email_id)
                user.save()
                messages.info(request, "Registered successfully")
                return redirect('login')
                
                
        else:
            print("User paswword unmatched")
            messages.info(request, "Password not matched")
            return redirect('signup_page')
        return redirect('user_home_page')
    else:
        return render(request, 'signup.html')


def user_home_page(request, id):
    user = Accounts.objects.get(pk= id)

    return render(request, 'profile.html', {'user': user})



def login(request):
    if request.method == "POST":
        email = request.POST['email_id']
        password = request.POST['password']

        user = auth.authenticate(email= email, password= password)

        if user is not None:
            auth.login(request, user)
            
            return redirect('user_home_page')


        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return redirect('login')






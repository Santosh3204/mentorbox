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
        
        email_id = request.POST['email_id']
        password = request.POST['password']
        conform_password = request.POST['conform_password']

        


        if password == conform_password:
            if User.objects.filter(username=email_id).exists():
                messages.info(request, "Username already exits")
                return redirect('signup_page')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request, "Email already exits")
                return redirect('signup_page')
            else:
                current_user = User.objects.create_user(username = email_id, password = password, email= email_id)
                current_user.save()
                user.email_id = email_id
                user.password = password
                user.save()
                messages.info(request, "Registered successfully")
                return render(request, 'login.html')
                
                
        else:
            print("User paswword unmatched")
            messages.info(request, "Password not matched")
            return redirect('signup_page')
    else:
        return render(request, 'signup.html')


def user_home_page(request, id):
    user = Accounts.objects.get(pk= id)

    if user.degree == None and user.user_name == None and user.college_name == None and user.passout_year == None and user.course == None and user.school_name == None and user.age == None:
        return render(request, 'incomplete_profile.html', {'user': user})

    return render(request, 'profile.html', {'user': user})

def update(request, id):
    if request.method == "POST":
        user = Accounts.objects.get(pk= id)
        
        user.user_name = request.POST['username']
        user.college_name = request.POST['college_name']
        user.degree = request.POST['degree']
        user.passout_year = request.POST['passout_year']
        user.course = request.POST['course']
        user.school_name = request.POST['school_name']
        user.age = request.POST['age']

        user.save()

    return render(request, 'profile.html', {'user': user})

def login(request):
    if request.method == "POST":
        email = request.POST['email_id']
        password = request.POST['password']

        user = auth.authenticate(username= email, password= password)

        if user is not None:
            auth.login(request, user)
            
            current_user = Accounts.objects.get(email_id= email)

            return redirect('user_home_page', id= current_user.id)
            


        else:
            messages.info(request, "Invalid credentials")
            return redirect('login_page')

    return redirect('login')

def logout_user(request):
    logout(request)
    return render(request, 'logout.html')





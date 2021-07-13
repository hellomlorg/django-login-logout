from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

# view for rendering homepage


def home(request):
    return render(request, "account/home.html")

# view for rendering signup page


def signup(request):
    return render(request, "account/signup.html")


# view for rendering login page
def login(request):
    return render(request, "account/login.html")

# view for rendering data coming from signup page


def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['uname'])
                messages.error(
                    request, " Username already taken, Try something else!!!")
                return redirect("/signup")
            except User.DoesNotExist:
                if len(uname) > 15:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("/signup")

                if not uname.isalnum():
                    messages.error(
                        request, " Username should only contain letters and numbers, Please try again")
                    return redirect("/signup")

                if password1 != password2:
                    messages.error(
                        request, " Password do not match, Please try again")
                    return redirect("/signup")

        # create the user
        user = User.objects.create_user(uname, email, password1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(
            request, " Your account has been successfully created")
        return redirect("/")

    else:
        return HttpResponse('404 - NOT FOUND ')


# view for rendering data from login page
def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters
        name = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)

        # cheching for valid login
        if user is not None:
            dj_login(request, user)
            messages.success(request, " Successfully logged in")
            return redirect("/")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
            return redirect("/")
    return HttpResponse('404 - NOT FOUND ')

# view for rendering logout


def handlelogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('/')

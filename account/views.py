from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Global variable
authenticated = False
# view for rendering homepage


def home(request):
    return render(request, "account/home.html")


# view for rendering signup page


def signup(request):
    if authenticated:
        return render(request, "account/home.html")
    return render(request, "account/signup.html")


# view for rendering login page
def login(request):
    if authenticated:
        return render(request, "account/home.html")
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
            global authenticated
            authenticated = True
            return redirect("/")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
            return redirect("/")
    return HttpResponse('404 - NOT FOUND ')


# view for rendering logout
@login_required
def handlelogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    global authenticated
    authenticated = False
    return redirect('/')


# view for rendering change password
class ChangePassword(LoginRequiredMixin, TemplateView):
    template_name = "account/passwordchange.html"

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=request.user)
            messages.success(request, "Changed Password successfully")
            return redirect('/')
        else:
            for err in form.errors.values():
                messages.error(request, err)
            return redirect('/changepass')

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, self.template_name, {"form": form})

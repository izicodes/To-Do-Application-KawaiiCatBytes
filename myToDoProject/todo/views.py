from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# The authenticate function is used to log out a user
from django.contrib.auth import logout

# The authenticate function is used to verify the user's credentials, and the login function is used to log the user in.
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def about(request):
    return render(request, 'todo/about.html')

def contact(request):
    return render(request, 'todo/contact.html')

# The Signing Up, Logging In and Out Section

def signup(request):
    # When the form is a POST FORM
    if request.method == 'POST':

        # the name in POST['usernames'] is whatever you have the name attribute in the input as.
        username = request.POST['usernameSignUpBox']
        password = request.POST['passwordSignUpBox']

        # This line creates a new User object using Django's built-in authentication system.
        User.objects.create_user(username=username, password=password)

        #  If the user registration is successful, the view redirects the user to the login page. 
        # The redirect() function takes a URL pattern name (e.g., 'login') as an argument: the name part of 'path('login/', views.login, name='login')'
        return redirect('login')
    
    #  If the request method is not POST
    else:
        #In this case, the view renders the signup.html template using the render() function. 
        # The render() function takes the request object and the name of the template as arguments.
        # Returns an HTTP response with the rendered template.
        return render(request, 'todo/signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['usernameLoginBox']
        password = request.POST['passwordLoginBox']

        # This line uses the authenticate function provided by Django's authentication module to verify the user's credentials. 
        # It takes the request object and the username and password as arguments. 
        # The function returns a User object if the credentials are valid, or None otherwise.
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # This line logs in the authenticated user using the login function from Django's authentication module. 
            # It takes the request object and the User object as arguments, establishing the user's session.
            login(request, user)
            
            # If the user is successfully authenticated, this line redirects them to the 'home' URL pattern. 
            return redirect('home')
        
        # If the user's credentials are invalid
        else:
            # This line creates an error message to display to the user.
            error_message = 'Invalid username or password'

            # This line renders the 'login.html' template and includes the error_message variable in the template context. 
            # This allows you to display the error message to the user, notifying them of the invalid credentials.
            return render(request, 'todo/login.html', {'error_message': error_message})
    else:
        # In this case, the view simply renders the 'login.html' template, 
        # allowing the user to see and fill in the login form.
        return render(request, 'todo/login.html')


@login_required # This just means that the user has to login to view this page
# Remember to add 'LOGIN_URL = '[the login page name]' to your settings as a redirect
def profile_page(request):
    return render(request, 'todo/profile.html')

def log_out(request):
    logout(request)
    return redirect('login')
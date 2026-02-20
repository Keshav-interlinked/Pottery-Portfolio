from django.shortcuts import redirect, render
from .models import LoginData,Img_data,SignupData

# Create your views here.
def index(request):
    posts = Img_data.objects.all()
   
    return render(request, 'index.html', {'posts': posts})
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Add your authentication logic here
        # For now, we'll just render the login page again   

        # Save to database
        LoginData.objects.create(
            username=username,password=password)
        return redirect('index2')
    return render(request, 'login.html')


def index2(request):

    posts = Img_data.objects.all()
   
    return render(request, 'index2.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        dob = request.POST['dob']
        # Add your authentication logic here
        # For now, we'll just render the login page again   

        # Save to database
        SignupData.objects.create(
            username=username,email=email,password=password,gender=gender,dob=dob)
        return redirect('index2')
    return render(request, 'signup.html')

def signout(request):
    return redirect('index')



from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def register_page(request):

  if request.method == "POST":
    data = request.POST
    first_name = data.get('firstname')
    last_name = data.get('lastname')
    username = data.get('username')
    password = data.get('password')
    confirmpassword = data.get('confirmpassword')
    email = data.get('email')

    if password != confirmpassword:
      messages.info(request,'invalid password')
      return redirect('/register/')

    user = User.objects.filter(username = username)
    if(user.exists()):
      messages.info(request,'Username is already taken')
      return redirect('/register/')

    user = User.objects.filter(email = email)
    if(user.exists()):
      messages.info(request,'email should be unique')
      return redirect('/register/')

    user = User(
      first_name = first_name,
      last_name = last_name,
      username = username,
      password = password,
      email=email,
    )

    user.set_password(password)
    user.save()
    messages.info(request,'account created successfully')
    return redirect('/login/')

  return render(request,'register.html')

def login_page(request):

  if request.method == "POST":
    data = request.POST
    username = data.get('username')
    password = data.get('password')

    user = User.objects.filter(username = username)

    if not user.exists():
      messages.info(request,'invalid username')
      return redirect('/login/')

    user = authenticate(username = username , password = password)

    if user is None:
      messages.info(request,'invalid password')
      return redirect('/login/')

    else:
      login(request,user)
      return redirect('homePage')
  
  return render(request,'login.html')

def logout_page(request):
  logout(request)
  return redirect('homePage')
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from . models import Record

def home (request):
    """ Home Page """
    return render (request, 'webapp/index.html')

def register (request):
    """ Register a new user """
    form = CreateUserForm() # empty form (method == 'GET')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully.')
            return redirect ('my-login')
    context = {'form': form}
    template_name = 'webapp/register.html'
    return render (request, template_name, context)

def my_login (request):
    """ Login a user """
    form = LoginForm() # empty form (method == 'GET')
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect ('dashboard')
    context = {'form': form}
    template_name = 'webapp/my-login.html'
    return render (request, template_name, context)

def user_logout (request):
    """ Logout a user """
    auth.logout(request)
    messages.success(request, 'Logged out.')
    return redirect ('my-login')

@login_required(login_url='my-login')
def dashboard (request):
    """ Display the existing records """
    records = Record.objects.all()
    context = {'records': records}
    template_name = 'webapp/dashboard.html'
    return render (request, template_name, context)

@login_required(login_url='my-login')
def create_record (request):
    """ Create a new record """
    form = CreateRecordForm() # empty form (method == 'GET')
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully.')
            return redirect ('dashboard')
    context = {'form': form}
    template_name = 'webapp/create-record.html'
    return render (request, template_name, context)

@login_required(login_url='my-login')
def update_record (request, id):
    """ Update an existing record """
    record = Record.objects.get(id=id)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully.')
            return redirect ('dashboard')
    context = {'form': form}
    template_name = 'webapp/update-record.html'
    return render (request, template_name, context)

@login_required(login_url='my-login')
def view_record (request, id):
    """ Update an existing record """
    record = Record.objects.get(id=id)
    context = {'record': record}
    template_name = 'webapp/view-record.html'
    return render (request, template_name, context)

@login_required(login_url='my-login')
def delete_record (request, id):
    """ Delete an existing record """
    record = Record.objects.get(id=id)
    record.delete()
    messages.success(request, 'Record deleted.')
    return redirect ('dashboard')


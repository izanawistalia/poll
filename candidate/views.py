from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import candidateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    hackers = candidates.objects.all()
    context = {'hackers': hackers}
    return render(request, 'candidate/dashboard.html', context)

def detail(request, pk):
    candidate = candidates.objects.get(pk=pk)
    c_spcl = candidate.specialty_set.all()
    context = {'candidate': candidate, 'expertise': c_spcl}
    return render(request, 'candidate/detail.html', context)

def vote(request, pk):
    candidate = candidates.objects.get(pk=pk)
    if request.method == 'POST':
        if 'message' in request.COOKIES:
            return HttpResponse('<h1 align="center">You already voted, huh..</h1>')
        candidate.votes += 1
        candidate.save()
        response = HttpResponse('<h1 align="center">CONGO....</h1>')
        response.set_cookie('message', 'Voted')
        return response
    return HttpResponse('<h1 align="center">This Page Can\'t Be Viewed</h1>')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin_dashboard')
        else:
            messages.error(request, "username or password is incorrect..")
    return render(request, 'candidate/loginPage.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('loginPage')
    
@login_required
def admin_dashboard(request):
    candidate = candidates.objects.all()
    context = {'candidates': candidate}
    return render(request, 'candidate/admin_dashboard.html', context)

@login_required
def create(request):
    form = candidateForm()
    expert = expertise.objects.all()
    if request.method == 'POST':
        form = candidateForm(request.POST)
        if form.is_valid():
            form.save()
            candidate = candidates.objects.get(name=request.POST['name'])
            subject = expertise.objects.all()
            for sub in subject:
                specialty.objects.create(name=candidate, subject=sub, rating=request.POST[sub.name])
                
            return redirect('/admin_dashboard')
    context = {'form': form, 'expert': expert}
    return render(request, 'candidate/create.html', context)

@login_required
def update(request, pk):
    candidate = candidates.objects.get(pk=pk)
    expert = expertise.objects.all()
    form = candidateForm(instance=candidate)
    if request.method == 'POST':
        form = candidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            candidate = candidates.objects.get(name=request.POST['name'])
            candidate.expert.clear()
            subject = expertise.objects.all()
            for sub in subject:
                specialty.objects.create(name=candidate, subject=sub, rating=request.POST[sub.name])
            return redirect('/admin_dashboard')
    context = {'form': form, 'expert': expert}
    return render(request, 'candidate/create.html', context)

@login_required
def delete(request, pk):
    candidate = candidates.objects.get(pk=pk)
    if request.method == 'POST':
        candidate.delete()
        return redirect('admin_dashboard')
    context = {'candidate': candidate}
    return render(request, 'candidate/delete.html', context)
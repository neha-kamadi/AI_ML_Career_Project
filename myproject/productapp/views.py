
# Create your views here.
from itertools import count
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CareerHistory
from django.contrib.auth.decorators import login_required

import joblib, os
from django.conf import settings
model_path =  os.path.join(settings.BASE_DIR, 'productapp','career_model.pkl')
model= joblib.load(model_path)

def home(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')


def result_user(request):
    if request.method == 'POST':
        skills = request.POST['skills']
        interests = request.POST['interests']
        
        #load model
        
        model_path = os.path.join(settings.BASE_DIR, 'productapp', 'career_model.pkl')
        model = joblib.load(model_path)
        text = skills + " " + interests
        career = model.predict([text]) [0]
        return render (request, 'result.html', {'career': career})
    else:
        return render(request, 'home.html')
# AUTH VIEWS
# -----------------------------
def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created! Please log in.')
            return redirect('login')
    return render(request, 'signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

@login_required
def result(request):
    if request.method == 'POST':
        skills = request.POST.get('skills')
        interests = request.POST.get('interests')
        model_path = os.path.join(settings.BASE_DIR, 'productapp', 'career_model.pkl')
        model= joblib.load(model_path)
        text = skills + " " + interests
        career = model.predict([text])[0]

        career_paths = {
            "Data Scientist": ["Python", "Machine Learning", "Statistics", "Pandas"],
            "UI/UX Designer": ["Figma", "Adobe XD", "Creativity", "User Research"],
            "Manager": ["Leadership", "Planning", "Communication"],
            "Web Developer": ["HTML", "CSS", "JavaScript", "Django"],
            "Data Analyst": ["Excel", "SQL", "Power BI", "Python"],
            "Content Writer": ["SEO", "Copywriting", "Editing"]
        }

        suggested_skills = career_paths.get(career, [])

        # ✅ Save to history table
        if request.user.is_authenticated:
         CareerHistory.objects.create(
            user=request.user,
            skills=skills,
            interests=interests,
            career_result=career
        )

        return render(request, 'result.html', {
            'career': career,
        })
    return render(request, 'home.html')
@login_required
def dashboard(request):
    history = CareerHistory.objects.filter(user=request.user).order_by('-date')
    
    #labels = [d['career_result'] for d in data]
    #values = [int(d['count']) for d in data]
    
    labels,values = [],[]
    for record in history:
        if record.career_result:
            labels.append(record.career_result )
            values.append(1) 
            
    
    return render(request, 'dashboard.html',{
        'history':history,
        'labels': labels,
        'values': values
    })
    
    
    
    
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import  Course, Module, Assignment
from .serializers import UserSerializer, CourseSerializer, ModuleSerializer, AssignmentSerializer
from .permissions import IsTeacherOrReadOnly, IsModeratorOrReadOnly
from .auth_form import CustomAuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Assignment, Category
from .form import GradeForm


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrReadOnly | IsTeacherOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrReadOnly]

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly | IsModeratorOrReadOnly]

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]


def index(request):
    return render(request, 'index.html')

def dashboard(request):
    if not request.user.is_authenticated:
        
        return redirect('index')
    contex = {
            'is_staff':request.user.is_staff,
            'is_superuser':request.user.is_superuser
        }
    
    return render(request, 'dashboard.html', contex)

def register(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def grade_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.assignment = assignment        
            grade.student = assignment.student
            grade.save()
            # Redirect to the assignment detail page after successful submission
            return redirect(f'/api/assignment/{assignment_id}')
    else:
        form = GradeForm()

    return render(request, 'grade_assignment.html', {'form': form, 'assignment': assignment})


@login_required
def assignment_details(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    return render(request, 'assignment_details.html', {'assignment':assignment})

@login_required
def assignment(request):
    assignment = Assignment.objects.all()
    return render(request, 'assignments.html', {'assignments':assignment})

@login_required
def course(request):
    course = Course.objects.all()
    return render(request, 'course.html', {'courses':course})

@login_required
def category(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category':category})
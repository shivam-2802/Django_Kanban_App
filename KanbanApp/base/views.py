from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import View
from django.views.decorators.http import require_POST
from .models import ToDoCard, DoingCard, DoneCard
from django.http import JsonResponse


def indexPage(request):
    return render(request, 'index.html')

@login_required(login_url='index')
def homePage(request):

    user_tasks = ToDoCard.objects.filter(user=request.user)
    user_tasksdoing = DoingCard.objects.filter(user=request.user)
    user_tasksdone = DoneCard.objects.filter(user=request.user)
    taskdata = {'user_tasks': user_tasks,
                'user_tasksdoing': user_tasksdoing,
                'user_tasksdone': user_tasksdone}
    return render(request, 'home.html', taskdata)

def signupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if User.objects.filter(username=uname).exists():
            return HttpResponse("this username is already being used")
        
        if User.objects.filter(email=email).exists():
            return HttpResponse("this email is already being used")
        
        if pass1!=pass2:
            return HttpResponse("password not matching")
        else:
            app_user = User.objects.create_user(uname, email, pass1)
            app_user.save()
            return redirect('login')


    return render(request, 'signup.html')

def loginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        app_user=authenticate(request,username=uname,password=pass1)
        if app_user is not None:
            login(request,app_user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('index')




class AddTaskView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_task.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            ToDoCard.objects.create(title=title, description=description, user=request.user)
            return redirect('home')
        else:
            return HttpResponse("Error: Title and description are required.")
        

def edit_task(request, task_id):
    if request.method == 'POST':
        task = ToDoCard.objects.get(pk=task_id)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('/home/')
    else:
        task = ToDoCard.objects.get(pk=task_id)
        return render(request, 'edit_task.html', {'task': task})
    

@require_POST
def delete_task(request, task_id):
    task = ToDoCard.objects.get(pk=task_id)
    task.delete()
    return redirect('/home/')



def save_changes(request):
    if request.method == 'POST':
        task_data = request.POST.get('taskData')
        # Process task data and update the database accordingly
        return JsonResponse({'message': 'Changes saved successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

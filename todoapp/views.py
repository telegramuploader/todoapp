from django.shortcuts import render,redirect
from .models import Task,User
from .forms import Taskform
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _user_id(request, ):
    user=request.session.session_key
    if not user:
        user=request.session.create()
    return user

def index(request):
    try:
        user=User.objects.get(user_id=_user_id(request))
    except User.DoesNotExist:
        user=User.objects.create(user_id=_user_id(request))
    task=Task.objects.all().filter(user=user)
    if not task:
        return render(request,'index.html')
    return render(request,'index.html',{'task':task})
def add(request):
    user = User.objects.get(user_id=_user_id(request))
    if request.method=='POST':
        name=request.POST['task_name']
        priority=request.POST['task_priority']
        date=request.POST['task_date']
        task=Task(name=name,priority=priority,date=date,user=user)
        task.save()
        return redirect('/')
    return redirect('/')

def done(request,task_id):
    try:
        user = User.objects.get(user_id=_user_id(request))
        task=Task.objects.get(id=task_id,user=user)
        task.delete()
        return redirect('/')
    except Task.DoesNotExist:
        return render(request,'permission.html')
def update(request,task_id):
    try:
        user = User.objects.get(user_id=_user_id(request))
        task=Task.objects.get(id=task_id,user=user)
        form=Taskform(request.POST or None ,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'update.html',{'form':form,'task':task})
    except Task.DoesNotExist:
        return render(request, 'permission.html')
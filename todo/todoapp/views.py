from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def add(request):
    task1=Task.objects.filter(is_completed=False)
    if request.method == 'POST':
        name = request.POST['task']
        priority = request.POST['priority']
        date = request.POST['date']
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.is_completed = True 
        task.save()
        return redirect('/')
    return render(request, 'delete.html')

  
  
def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task} )


def completed_tasks(request):
    completed_tasks = Task.objects.filter(is_completed=True)  
    print(completed_tasks) 
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})


def tdelete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('/')
    

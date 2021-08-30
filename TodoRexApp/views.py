
from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    else:
        form = TodoForm()
    todos = Todo.objects.all()
    total_todos = Todo.objects.all().count()
    context = {'todos':todos,'total_todos':total_todos,'form':form}
    return render(request,'TodoRexApp/index.html',context=context)

def todo(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request,'TodoRexApp/todo.html',context=context)



def update(request,id):
    todos = Todo.objects.all()
    todo = Todo.objects.get(id=id)
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    else:
        form = TodoForm(instance=todo)
    context = {'todo':todo,'form':form,'todos':todos}
    return render(request,'TodoRexApp/update.html',context=context)


def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todo')

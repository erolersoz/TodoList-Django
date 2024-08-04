#from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Todo,Category,Tag
#from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
@login_required(login_url='/admin/login/')#access control
def home_view(request):
        #todos=Todo.objects.all() bring all objects
    todos=Todo.objects.filter(
        user=request.user,
        is_active=True,
        #title__icontains="todo",                      
        )
    context=dict(
        
        todos=todos#key value
    )
    return render(request,'todo/todo_list.html',context)

# def todo_detail_view(request,id):
#     try:
#         todo=Todo.objects.get(pk=id)#pk primary key anlamına geliyor yerine id de yazabilirdik
#         context=dict(
#             todo=todo,#burda yine key valu alakalı tanımladık
#     )
#         return render(request,'todo/todo_detail.html',context)
#     except Todo.DoesNotExist:
#         raise Http404
@login_required(login_url='/admin/login/')#access control
def category_view(request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    todos = Todo.objects.filter(
        is_active=True,
        category=category,
        user=request.user,
    )
    context = dict(
        todos=todos,
        category=category,
    )
    return render (request, 'todo/todo_list.html',context)



@login_required(login_url='/admin/login/')#access control
def todo_detail_view(request,category_slug,id):
    todo=get_object_or_404(Todo,category__slug=category_slug ,pk=id ,user=request.user)#bring obje or 404
    context=dict(
        todo=todo,#key value
    )
    return render(request,'todo/todo_detail.html',context)
    
    


@login_required(login_url='/admin/login/')
def tag_view(request,tag_slug):
    tag=get_object_or_404(Tag,slug=tag_slug)
    context = dict(
        tag=tag,
        todos=tag.todo_set.filter(user=request.user)
    )
    return render (request, 'todo/todo_list.html',context)

from django.shortcuts import render
from django.views import View
from .models import TodoList, Category
from django.shortcuts import redirect


# Create your views here.

class Todolist(View):
    def get(self, request):

        todos = TodoList.objects.all() #quering all todos with the object manager
        categories = Category.objects.all() #getting all categories with object manager

        return render(request, 'todo_list.html', {  "todos": todos,

                                                    "categories": categories})

    def post(self, request):
        # todos = TodoList.objects.all() #quering all todos with the object manager
        # categories = Category.objects.all() #getting all categories with object manager
        if "taskAdd" in request.POST:
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 

            return redirect("/todo") 

        if "taskDelete" in request.POST: 
            
            # checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            checkedlist = request.POST.getlist('checkedbox', '')  #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo

        return redirect("/todo") 

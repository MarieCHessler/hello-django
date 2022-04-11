from django.shortcuts import render


# Create your views here.
def get_todo_list(request):
    """ Return a response that says Hello! """
    return render(request, 'todo/todo_list.html')

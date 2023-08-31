from django.shortcuts import render

def task_view(request):
    # You can pass dynamic data to the template here if needed
    context = {
        'task_data': 'This is dynamic data from the view!',
    }
    return render(request, 'task.html', context)

from django.shortcuts import render

def post_list(request):
    return render(request, 'django/post_list.html', {})
from django.shortcuts import render

def blog_page(request):
    return render(request, 'app_blog/index.html')

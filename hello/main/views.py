from django.shortcuts import render


def mai(request):
    data = {
        'main': 'Main page',
    }
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/about.html')
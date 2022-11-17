from django.shortcuts import render, redirect


def error_404(request):
    return render(request, '404.html', status=404)

from django.shortcuts import render, redirect, get_object_or_404



def index(request):
    return render(request, 'jobs/index.html', {})


def user_profile(request, username):
    return render(request, 'jobs/index.html', {})


def job_offers(request):
    return render(request, 'jobs/index.html', {})

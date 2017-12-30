from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .forms import *



def index(request):
    return render(request, 'jobs/index.html', {})


def user_profile(request, username):
    return render(request, 'jobs/index.html', {})


def job_offers(request):
    offers = JobOffer.objects.all().order_by('-created_date')
    context = {
        'offers': offers,
    }
    return render(request, 'jobs/offers.html', context)



def job_offer_add(request):
    title = ""
    if request.method == 'POST':
        offerForm = JobOfferForm(request.POST, request.FILES)
        requirementsForm = ApplicationForm(request.POST)
        if offerForm.is_valid() and requirementsForm.is_valid():
            job_offer = offerForm.save(commit=False)
            job_offer.user = request.user
            job_offer.save()

            requirements = requirementsForm.save(commit=False)
            requirements.job_offer = job_offer
            requirements.save()

            return redirect('jobs:index')

        else:
            title = 'Invalid Form'

    offerForm = JobOfferForm()
    requirementsForm = ApplicationForm()
    context = {
        'offerForm': offerForm,
        'title': title,
        'requirements': requirementsForm,
    }
    return render(request, 'jobs/job_offer_add.html', context)


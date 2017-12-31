from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .forms import *



def index(request):
    return render(request, 'jobs/index.html', {})


def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'jobs/user_profile.html', {'user': user})


def user_applications(request, username):
    applications = []
    title = 'Your Applications'
    if request.user.is_authenticated():
        applications = JobApplication.objects.filter(user=request.user).order_by('-created_date')

    context = {
        'applications': applications,
        'title': title,
    }
    return render(request, 'jobs/user_applications.html', context)


def candidates(request, username):
    applications = []
    title = 'Your Candidates'
    if request.user.is_authenticated():
        applications = JobApplication.objects.filter(job_offer__user=request.user).order_by('-created_date')

    context = {
        'applications': applications,
        'title': title,
    }
    return render(request, 'jobs/candidates.html', context)


def user_offers(request, username):
    offers = []
    if request.user.is_authenticated():
        offers = JobOffer.objects.filter(user=request.user).order_by('-created_date')

    return render(request, 'jobs/user_offers.html', {'offers': offers})


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



def offer_detail(request, offer_id):
    offer = get_object_or_404(JobOffer, id=offer_id)
    requirements = offer.requirements.rstrip().split('-')
    requirements = filter(None, requirements)
    whatWeOffer = offer.whatWeOffer.rstrip().split('-')
    whatWeOffer = filter(None, whatWeOffer)
    jobDescription = offer.jobDescription.rstrip().split('-')
    jobDescription = filter(None, jobDescription)
    aboutUs = offer.aboutUs.splitlines()
    context = {
        'offer': offer,
        'requirements': requirements,
        'whatWeOffer': whatWeOffer,
        'jobDescription': jobDescription,
        'aboutUs': aboutUs,
    }
    return render(request, 'jobs/offer_detail.html', context)



def job_apply(request, offer_id):
    title = ""
    offer = get_object_or_404(JobOffer, id=offer_id)
    requirements = get_object_or_404(ApplicationRequirements, job_offer_id=offer_id)
    if request.method == 'POST':
        applyForm = JobApplyForm(request.POST, request.FILES)
        if applyForm.is_valid():
            apply_form = applyForm.save(commit=False)
            apply_form.user = request.user
            apply_form.job_offer = offer
            apply_form.save()

            return redirect('jobs:user_profile', username=request.user.username)
        else:
            title = 'Invalid Form'

    applyForm = JobApplyForm()
    context = {
        'offer': offer,
        'applyForm': applyForm,
        'title': title,
        'requirements': requirements,
    }
    return render(request, 'jobs/apply_now.html', context)
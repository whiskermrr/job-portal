from django import forms
from django.forms import Textarea
from django.utils.translation import gettext as _
from .models import *


class JobOfferForm(forms.ModelForm):

    class Meta:
        model = JobOffer
        fields = ['industry', 'avatar', 'title', 'companyName', 'aboutUs', 'jobDescription', 'requirements',
                  'whatWeOffer', 'salary', 'location',]

        widgets = {
            'aboutUs': Textarea(attrs={'cols': 80, 'rows': 10}),
            'jobDescription': Textarea(attrs={'cols': 80, 'rows': 10}),
            'requirements': Textarea(attrs={'cols': 80, 'rows': 10}),
            'whatWeOffer': Textarea(attrs={'cols': 80, 'rows': 10}),
        }

        labels = {
            'avatar': _('Picture of Your Company'),
            'title': _('Title'),
            'companyName': _('Company Name'),
            'aboutUs': _('About Your Company'),
            'jobDescription': _('Description of the Job'),
            'requirements': _('Requirements'),
            'whatWeOffer': _('What we Offer'),
            'salary': _('Salary'),
            'location': _('Location'),
        }

        help_texts = {
            'avatar': _('best resolution: 16:9'),
            'title': _('job name (search sensitive)'),
            'aboutUs': _('company name, people, what is your products etc.'),
            'jobDescription': _('responsibilities, working hours etc.'),
            'requirements': _('what skills candidate should have (new line is new point)'),
            'whatWeOffer': _('health care, free lunch etc. (new line is new point)'),
            'salary': _('monthly'),
            'location': _('city, street (search sensitive)'),
        }



class ApplicationForm(forms.ModelForm):

    class Meta:
        model = ApplicationRequirements
        fields = ['formPicture', 'formAge', 'formEducation', 'formPlaceOfResidence',
                  'formAboutYou', 'formCurrentStatus', 'formLanguages', 'formExperience', 'formHobby']

        labels = {
            'formPicture': _('Picture of Candidate.'),
            'formAge': _('Age of Candidate.'),
            'formEducation': _('Education of Candidate.'),
            'formPlaceOfResidence': _('Living Place of Candidate.'),
            'formAboutYou': _('Section "About".'),
            'formCurrentStatus': _('Current working status of Candidate.'),
            'formLanguages': _('Languages that Candidate knows.'),
            'formExperience': _('Previous experience of Candidate.'),
            'formHobby': _('Hobby of Candidate.'),
        }
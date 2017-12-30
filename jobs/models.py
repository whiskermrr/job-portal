from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class JobOffer(models.Model):
    INDUSTRY_TYPES = (
        ('accounting', 'Accounting'),
        ('factory' , 'Factory'),
        ('banking', 'Banking'),
        ('marketing', 'Marketing'),
        ('IT - software development', 'IT - Software Development'),
        ('IT - administration', "IT - Administration"),
        ('transport', 'Transport'),
        ('medical', 'Medical'),
        ('education', 'Education'),
        ('hospitality', 'Hospitality'),
        ('real estate', 'Real Estate'),
        ('production', 'Production'),
        ('Engineering', 'Engineering'),
        ('other', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    industry = models.CharField(choices=INDUSTRY_TYPES, max_length=50)
    avatar = models.ImageField(upload_to='media/avatars')
    title = models.CharField(max_length=70)
    companyName = models.CharField(max_length=70)
    aboutUs = models.CharField(max_length=2000)
    requirements = models.CharField(max_length=1000)
    whatWeOffer = models.CharField(max_length=1000)
    jobDescription = models.CharField(max_length=1000)
    salary = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.created_date)




class ApplicationRequirements(models.Model):
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE, blank=True)
    formPicture = models.BooleanField()
    formAge = models.BooleanField()
    formEducation = models.BooleanField()
    formPlaceOfResidence = models.BooleanField()
    formAboutYou = models.BooleanField()
    formCurrentStatus = models.BooleanField()
    formLanguages = models.BooleanField()
    formExperience = models.BooleanField()
    formHobby = models.BooleanField()



class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    picture = models.ImageField(upload_to='media/avatars')
    age = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)

    EDUCATION_TYPES = (
        ('secondary education', 'Secondary Education'),
        ('bachelor degree', 'Bachelor degree'),
        ('master degree', 'Master Degree'),
        ('engineer', 'Engineer'),
        ('other', 'Other'),
    )
    education = models.CharField(choices=EDUCATION_TYPES, max_length=50, blank=True, null=True)
    placeOfResidence = models.CharField(max_length=120, blank=True, null=True)
    aboutYou = models.CharField(max_length=1000, blank=True, null=True)

    STATUS_TYPES = (
        ('student', 'Student'),
        ('working - the same industry', 'Working - the same industry'),
        ('working - other industry', 'Working - other industry'),
        ('unemployed', 'Unemployed')
    )
    currentStatus = models.CharField(choices=STATUS_TYPES, max_length=50, blank=True, null=True)
    languages = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=1000, blank=True, null=True)
    hobby = models.CharField(max_length=300, blank=True, null=True)

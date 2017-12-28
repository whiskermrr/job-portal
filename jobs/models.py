from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class JobOffer(models.Model):
    INDUSTRY_TYPES = (
        ('Accounting', 'accounting'),
        ('Factory' , 'factory'),
        ('Banking', 'banking'),
        ('Marketing', 'marketing'),
        ('IT - Software Development', 'it - software development'),
        ('IT - Administration', "it - administration"),
        ('Transport', 'transport'),
        ('Medical', 'medical'),
        ('Education', 'education'),
        ('Hospitality', 'hospitality'),
        ('Real Estate', 'real estate'),
        ('Production', 'production'),
        ('Engineering', 'engineering'),
        ('Other', 'other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    industry = models.CharField(choices=INDUSTRY_TYPES, max_length=50)
    avatar = models.ImageField(upload_to='media/avatars')
    title = models.CharField(max_length=70)
    aboutUs = models.CharField(max_length=2000)
    requirements = models.CharField(max_length=500)
    whatWeOffer = models.CharField(max_length=500)
    salary = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    created_date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=120)




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
    picture = models.ImageField(upload_to='media/avatars')
    age = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    EDUCATION_TYPES = (
        ('Secondary Education', 'secondary education'),
        ('Bachelor Degree', 'bachelor degree'),
        ('Master Degree', 'master degree'),
        ('Engineer', 'engineer'),
        ('Other', 'other'),
    )
    education = models.CharField(choices=EDUCATION_TYPES, max_length=50)
    placeOfResidence = models.CharField(max_length=120)
    aboutYou = models.CharField(max_length=1000)

    STATUS_TYPES = (
        ('Student', 'student'),
        ('Working - The same industry', 'working - the same industry'),
        ('Working - Other industry', 'working - other industry'),
        ('Unemployed', 'unemployed')
    )
    currentStatus = models.CharField(choices=STATUS_TYPES, max_length=50)
    languages = models.CharField(max_length=100)
    experience = models.CharField(max_length=1000)
    hobby = models.CharField(max_length=300)

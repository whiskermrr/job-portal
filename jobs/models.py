from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# model ofery pracy, user ma wartosc blank True gdyz nie potrzebny nam w formularzu (uzupelniamy go w views
# pensja nie jest wymagana dlatego ma wartosc null i blank
# mamy tez python tuple (to cos co wyglada jak enum) do naszego comboboxa w formularzu
class JobOffer(models.Model):
    INDUSTRY_TYPES = (
        ('Accounting', 'Accounting'),
        ('Factory' , 'Factory'),
        ('Banking', 'Banking'),
        ('Marketing', 'Marketing'),
        ('IT - Software Development', 'IT - Software Development'),
        ('IT - Administration', "IT - Administration"),
        ('Transport', 'Transport'),
        ('Medical', 'Medical'),
        ('Education', 'Education'),
        ('Hospitality', 'Hospitality'),
        ('Real Estate', 'Real Estate'),
        ('Production', 'Production'),
        ('Engineering', 'Engineering'),
        ('Other', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    industry = models.CharField(choices=INDUSTRY_TYPES, max_length=50)
    avatar = models.ImageField(upload_to='media/avatars')
    title = models.CharField(max_length=38)
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



# jest to model przypisany do oferty
# dzieki niemu mozemy wybrac co jest wymagane w formularzu wypelnianego przez potencjalnego pracownika
# job_offer blank True gdyz nie jest potrzebna w formularzu (dodajemy ja w views.py)
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


# model cv czy po prostu aplikacji o prace
# te rzeczy ktore sa blank nie sa wymagane i sa zalezne od pol ApplicationRequirements
# tutaj tez enum do comboboxa
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    picture = models.ImageField(upload_to='media/avatars', blank=True, null=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)

    EDUCATION_TYPES = (
        ('Secondary Education', 'Secondary Education'),
        ('Bachelor degree', 'Bachelor degree'),
        ('Master Degree', 'Master Degree'),
        ('Engineer', 'Engineer'),
        ('Other', 'Other'),
    )
    education = models.CharField(choices=EDUCATION_TYPES, max_length=50, blank=True, null=True)
    placeOfResidence = models.CharField(max_length=120, blank=True, null=True)
    aboutYou = models.CharField(max_length=2000, blank=True, null=True)

    STATUS_TYPES = (
        ('Student', 'Student'),
        ('Working - the same industry', 'Working - the same industry'),
        ('Working - other industry', 'Working - other industry'),
        ('Unemployed', 'Unemployed')
    )
    currentStatus = models.CharField(choices=STATUS_TYPES, max_length=50, blank=True, null=True)
    languages = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=2000, blank=True, null=True)
    hobby = models.CharField(max_length=1000, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)


# dodalem mozliwosc stworzenia konwersacji z potencjalnym pracownikiem
# nie wiem czy gdzies indziej tez nazywa sie to CASCADE wiec wytlumacze :D
# jezeli ktorys uzytkownik zostanie usuniety to konwersacja tez (CASCADE)
# blank dlatego ze uzytkownikow ustawiamy w views
class Conversation(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='user_one')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='user_two')
    title = models.CharField(max_length=38)

# chyba nie trzeba tlumaczyc
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)
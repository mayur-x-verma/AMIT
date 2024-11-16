from django.db import models

class JobApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    college_name = models.CharField(max_length=255)
    marks = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Subscriber(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class JobVacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100, default='Varanasi')

    def __str__(self):
        return self.title

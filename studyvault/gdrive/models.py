from django.db import models

# Create your models here.
# class Resource(models.Model):
#     semester = models.CharField(max_length=50)  # e.g., "1st Semester"
#     subject = models.CharField(max_length=100)  # e.g., "Mathematics"
#     year = models.CharField(max_length=4)  # e.g., "2023"
#     resource_type = models.CharField(max_length=50)  # e.g., "notes", "books", "pyq"
#     file_link = models.URLField()  # URL to the file (Telegram link or elsewhere)
#     file_name = models.CharField(max_length=255)  # Name of the file

#     def __str__(self):
#         return f"{self.file_name} ({self.resource_type})"

class Resource(models.Model):
    semester = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=255)
    file = models.FileField(upload_to='resources/')

    def __str__(self):
        return self.file.name



# Here’s how the models.py should look for your project. Since we're focusing on a minimal Google Drive-like structure where only the file_link and file_name are displayed, along with filtering by semester, subject, year, and resource_type, here’s the reduced model:

# ### models.py

# python
# from django.db import models

# class Resource(models.Model):
#     semester = models.CharField(max_length=50)  # e.g., "1st Semester"
#     subject = models.CharField(max_length=100)  # e.g., "Mathematics"
#     year = models.CharField(max_length=4)  # e.g., "2023"
#     resource_type = models.CharField(max_length=50)  # e.g., "notes", "books", "pyq"
#     file_link = models.URLField()  # URL to the file (Telegram link or elsewhere)
#     file_name = models.CharField(max_length=255)  # Name of the file

#     def __str__(self):
#         return f"{self.file_name} ({self.resource_type})"



# ### Explanation:
# 1. **semester**: A string field to store the semester (e.g., "1st Semester").
# 2. **subject**: A string field to store the subject (e.g., "Mathematics").
# 3. **year**: A string field to store the academic year (e.g., "2023").
# 4. **resource_type**: A string field to categorize the resource (e.g., "notes", "books", "pyq").
# 5. **file_link**: A URL field to store the link to the file (could be a Telegram link, Google Drive link, etc.).
# 6. **file_name**: The name of the file that will be displayed to users.

# ### Step 1: Migration

# After modifying or adding the model, you need to run migrations to apply these changes to your database:

# bash
# python manage.py makemigrations
# python manage.py migrate


# ### Step 2: Populate the Database

# You can populate the Resource model either manually via Django’s admin interface or by importing data from a CSV (using Django management commands, which I can help you set up if needed).

# This models.py file will now integrate with your views and URL patterns to fetch and display the files according to the selected semester, subject, year, and resource_type.
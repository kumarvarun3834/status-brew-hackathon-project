# Great! Since you have the read_menu_data function to parse the CSV file and build the menu hierarchy, we can integrate this function into your Django project to populate the menus dynamically from the CSV file. The goal is to use this data for generating the menu structure and linking it to the URL patterns in your Django views.

# ### Step 1: Update views.py to Use read_menu_data

# You can use this function in your views to dynamically generate the menu based on the CSV file.

# #### Updated views.py:

# python
# from django.shortcuts import render
# from .models import Resource
# from .utils import read_menu_data  # Assuming you placed the function in a utils.py file
# import os

# # Path to your CSV file (adjust this based on your project structure)
# CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'menu_data.csv')

# # Step 1: Display all available semesters
# def semester_view(request):
#     menu_data = read_menu_data(CSV_FILE_PATH)  # Read menu from CSV
#     semesters = list(menu_data.keys())  # Get all available semesters
#     return render(request, 'semester.html', {'semesters': semesters})

# # Step 2: Display subjects for the selected semester
# def subject_view(request, semester):
#     menu_data = read_menu_data(CSV_FILE_PATH)
#     subjects = list(menu_data.get("/" + semester, {}).keys())  # Get subjects for the selected semester
#     return render(request, 'subject.html', {'semester': semester, 'subjects': subjects})

# # Step 3: Display years for the selected semester and subject
# def year_view(request, semester, subject):
#     menu_data = read_menu_data(CSV_FILE_PATH)
#     years = menu_data.get("/" + semester, {}).get("/" + subject, [])  # Get years for the selected semester and subject
#     return render(request, 'year.html', {'semester': semester, 'subject': subject, 'years': years})

# # Step 4: Display resource types for the selected semester, subject, and year
# def resource_type_view(request, semester, subject, year):
#     resource_types = ['notes', 'books', 'pyq']  # Resource types can be static
#     return render(request, 'resource_type.html', {'semester': semester, 'subject': subject, 'year': year, 'resource_types': resource_types})

# # Step 5: Display files for the selected semester, subject, year, and resource type
# def file_view(request, semester, subject, year, resource_type):
#     resources = Resource.objects.filter(semester=semester, resource_type=resource_type, year=year)
#     return render(request, 'files.html', {'resources': resources, 'semester': semester, 'subject': subject, 'year': year, 'resource_type': resource_type})


# ### Step 2: Create utils.py for the read_menu_data Function

# Place your read_menu_data function in a utility file (utils.py) so it can be used in the views.

# #### utils.py:

# python
# import csv

# def read_menu_data(filename):
#     """
#     Reads a CSV file and returns a menu hierarchy.

#     filename : str
#         The file you want to get the menu from, syntax is directory name 
#         and its subsectors in each line separated by commas.

#     Returns:
#     --------
#     dict
#         Dictionary structure representing menu hierarchy.
#     """
#     menu_data = {}  # Dictionary to store menu hierarchy
#     with open(filename, "r") as file:
#         for line in file:
#             semester, subject, year = (line.strip().split(","))
#             semester, subject, year = "/" + semester, "/" + subject, "/" + year
#             if semester not in menu_data:
#                 menu_data[semester] = {}
#             if subject not in menu_data[semester]:
#                 menu_data[semester][subject] = []
#             menu_data[semester][subject].append(year)
#     return menu_data


# ### Step 3: Update Templates to Display the Menu

# You need to update your HTML templates (semester.html, subject.html, year.html, etc.) to display the dynamic menu based on the data passed from the views.

# #### semester.html:

# html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Choose Semester</title>
# </head>
# <body>
#     <h1>Choose Semester</h1>
#     <ul>
#         {% for semester in semesters %}
#             <li><a href="/home{{ semester }}/">{{ semester|slice:"1:" }}</a></li>  <!-- Remove leading "/" -->
#         {% endfor %}
#     </ul>
# </body>
# </html>


# #### subject.html:

# html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Choose Subject</title>
# </head>
# <body>
#     <h1>Choose Subject for {{ semester }}</h1>
#     <ul>
#         {% for subject in subjects %}
#             <li><a href="/home{{ semester }}{{ subject }}/">{{ subject|slice:"1:" }}</a></li>
#         {% endfor %}
#     </ul>
# </body>
# </html>


# #### year.html:

# html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Choose Year</title>
# </head>
# <body>
#     <h1>Choose Year for {{ subject }} in {{ semester }}</h1>
#     <ul>
#         {% for year in years %}
#             <li><a href="/home{{ semester }}{{ subject }}{{ year }}/">{{ year|slice:"1:" }}</a></li>
#         {% endfor %}
#     </ul>
# </body>
# </html>


# This setup will dynamically generate the menu hierarchy from the CSV and display it in the templates based on the current step (semester, subject, year, etc.).

# ### Step 4: Test the Application

# - Ensure the menu_data.csv file is in the correct directory.
# - Start the Django server:

# bash
# python manage.py runserver


# - Visit /home/ to see the semesters, /home/semesterchoice/ for subjects, and so on.

# Let me know if you need further assistance!
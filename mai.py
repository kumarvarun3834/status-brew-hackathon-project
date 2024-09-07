# To implement a structure that dynamically displays the hierarchy as /home, /home/semesterchoice, /home/semesterchoice/subjectchoice, and so on, while maintaining the block-like structure, you can follow these steps:

# ### Objective

# The URL structure will be like:

# - /home/: Display all available semesters.
# - /home/semesterchoice/: Display subjects for the selected semester.
# - /home/semesterchoice/subjectchoice/: Display years for the selected semester and subject.
# - /home/semesterchoice/subjectchoice/yearchoice/: Display resources (notes, books, pyq) for the selected semester, subject, and year.
# - /home/semesterchoice/subjectchoice/yearchoice/resourcetype/: Display files for the chosen semester, subject, year, and resource type.

# ### Step 1: Update URL Patterns

# You need to define dynamic URL patterns for the hierarchy in your urls.py.

# **urls.py**:

# python
# from django.urls import path
# from . import views

# urlpatterns = [
#     # Step 1: Display all semesters at /home/
#     path('home/', views.semester_view, name='semester_view'),
    
#     # Step 2: Display subjects for the selected semester
#     path('home/<str:semester>/', views.subject_view, name='subject_view'),
    
#     # Step 3: Display years for the selected semester and subject
#     path('home/<str:semester>/<str:subject>/', views.year_view, name='year_view'),
    
#     # Step 4: Display resources for the selected semester, subject, and year
#     path('home/<str:semester>/<str:subject>/<str:year>/', views.resource_type_view, name='resource_type_view'),
    
#     # Step 5: Display files for the selected semester, subject, year, and resource type
#     path('home/<str:semester>/<str:subject>/<str:year>/<str:resource_type>/', views.file_view, name='file_view'),
# ]


# ### Step 2: Create Views for Each Step

# 1. *Semester View*: Display all available semesters.
# 2. *Subject View*: Display subjects based on the selected semester.
# 3. *Year View*: Display years based on the selected semester and subject.
# 4. *Resource Type View*: Display the types of resources (notes, books, pyq) for the selected semester, subject, and year.
# 5. *File View*: Display the files based on the selected resource type, semester, subject, and year.

# **views.py**:

# python
# from django.shortcuts import render
# from .models import Resource

# # Step 1: Display all available semesters
# def semester_view(request):
#     semesters = Resource.objects.values_list('semester', flat=True).distinct()
#     return render(request, 'semester.html', {'semesters': semesters})

# # Step 2: Display subjects for the selected semester
# def subject_view(request, semester):
#     subjects = Resource.objects.filter(semester=semester).values_list('resource_type', flat=True).distinct()
#     return render(request, 'subject.html', {'semester': semester, 'subjects': subjects})

# # Step 3: Display years for the selected semester and subject
# def year_view(request, semester, subject):
#     years = Resource.objects.filter(semester=semester, resource_type=subject).values_list('year', flat=True).distinct()
#     return render(request, 'year.html', {'semester': semester, 'subject': subject, 'years': years})

# # Step 4: Display resource types for the selected semester, subject, and year
# def resource_type_view(request, semester, subject, year):
#     resource_types = ['notes', 'books', 'pyq']  # Resource types can be static
#     return render(request, 'resource_type.html', {'semester': semester, 'subject': subject, 'year': year, 'resource_types': resource_types})

# # Step 5: Display files for the selected semester, subject, year, and resource type
# def file_view(request, semester, subject, year, resource_type):
#     resources = Resource.objects.filter(semester=semester, resource_type=resource_type, year=year)
#     return render(request, 'files.html', {'resources': resources, 'semester': semester, 'subject': subject, 'year': year, 'resource_type': resource_type})


# ### Step 3: Create Templates

# 1. **semester.html**: Display the available semesters.

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
#             <li><a href="/home/{{ semester }}/">{{ semester }}</a></li>
#         {% endfor %}
#     </ul>
# </body>
# </html>


# 2. **subject.html**: Display the available subjects based on the semester.

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
#             <li><a href="/home/{{ semester }}/{{ subject }}/">{{ subject }}</a></li>
#         {% endfor %}
#     </ul>
# </body>
# </html>


# 3. **year.html**: Display the available years based on the semester and subject.

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
#             <li><a href="/home/{{ semester }}/{{ subject }}/{{ year }}/">{{ year }}</a></li>
#         {% endfor %}
#     </ul>
# </body>
# </html>


# 4. **resource_type.html**: Display the resource types based on semester, subject, and year.

# html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Choose Resource Type</title>
# </head>
# <body>
#     <h1>Choose Resource Type for {{ subject }} in {{ semester }} ({{ year }})</h1>
#     <ul>
#         {% for resource_type in resource_types %}
#             <li><a href="/home/{{ semester }}/{{ subject }}/{{ year }}/{{ resource_type }}/">{{ resource_type }}</a></li>
#         {% endfor %}
#     </ul>
# </body>
# </html>


# 5. **files.html**: Display the files for the selected semester, subject, year, and resource type.

# html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{{ resource_type|title }} for {{ subject }} - {{ semester }}</title>
#     <style>
#         .file-container {
#             display: flex;
#             flex-wrap: wrap;
#             justify-content: space-around;
#             gap: 20px;
#             margin-top: 20px;
#         }

#         .file-block {
#             width: 150px;
#             height: 150px;
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             justify-content: center;
#             border: 2px solid #ccc;
#             border-radius: 10px;
#             padding: 10px;
#             text-align: center;
#             background-color: #f9f9f9;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: transform 0.2s;
#         }

#         .file-block:hover {
#             transform: scale(1.05);
#         }

#         .file-link {
#             text-decoration: none;
#             color: #333;
#             font-weight: bold;
#             margin-top: 10px;
#         }
#     </style>
# </head>
# <body>
#     <h1>{{ resource_type|title }} for {{ subject }} - {{ semester }} ({{ year }})</h1>

#     <div class="file-container">
#         {% for resource in resources %}
#             <div class="file-block">
#                 <a href="{{ resource.file_link }}" class="file-link" target="_blank">
#                     {{ resource.file_name }}
#                 </a>
#             </div>
#         {% endfor %}
#     </div>
# </body>
# </html>


# ### Step 4: Testing

# 1. *Run the Django development server*:

#    bash
#    python manage.py runserver
   

# 2. *Test the URL structure*:

#    - /home/: Displays all semesters.
#    - /home/1st-semester/: Displays subjects for the selected semester.
#    - /home/1st-semester/math/: Displays years for the selected semester and subject.
#    - /home/1st-semester/math/2023/: Displays resource types for the selected semester, subject, and year.
#    - /home/1st-semester/math/2023/notes/: Displays files for the selected semester, subject
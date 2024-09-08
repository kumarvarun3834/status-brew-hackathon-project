from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource
from .utils import read_menu_data  # Assuming you placed the function in a utils.py file
import os
from .utils import read_menu_data
# Create your views here.

# Path to your CSV file (adjust this based on your project structure)
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'menu_data.csv')
# menu_data = read_menu_data("studyvault\gdrive\main_menu_buttons")
# os.path.join(os.path.dirname(__file__), "main_menu_buttons")
# import os
menu_data = read_menu_data(os.path.join(os.path.dirname(__file__), "main_menu_buttons"))

# step 0: getstarted page
def home_view(request):
    # this will generate the getstarted page
    # / dir
    return render(request, 'index.html')

# Step 1: Display all available semesters
def semester_view(request):
    # this will show semester 
    # /semesterchoise dir >>select semester chnages to that text like semester1 , semester 2 etc and redirect to automatically to /semester1/subjectchoise
    semesters = list(menu_data.keys())  # Get all available semesters
    return render(request, 'semester.html', {'semesters': semesters})

# Step 2: Display subjects for the selected semester
def subject_view(request, semester):
    # this will show subjects 
    # /semester1/subjectchoise dir >> select subjects chenged to text subject name like physics maths all and redirects automatically to /semester1/subjectname/yearchoise 
    
    subjects = list(menu_data.get("/" + semester, {}).keys())  # Get subjects for the selected semester
    return render(request, 'subject.html', {'semester': semester, 'subjects': subjects})

# Step 3: Display years for the selected semester and subject
def year_view(request, semester, subject):
    # this will display the year choise 
    # /semester1/subjectname/yearchoise >> select year like 2023 , 2024 etc after click changes to /semester1/subjectname/year/resourcechoise automatically
    #  
    years = menu_data.get("/" + semester, {}).get("/" + subject, [])  # Get years for the selected semester and subject
    return render(request, 'year.html', {'semester': semester, 'subject': subject, 'years': years})

# Step 4: Display resource types for the selected semester, subject, and year
def resource_type_view(request, semester, subject, year):
    # this will show type filter like resourse type 
    # /semester1/subjectname/year/resourcechoise >> click chnages to any of below button name like /semester1/subjectname/year/PYQs and redirects to /semester1/subjectname/year/PYQs/files automatically

    resource_types = ['notes', 'books', 'pyq']  # Resource types can be static
    return render(request, 'resource_type.html', {'semester': semester, 'subject': subject, 'year': year, 'resource_types': resource_types})

# Step 5: Display files for the selected semester, subject, year, and resource type
def file_view(request, semester, subject, year, resource_type):
    # this will show files that are inside the csv 
    # all the messages are in form message id in back and file name is shown just make a for loop and a test data for it 
    # when user clicks the image it redirects and run a specific python code to get file and show a menu at /semester1/subjectname/year/PYQs/files/id given that id is always unique and id is int type it contais 2 buttons like if code run both will show but if code doesnt run it will show only one button and that one button is fixed that it will redirct to that specific id link of csv file 

    resources = Resource.objects.filter(semester=semester, subject=subject, year=year, resource_type=resource_type)
    return render(request, 'files.html', {'resources': resources, 'semester': semester, 'subject': subject, 'year': year, 'resource_type': resource_type})

# from django.shortcuts import render
# from .models import Resource

# def directory_structure(request):
#     # Prepare a dictionary with the hierarchical structure
#     structure = {}

#     resources = Resource.objects.all()
#     for resource in resources:
#         semester = resource.semester
#         subject = resource.subject
#         year = resource.year
#         resource_type = resource.resource_type

#         if semester not in structure:
#             structure[semester] = {}
#         if subject not in structure[semester]:
#             structure[semester][subject] = {}
#         if year not in structure[semester][subject]:
#             structure[semester][subject][year] = {}
#         if resource_type not in structure[semester][subject][year]:
#             structure[semester][subject][year][resource_type] = []

#         structure[semester][subject][year][resource_type].append({
#             'name': resource.file.name,
#             'url': resource.file.url
#         })

#     return render(request, 'directory.html', {'structure': structure})

# def file_view(request, semester, subject, year, resource_type):
#     resources = Resource.objects.filter(
#         semester=semester,
#         subject=subject,
#         year=year,
#         resource_type=resource_type
#     )
    
#     file_data = [{
#         'name': resource.file.name,
#         'url': resource.file.url
#     } for resource in resources]
    
#     return render(request, 'files.html', {'files': file_data, 'semester': semester, 'subject': subject, 'year': year, 'resource_type': resource_type})

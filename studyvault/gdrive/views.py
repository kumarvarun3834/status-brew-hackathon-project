from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource
# Create your views here.

# Step 1: Display all available semesters
def semester_view(request):
    semesters = Resource.objects.values_list('semester', flat=True).distinct()
    return render(request, 'semester.html', {'semesters': semesters})

# Step 2: Display subjects for the selected semester
def subject_view(request, semester):
    subjects = Resource.objects.filter(semester=semester).values_list('resource_type', flat=True).distinct()
    return render(request, 'subject.html', {'semester': semester, 'subjects': subjects})

# Step 3: Display years for the selected semester and subject
def year_view(request, semester, subject):
    years = Resource.objects.filter(semester=semester, resource_type=subject).values_list('year', flat=True).distinct()
    return render(request, 'year.html', {'semester': semester, 'subject': subject, 'years': years})

# Step 4: Display resource types for the selected semester, subject, and year
def resource_type_view(request, semester, subject, year):
    resource_types = ['notes', 'books', 'pyq']  # Resource types can be static
    return render(request, 'resource_type.html', {'semester': semester, 'subject': subject, 'year': year, 'resource_types': resource_types})

# Step 5: Display files for the selected semester, subject, year, and resource type
def file_view(request, semester, subject, year, resource_type):
    resources = Resource.objects.filter(semester=semester, resource_type=resource_type, year=year)
    return render(request, 'files.html', {'resources': resources, 'semester': semester, 'subject': subject, 'year': year, 'resource_type': resource_type})

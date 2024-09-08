from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def read_menu_data(filename):
    """Reads the file and returns a dictionary of semesters, subjects, and years."""
    menu_data = {}  # Dictionary to store menu hierarchy
    with open(filename, "r") as file:
        for line in file:
            semester, subject, year = line.strip().split(",")
            semester_path = "/" + semester
            subject_path = "/" + subject
            year_path = "/" + year

            if semester_path not in menu_data:
                menu_data[semester_path] = {}
            if subject_path not in menu_data[semester_path]:
                menu_data[semester_path][subject_path] = []
            menu_data[semester_path][subject_path].append(year_path)
    
    return menu_data

# Load menu data from the file
menu_data = read_menu_data('data_share_bot\main_menu_buttons')

# Routes for each HTML page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/semester')
def semester():
    # Display the list of semesters
    semesters = list(menu_data.keys())
    return render_template('semester.html', semesters=semesters)

@app.route('/subject/<semester>')
def subject(semester):
    # Get subjects for the selected semester
    subjects = menu_data.get("/" + semester, {})
    return render_template('subject.html', subjects=subjects, semester=semester)

@app.route('/year/<semester>/<subject>')
def year(semester, subject):
    # Get years for the selected semester and subject
    years = menu_data.get("/" + semester, {}).get("/" + subject, [])
    return render_template('year.html', years=years, subject=subject, semester=semester)

@app.route('/resource/<year>')
def resource(year):
    # Display static resources for simplicity
    resources = [" Books", " PYQs", " Notes"]
    return render_template('resource.html', resources=resources, year=year)

if __name__ == '__main__':
    app.run(debug=True)

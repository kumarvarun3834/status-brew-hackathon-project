from flask import Flask, render_template, request, redirect, url_for
import pandas as pd


app = Flask(__name__)

def read_menu_data(filename):
    """filename : file you wanted to get menu from and syntax is directory name and its sub sector in each line seperated by commas"""
    filename="main_menu_buttons"
    menu_data = {}  # Dictionary to store menu hierarchy
    with open(filename, "r") as file:
        for line in file:
            semester, subject, year = (line.strip().split(","))
            semester, subject, year = "/"+semester, "/"+subject, "/"+year
            if semester not in menu_data:
                menu_data[semester] = {}
            if subject not in menu_data[semester]:
                menu_data[semester][subject] = []
            menu_data[semester][subject].append(year)
        # print(menu_data)
    return menu_data

# # Load data from CSV
# def read_menu_data():
#     data = pd.read_csv('menu_data.csv')
#     return data
menu_data = read_menu_data()

sem=yer=sub=res=None
# Routes for each HTML page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/semester')
def semester():
    # Load semester data from CSV or a database
    
    semesters = menu_data.keys()

    return render_template('semester.html', semesters=semesters)

@app.route('/subject/<semester>')
def subject(semester):
    sem=semester
    subjects = menu_data[sem]  # Filter based on semester if necessary
    return render_template('subject.html', subjects=subjects, semester=sem)

@app.route('/year/<subject>')
def year(subject):
    sub=subject
    years=menu_data[sem][sub]
    # years = ['1st Year', '2nd Year', '3rd Year', '4th Year']
    return render_template('year.html', years=years , subject=sub)

@app.route('/resource/<year>')
def resource(year):
    yer=year
    resources = ["Books","PYQs", "Notes"]  # Load resources based on the year
    return render_template('resource.html', resources=resources, year=year)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    telegram_bot_send_text(message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

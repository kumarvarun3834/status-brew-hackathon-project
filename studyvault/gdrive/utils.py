import csv

def read_menu_data(filename="studyvault\gdrive\main_menu_buttons"):
    """
    Reads a CSV file and returns a menu hierarchy.

    filename : str
        The file you want to get the menu from, syntax is directory name 
        and its subsectors in each line separated by commas.

    Returns:
    --------
    dict
        Dictionary structure representing menu hierarchy.
    """
    menu_data = {}  # Dictionary to store menu hierarchy
    with open(filename, "r") as file:
        for line in file:
            semester, subject, year = (line.strip().split(","))
            semester, subject, year = "/" + semester, "/" + subject, "/" + year
            if semester not in menu_data:
                menu_data[semester] = {}
            if subject not in menu_data[semester]:
                menu_data[semester][subject] = []
            menu_data[semester][subject].append(year)
    return menu_data


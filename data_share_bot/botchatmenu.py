# this file woll handle the menu and redirection to another directories


def read_menu_data(filename):
    """filename : file you wanted to get menu from and syntax is directory name and its sub sector in each line seperated by commas"""
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
menu=read_menu_data("datasharebot\main_menu_buttons")
# # print(menu["/semester1"]
# print(list(menu.keys()))
from data import *
def display_semester(baseurl,TOKEN,user,update,menu_data=read_menu_data("datasharebot\main_menu_buttons")):
    """
    baseurl,TOKEN : requirement for working of bot
    temp_offset : from which update id we have to read data
    user : its the userid from which we have to get results
    menu_data : data from where we are getting our directory
    """
    # this message will show user a menu of semesters that are currently stored in it
    # Display the main menu (semesters)
    menu_text = "Choose a semester:\n"
    
    for semester in menu_data:
        menu_text += f"{semester}\n"

    import send_message
    send_message.sendMessage(baseurl,TOKEN,user,menu_text,update["message_id"])
    print(menu_text)


def display_subject(baseurl,TOKEN,user,semester_choice,update,menu_data=read_menu_data("datasharebot\main_menu_buttons")):
    """
    baseurl,TOKEN : requirement for working of bot
    temp_offset : from which update id we have to read data
    user : its the userid from which we have to get results
    semester_choice : the subjects inside the semesters directory
    menu_data : data from where we are getting our directory
    """
    # this message will show user a menu of semesters that are currently stored in it
    # Display the main menu (semesters)
    menu_text = "Choose a subject:\n"
    for subject in (menu_data[semester_choice]):
        menu_text += f"{subject}\n"

    import send_message
    send_message.sendMessage(baseurl,TOKEN,user,menu_text,update["message_id"])
    print(menu_text)

    

user_data = {}  # Dictionary to keep track of each user's offset


           

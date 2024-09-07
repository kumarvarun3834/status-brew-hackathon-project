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

user_data = {}  # Dictionary to keep track of each user's offset


           

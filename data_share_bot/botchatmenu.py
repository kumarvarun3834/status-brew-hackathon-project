# this file will handle the menu and redirection to another directories

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
# menu=read_menu_data("data_share_bot\main_menu_buttons")
# # print(menu["/semester1"]
# print(list(menu.keys()))
from data import *
def display_semester(baseurl,TOKEN,user,update,menu_data=read_menu_data("data_share_bot\main_menu_buttons")):
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


def display_subject(baseurl,TOKEN,user,semester_choice,update,menu_data=read_menu_data("data_share_bot\main_menu_buttons")):
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

    
def display_years(baseurl,TOKEN,user,semester_choice,subject_choice,update,menu_data=read_menu_data("data_share_bot\main_menu_buttons")):
    """
    baseurl,TOKEN : requirement for working of bot
    temp_offset : from which update id we have to read data
    user : its the userid from which we have to get results
    semester_choice : the semester directory
    subject_choice : the subjects inside the semesters directory
    menu_data : data from where we are getting our directory
    """
    # this message will show user a menu of semesters that are currently stored in it
    # Display the main menu (semesters)
    menu_text = "Choose a year:\n"
    for year in (menu_data[semester_choice][subject_choice]):
        menu_text += f"{year}\n"

    import send_message
    send_message.sendMessage(baseurl,TOKEN,user,menu_text,update["message_id"])
    print(menu_text)

def display_resourse_type(baseurl,TOKEN,user,update):
    """
    baseurl,TOKEN : requirement for working of bot
    temp_offset : from which update id we have to read data
    user : its the userid from which we have to get results
    """
    # this message will show user a menu of semesters that are currently stored in it
    # Display the main menu (semesters)
    menu_text = "Choose a year:\n"
    for type in (["/Books, /PYQs, /Notes"]):
        menu_text += f"{type}\n"

    import send_message
    send_message.sendMessage(baseurl,TOKEN,user,menu_text,update["message_id"])
    print(menu_text)

user_data = {}  # Dictionary to keep track of each user's offset

def add_or_update_user(user_id, user_offset, command=None, semester_choice=None, subject_choice=None, year_choice=None, resource_type=None):
    user_data[f'{user_id}'] = [user_offset, command, semester_choice, subject_choice, year_choice, resource_type]

def main_menu(baseurl,TOKEN,user,user_data,update,text=None,menu_data=read_menu_data("data_share_bot\main_menu_buttons")):
    print(text)

    if text.count("/")>1:
        lst= (text.strip().split("/"))
        user_data[1]="/"+lst[4]
        user_data[2]="/"+lst[0]
        user_data[3]="/"+lst[1]
        user_data[4]="/"+lst[2]
        user_data[5]="/"+lst[3]


    if text in ["/getfiles","/addfiles","/getfile","/listfiles"] or user_data[user][1] == "/getfiles" or user_data[user][1]=="/addfiles" or user_data[user][1] == "/getfile" or user_data[user][1] == "/listfiles": 
        # here the conditions are been checked either to add files or get files
        
        
            
        if text in ["/getfile","/addfiles","/getfiles","/listfiles"]:
            # here the text is being updated that it when command is passed
            # selected list elements are saved already just updated action
            user_data[user][1]=text
            import send_message
            send_message.sendMessage(baseurl,TOKEN,user,f"setted your command to {text[1:]}",update["message_id"])

        
        
        if user_data[user][1]=="/getfile" or text=="/getfile":
            if text=="/getfiles":
                import send_message
                send_message.sendMessage(baseurl,TOKEN,user,"send me message_id you want \n \n note-to get list of files send /listfiles",[update["message_id"]])
            else:
                # shareing logic 
                import copymessage
                copymessage.copyMessage(baseurl,TOKEN,user,store,text)

        elif user_data[user][2] == None and text not in list(menu_data.keys()):
            # text not in list(menu_data.keys()) this is required to prevent multiple results
            display_semester(baseurl,TOKEN,int(user),update)
            print('semester_choice sent-------------------------')
        

        if user_data[user][2] in list(menu_data.keys()) or text in list(menu_data.keys()):
            print("this is also running")
            # here its checking for the semester choice exist or not in list

            if text in list(menu_data.keys()):
                # here the text is being updated
                user_data[user][2]=text
                user_data[user][3]=None
                user_data[user][4]=None
                user_data[user][5]=None


            semester_choice=user_data[user][2]
    
            if user_data[user][3] == None and text not in menu_data[semester_choice]:
                display_subject(baseurl,TOKEN,int(user),semester_choice,update)
                print('subject choice sent-------------------------')

            if user_data[user][3] in menu_data[semester_choice] or text in menu_data[semester_choice]:
                if text in menu_data[semester_choice]:
                    user_data[user][3]=text
                    user_data[user][4]=None
                    user_data[user][5]=None

                subject_choice=user_data[user][3]

                if user_data[user][4] == None and text not in menu_data[semester_choice][subject_choice]:
                    display_years(baseurl,TOKEN,int(user),semester_choice,subject_choice,update)
                    print('year choice sent-------------------------')

                if user_data[user][4] in menu_data[semester_choice][subject_choice] or text in menu_data[semester_choice][subject_choice]:
                    if text in menu_data[semester_choice][subject_choice]:
                        user_data[user][4]=text
                        user_data[user][5]=None

                    
                    year_choice=user_data[user][4]

                    if user_data[user][5] == None and text not in ["/Books", "/PYQs", "/Notes"] :
                        display_resourse_type(baseurl,TOKEN,user,update)
                        print('resource choice sent-------------------------')
                    
                    if user_data[user][5] in ["/Books", "/PYQs", "/Notes"] or text in ["/Books", "/PYQs", "/Notes"]:
                        print("till hare reachged")

                        if text in ["/Books", "/PYQs", "/Notes"]:
                            user_data[user][5]=text
                    
                        resource_choice=user_data[user][5]
    
                        if user_data[user][5] in ["/Books", "/PYQs", "/Notes"] and user_data[user][1]=="/addfiles":
                            import addfiles

                            if "document" in update:
                                new_data=update
                                addfiles.write_file(baseurl,TOKEN,semester_choice,subject_choice,year_choice,resource_choice,new_data)
                            else:
                                import send_message
                                send_message.sendMessage(baseurl,TOKEN,user,"this bot can only save file type documents",update["message_id"])

                        elif user_data[user][5] in ["/Books", "/PYQs", "/Notes"] and user_data[user][1]=="/getfiles":
                            import addfiles
                            addfiles.share_files(baseurl,TOKEN,user,semester_choice,subject_choice,year_choice,resource_choice)

                        elif user_data[user][5] in ["/Books", "/PYQs", "/Notes"] and user_data[user][1]=="/listfiles":
                            import addfiles
                            addfiles.share_file(baseurl,TOKEN,user,semester_choice,subject_choice,year_choice,resource_choice)
                            import send_message
                            send_message.sendMessage(baseurl,TOKEN,user,"send me the text id of that file you want",update["message_id"])
                            user_data[user][1]="/getfile"
                            send_message.sendMessage(baseurl,TOKEN,user,"setted your command to getfiles",update["message_id"])


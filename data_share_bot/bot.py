# actual bot logic will be places here ie start of code

import threading
from typing import NoReturn
from data import *
from getupdates import *
import botchatmenu 

# def handle_user_update(baseurl, TOKEN, update,user_data):
#     chat_id = update["message"]["chat"]["id"]
#     # Check if 'text' key exists in the update
#     if "text" in update["message"]:
#         text = update["message"]["text"]
#         # Your existing logic for handling text updates
#     else:
#         text=None
#         # Handle non-text updates or log an appropriate message
#         print("Received a non-text message update.")

#     temp_offset = update["update_id"] + 1

#     user = update["message"]["chat"]
#     print(f"passes through main menu /start for user {chat_id}")
#     if text=="/start":
#         botchatmenu.add_or_update_user(chat_id, temp_offset)
#         menu_text="WELCOME TO THE BOT"+"\n"+"CHOOSE YOUR ACTION"+"\n"+"/addfiles"+" -to add more files to bot"+"\n"+"/getfiles"+" - to get files from the bot"

#         import send_message
#         send_message.sendMessage(baseurl,TOKEN,chat_id,menu_text)
    
#     elif text =="/stop":
#         del user_data[f'{chat_id}']
#         import send_message
#         send_message.sendMessage(baseurl,TOKEN,chat_id,"Bot stopped to activate it again send : /start")
#     else:
#         botchatmenu.main_menu(baseurl, TOKEN ,f"{chat_id}",user_data,update["message"],text)
        
#     # botchatmenu.main_menu(baseurl, TOKEN ,f"{chat_id}",user_data,update["message"],text)

def handle_user_update(baseurl, TOKEN, update,user_data) -> None:
    # print(update)
    chat_id = update["message"]["chat"]["id"]
    # Check if 'text' key exists in the update
    if "text" in update["message"]:
        text = update["message"]["text"]
        # Your existing logic for handling text updates
    else:
        text=None
        # Handle non-text updates or log an appropriate message
        print("Received a non-text message update.")

    temp_offset = update["update_id"] + 1

    user = update["message"]["chat"]
    print(f"passes through main menu /start for user {chat_id}")
    if text=="/start":
        botchatmenu.add_or_update_user(chat_id, temp_offset) 
        menu_text="WELCOME TO THE BOT"+"\n"+"CHOOSE YOUR ACTION"+"\n"+"/addfiles"+" -to add more files to bot"+"\n"+"/getfiles"+" - to get files from the bot"
        import send_message
        send_message.sendMessage(baseurl,TOKEN,chat_id,menu_text,update["message"]["message_id"])
        
    elif text =="/stop":
        del user_data[f'{chat_id}']
        import send_message
        send_message.sendMessage(baseurl,TOKEN,chat_id,"Bot stopped to activate it again send : /start",update["message"]["message_id"])
    else:
        botchatmenu.main_menu(baseurl, TOKEN ,f"{chat_id}",user_data,update["message"],text)
 
# Recalculate the global_offset
# global offset
global_offset=845428994
threads = [] 


def main(global_offset,user_data,threads):
    print("bot is getting updates")
    while True:
        updates = get_updates(baseurl, TOKEN, global_offset)
    
        import check_userid
        check_userid.userid(updates)
    
        if updates!=[]:
            global_offset=updates[-1]["update_id"]
        threads=[]
        print(user_data)
        for update in updates:
            if "message" in update:
                import forward_messages
                print(update["update_id"])
                trash=forward_messages.forwardMessages(baseurl,TOKEN,monitor,update["message"]["chat"]["id"],message_ids=update["message"]["message_id"])
                chat_id = update["message"]["chat"]["id"]
                temp_offset=update["update_id"] 
                global_offset+=1
                print(list(user_data.keys()))
                if str(chat_id) not in user_data:
                    print(f"new user {chat_id} is being added to dict")
                    botchatmenu.add_or_update_user(str(chat_id), temp_offset)
                thread = threading.Thread(target=handle_user_update, args=(baseurl, TOKEN,  update,user_data))
                # thread = threading.Thread(target=forward_messages, args=(baseurl,TOKEN,monitor,update["message"]["chat"]["id"],update["message"]["message_id"]))

                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()
    # print("bot is getting updates")
    # while True:
    #     updates = get_updates(baseurl, TOKEN, global_offset)
    
    #     import check_userid
    #     check_userid.userid(updates)
    
    #     if updates!=[]:
    #         global_offset=updates[-1]["update_id"]
        
    #     print(user_data)
    #     for update in updates:
    #         chat_id = update["message"]["chat"]["id"]
    #         temp_offset=update["update_id"] 
    #         global_offset+=1
    #         print(list(user_data.keys()))
    #         if str(chat_id) not in user_data:
    #             print(f"new user {chat_id} is being added to dict")
    #             botchatmenu.add_or_update_user(str(chat_id), temp_offset)
    #         thread = threading.Thread(target=handle_user_update, args=(baseurl, TOKEN,  update,user_data))
    #         threads.append(thread)
    #         thread.start()

    #     for thread in threads:
    #         thread.join()

main(global_offset,botchatmenu.user_data,threads)

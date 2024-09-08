# this file stores the user ids into a file just test case 
def userid(lst) -> None:  
    # this file check and stores user id of all users   
    if lst!=[]:
        with open("data_share_bot\datafile\chats", "r") as users:
            existing_users=users.readlines()

        for i in lst:
            if "message" in i:
                user_id=f'{i["message"]["chat"]["id"]}\n'

                if user_id not in existing_users:
                # Write the new user_id to the file
                    with open("data_share_bot\datafile\chats", "a") as users:
                        users.write(user_id)
                        print(f"User {user_id} added.")
                else:
                    print(f"User {user_id} already exists.")
# it will handle data store and all the file handing system of the files

import pandas as pd
from data import  store,monitor

new_data={"message_id": 7,
                "from": {
                    "id": 1789016259,
                    "is_bot": False,
                    "first_name": "Beelzebub",
                    "language_code": "en"
                },
                "chat": {
                    "id": 1789016259,
                    "first_name": "Beelzebub",
                    "type": "private"
                },
                "date": 1718298113,
                "document": {
                    "file_name": "__init__.py",
                    "mime_type": "text/x-python",
                    "file_id": "BQACAgUAAxkBAAMHZmsmAS_x7iMkj4pcsJ7oKKKH8IAAAgoPAAI-ZlhXpdvvIXf93no1BA",
                    "file_unique_id": "AgADCg8AAj5mWFc",
                    "file_size": 3944}}

# print(res["from"].values())
# df1={"semester":"/semester1",
#     "subject":"/Maths 1",
#     "year":"/2023-24",
#     "file_link":"dsjdckjdsncld",
#     "from_id":res["from"]["id"],
#     "chat_id":res["chat"]["id"],
#     "date":res["date"],
#     "file_name": res["document"]["file_name"],
#     "mime_type": res["document"]["mime_type"],
#     "file_id":res["document"]["file_id"],
#     "file_unique_id": res["document"]["file_unique_id"],
#     "file_size": res["document"]["file_size"]
#     }

# print(res["from"]["id"])
# data=pd.DataFrame(df1)
# print(data)
import os,csv
# import get_file_link



def write_file(baseurl,TOKEN,semester_choice,subject_choice,year_choice,new_data, database="datasharebot/datafile/data.csv"):
    file_exists = os.path.isfile(database)
    # file_link=get_file_link.get_file_link(baseurl,TOKEN)
    import forward_messages
    message_id=forward_messages.forwardMessages(baseurl,TOKEN,store,new_data["chat"]["id"],new_data["message_id"])

    df1={
        "message_id":message_id,
        "semester":semester_choice,
        "subject":subject_choice,
        "year":year_choice,
        "file_link":"",
        "from_id":new_data["from"]["id"],
        "chat_id":new_data["chat"]["id"],
        "date":new_data["date"],
        "file_name": new_data["document"]["file_name"],
        "mime_type": new_data["document"]["mime_type"],
        "file_id":new_data["document"]["file_id"],
        "file_unique_id": new_data["document"]["file_unique_id"],
        "file_size": new_data["document"]["file_size"]
        }
    
    file_exists = os.path.isfile(database)
    # Write the header only if the file does not already exist
        
    with open(database, "a", newline='') as f:
        fieldnames = df1.keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Write the header only if the file does not already exist
        if not file_exists:
            writer.writeheader()
            
        writer.writerow(df1)

    import send_message
    send_message.sendMessage(baseurl,TOKEN,new_data["chat"]["id"],"your given data had been recorded",new_data["message_id"])

# write_file(df1)

# mi=[1,4,3,2,6,8,5,3,9]
# mi.sort()
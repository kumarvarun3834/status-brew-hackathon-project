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



def write_file(baseurl,TOKEN,semester_choice,subject_choice,year_choice,new_data, database="data_share_bot\datafile\data.csv"):
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

def share_file(baseurl,TOKEN,user,semester_choice,subject_choice,year_choice,file='data_share_bot\datafile\data.csv'):
    # share list of files
    database=pd.read_csv(file)
    
    semester_filter=database[database["semester"]==semester_choice]
    subject_filter=semester_filter[semester_filter["subject"]==subject_choice]
    year_filter=subject_filter[subject_filter["year"]==year_choice]
    # print(semester_choice,"---------------------------------------")
    # print(semester_filter)
    # print(subject_choice,"---------------------------------------")

    # print(subject_filter)
    # print(year_choice,"---------------------------------------")

    # print(year_filter)
# 
    # print("Database shape:", database.shape)
    # print("Chat ID from new_data:", new_data["chat"]["id"])

    # database=database[database["from_id"]== new_data["chat"]["id"]]

    columns_to_keep = ["message_id","file_name","file_link","mime_type","file_size"]
    filtered = year_filter[columns_to_keep]
    filtered.reset_index(drop=True, inplace=True)
    # user=new_data["chat"]["id"]
    
    import files_handling
    files_handling.pdf_creation(baseurl,TOKEN,filtered,user)

def share_files(baseurl,TOKEN,user,semester_choice,subject_choice,year_choice,file='data_share_bot\datafile\data.csv'):
    database=pd.read_csv(file)
    semester_filter=database[database["semester"]==semester_choice]
    subject_filter=semester_filter[semester_filter["subject"]==subject_choice]
    year_filter=subject_filter[subject_filter["year"]==year_choice]


    print("Database shape:", database.shape)
    print("Chat ID from new_data:", new_data["chat"]["id"])

    # database=database[database["from_id"]== new_data["chat"]["id"]]

    columns_to_keep = ["message_id","file_name","file_link","mime_type","file_size"]
    filtered = year_filter[columns_to_keep]
    print(year_filter)

    # user=new_data["chat"]["id"]
    # Extract 'city' column as a list
    messageidslst = list(filtered['message_id'].tolist())
    messageidslst.sort()

    # Check the length
    if len(messageidslst) > 90:
        # Split into chunks of 90
        chunks = [messageidslst[i:i + 90] for i in range(0, len(messageidslst), 90)]
    else:
        # If length <= 90, keep the list as is
        chunks = [messageidslst]

    # Now 'chunks' is a list of lists, each with a maximum length of 90
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}: {chunk}")
    print(chunks)
    import copymessages
    for  i in chunks:
        print("------------------------------------------------------------------------")
        copymessages.copyMessages(baseurl,TOKEN,user,store,i)
        print("message sent of file", i)


# mi=[1,4,3,2,6,8,5,3,9]
# mi.sort()
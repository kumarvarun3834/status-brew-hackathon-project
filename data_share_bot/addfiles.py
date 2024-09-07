# it will handle data store and all the file handing system of the files

import pandas as pd
from data import  store,monitor
import os,csv
from data import cloud , public

def write_file(baseurl,TOKEN,semester_choice,subject_choice,year_choice,resource_type,new_data, database="data_share_bot\datafile\data.csv"):
    file_exists = os.path.isfile(database)
    # file_link=get_file_link.get_file_link(baseurl,TOKEN)
    import forward_messages
    message_id=forward_messages.forwardMessages(baseurl,TOKEN,store,new_data["chat"]["id"],new_data["message_id"])
    import get_link_public
    get_link_public.generateMessageLink(chat_id=store, message_id=message_id, username=None, is_private=True)
    get_link_public.generateMessageLink(chat_id=cloud, message_id=message_id, username=public, is_private=False)

    df1={
        "message_id":message_id,
        "semester":semester_choice,
        "subject":subject_choice,
        "year":year_choice,
        "resource_type":resource_type,
        "file_link":"",
        "backup_file_link":"",
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

def share_file(baseurl,TOKEN,user,semester_choice,subject_choice,year_choice,resource_type,file='data_share_bot\datafile\data.csv'):
    # share list of files
    database=pd.read_csv(file)
    
    semester_filter=database[database["semester"]==semester_choice]
    subject_filter=semester_filter[semester_filter["subject"]==subject_choice]
    year_filter=subject_filter[subject_filter["year"]==year_choice]
    final_filter=year_filter[year_filter["resource_type"]==resource_type]

    columns_to_keep = ["message_id","file_name","file_link","mime_type","file_size"]
    filtered = final_filter[columns_to_keep]
    filtered.reset_index(drop=True, inplace=True)
    
    import files_handling
    files_handling.pdf_creation(baseurl,TOKEN,filtered,user)

def share_files(baseurl,TOKEN,user,semester_choice,subject_choice,year_choice,resource_type,file='data_share_bot\datafile\data.csv'):
    database=pd.read_csv(file)
    semester_filter=database[database["semester"]==semester_choice]
    subject_filter=semester_filter[semester_filter["subject"]==subject_choice]
    year_filter=subject_filter[subject_filter["year"]==year_choice]
    final_filter=year_filter[year_filter["resource"]==resource_type]

    columns_to_keep = ["message_id","file_name","file_link","mime_type","file_size"]
    filtered = final_filter[columns_to_keep]
    print(year_filter)

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

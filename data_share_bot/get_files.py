# this will share the files to user
# this file handles message id to share
from data import store
import pandas as pd
def get_files(baseurl,TOKEN,user,text,database="userfilestorebot/datafile/data.csv") -> None:
    
    data=pd.read_csv(database)

    filter=data[data["message_id"]==text] 
    # filter=filter[filter["message_id"]==text] 
    filter=filter[filter["chat_id"]==user]

    import forward_messages
    forward_messages.forwardMessages(baseurl,TOKEN,user,store,text)
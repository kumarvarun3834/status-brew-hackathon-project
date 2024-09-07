# this file will help in sending the files to bot
import requests
def copyMessages(baseurl,TOKEN , chat_id, from_chat_id, message_ids) -> None:
    url=baseurl+TOKEN+"copyMessages"
    parameters={
        "chat_id":chat_id,
        "from_chat_id": from_chat_id,
        "message_id":message_ids
                }
    run=0
    try:
        res=requests.get(url,data=parameters)
    except Exception as e:
        print(f'error occured {e}')
        if run<5:
            copyMessages(baseurl,TOKEN , chat_id, from_chat_id, message_ids)
            run+=1
    import dataview
    lst=dataview.data_view(res)
    print(lst)
    
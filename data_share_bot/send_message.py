import requests

def sendMessage(baseurl,TOKEN,chat_id, text,reply_to_message_id=None) -> None:
    url=baseurl+TOKEN+"sendmessage"
    parameters={
        "chat_id":chat_id,
        "text":text,
        "reply_to_message_id":reply_to_message_id
                }
    res=requests.get(url,data=parameters)
    if res.status_code==200:
        print("message sent")
    else:
        print("message failed to send")

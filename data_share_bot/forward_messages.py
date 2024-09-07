# this will help in management and bot file storage to another locations
from typing import Any
import requests

def forwardMessages(baseurl, TOKEN, chat_id, from_chat_id, message_ids) -> int:
    if type(message_ids) == int:
        message_ids = [message_ids]
    elif "/" in message_ids:
        message_ids = [message_ids[1:]]
    print(message_ids)
    
    url=baseurl+TOKEN+"forwardMessages"
    parameters = {
        "chat_id": chat_id,
        "from_chat_id": from_chat_id,
        "message_ids": message_ids
        # "disable_notification": disable_notification,
        # "protect_content": protect_content
    }
    run=0
    try:
        res = requests.post(url, json=parameters)
    except Exception as e:
        print(f'error occured {e}')
        if run<5:
            forwardMessages(baseurl, TOKEN, chat_id, from_chat_id, message_ids)
            run+=1
    
    if res.status_code == 200:
        response_json = res.json()
        print("Message sent")
        print("Response:", response_json)
        # Extract message details if available
        if "result" in response_json:
            result = response_json["result"]
            print("Forwarded message details:", result)
            # Response: {"ok":false,"error_code":404,"description":"Not Found"}
            if response_json["ok"]!="false":
                message_ids = [msg.get('message_id') for msg in result]
                return message_ids[-1]
                # return response_json

        else:
            print("No result in response")
    else:
        print("Message failed to send")
        print("Status code:", res.status_code)
        print("Response:", res.text)

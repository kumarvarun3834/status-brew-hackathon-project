# this will help in management and bot file storage to another locations
from typing import Any
import requests

def copymessages(baseurl, TOKEN, chat_id, from_chat_id, message_ids) -> int:
    if type(message_ids) == int:
        message_ids = [message_ids]
    elif "/" in message_ids:
        message_ids = [message_ids[1:]]
    print(message_ids)
    
    url=baseurl+TOKEN+"copyMessages"
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
            copymessages(baseurl, TOKEN, chat_id, from_chat_id, message_ids)
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


# from data import *
# res=forwardMessages(baseurl, TOKEN, cloud, store, 4780)
# print(res)
# # # this file will help in sending the file to bot
# # import requests
# # def copyMessages(baseurl,TOKEN , chat_id, from_chat_id, message_ids):
# #     url=baseurl+TOKEN+"copyMessages"
# #     parameters={
# #         "chat_id":chat_id,
# #         "from_chat_id": from_chat_id,
# #         "message_id":message_ids
# #                 }
# #     run=0
# #     try:
# #         res=requests.get(url,data=parameters)
# #         res_data = res.json()  # Parse the response JSON
# #         print(res_data)

# #         # Return the message_id if the response is successful
# #         return res_data.get("result", {}).get("message_id", None)
    
# #     except Exception as e:
# #         print(f'error occured {e}')
# #         if run<5:
# #             copyMessages(baseurl,TOKEN , chat_id, from_chat_id, message_ids)
# #             run+=1
# #     # import dataview
# #     # lst=dataview.data_view(res)
# #     # print(lst)

    

# # # from data import *

# # # # Testing the function
# # # if __name__ == "__main__":
# # #     # Simulate a successful call
# # #     print("Testing with successful response simulation...")
    
# # #     # Replace 'copyMessage' with 'copyMessages' if your endpoint is correct
# # #     response = copyMessages(baseurl, TOKEN, public , store, 4780)
    
# # #     # Print the result for verification
# # #     print(f"Result: {response}")

# import requests

# def copyMessages(baseurl, TOKEN, chat_id, from_chat_id, message_ids):
#     url = f"{baseurl}bot{TOKEN}/copyMessage"
#     parameters = {
#         "chat_id": chat_id,
#         "from_chat_id": from_chat_id,
#         "message_id": message_ids
#     }
#     run = 0
#     while run < 5:
#         try:
#             res = requests.post(url, json=parameters)  # Use post and json for API requests
#             res_data = res.json()  # Parse the response JSON
#             print("Response Data:", res_data)

#             if res.status_code == 200:
#                 if "result" in res_data:
#                     print("Copied message details:", res_data["result"])
#                     return res_data["result"].get("message_id", None)
#                 else:
#                     print("No result in response")
#             else:
#                 print("Message failed to copy")
#                 print("Status code:", res.status_code)
#                 print("Response:", res.text)
        
#         except Exception as e:
#             print(f'Error occurred: {e}')
#             run += 1
    
#     return None  # Return None if it fails after retries

# # # Example Usage
# # baseurl = "https://api.telegram.org/"
# # TOKEN = "YOUR_BOT_TOKEN"
# # chat_id = "TARGET_CHAT_ID"
# # from_chat_id = "SOURCE_CHAT_ID"
# # message_ids = 4780

# # if __name__ == "__main__":
# #     response = copyMessages(baseurl, TOKEN, chat_id, from_chat_id, message_ids)
# #     print(f"Result: {response}")

# this file will help in sending the file to bot
import requests
def copyMessages(baseurl,TOKEN , chat_id, from_chat_id, message_ids):
    url=baseurl+TOKEN+"copyMessages"
    parameters={
        "chat_id":chat_id,
        "from_chat_id": from_chat_id,
        "message_id":message_ids
                }
    run=0
    try:
        res=requests.get(url,data=parameters)
        res_data = res.json()  # Parse the response JSON
        print(res_data)

        # Return the message_id if the response is successful
        return res_data.get("result", {}).get("message_id", None)
    
    except Exception as e:
        print(f'error occured {e}')
        if run<5:
            copyMessages(baseurl,TOKEN , chat_id, from_chat_id, message_ids)
            run+=1
    # import dataview
    # lst=dataview.data_view(res)
    # print(lst)

    

# from data import *

# # Testing the function
# if __name__ == "__main__":
#     # Simulate a successful call
#     print("Testing with successful response simulation...")
    
#     # Replace 'copyMessage' with 'copyMessages' if your endpoint is correct
#     response = copyMessages(baseurl, TOKEN, public , store, 4780)
    
#     # Print the result for verification
#     print(f"Result: {response}")
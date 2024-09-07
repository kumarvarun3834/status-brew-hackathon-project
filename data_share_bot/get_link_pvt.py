import requests

def generateMessageLink(chat_id, message_id, is_private=True):
    if is_private:
        # Remove the '-100' prefix from chat_id
        chat_id = str(chat_id).replace('-100', '')
    
    link = f"https://t.me/{chat_id}/{message_id}"
    return link

# # Example usage:
chat_id = -4566364009  # Example private chat ID
message_id = 2193

from data import *
message_link = generateMessageLink(chat_id, message_id, is_private=True)
print("Direct Message Link:", message_link)

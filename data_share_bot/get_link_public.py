def generateMessageLink(chat_id=None, message_id=None, username=None, is_private=True):
    if not message_id:
        raise ValueError("message_id is required to generate a link to a specific message.")
    
    if is_private and chat_id:
        # Remove the '-100' prefix from chat_id for private groups
        chat_id = str(chat_id).replace('-100', '')
        link = f"https://t.me/c/{chat_id}/{message_id}"
    elif username:
        # Public groups/channels use the username
        link = f"https://t.me/{username}/{message_id}"
    else:
        raise ValueError("Either chat_id for private or username for public group is required.")
    
    return link

# Example usage for a private group:
private_group_chat_id = -4566364009  # Example private group chat ID
message_id = 2193
private_group_message_link = generateMessageLink(chat_id=private_group_chat_id, message_id=message_id, is_private=True)
print("Private Group Chat Message Link:", private_group_message_link)

# Example usage for a public group:
public_group_username = "examplegroup"
public_group_message_link = generateMessageLink(username=public_group_username, message_id=message_id, is_private=False)
print("Public Group Chat Message Link:", public_group_message_link)

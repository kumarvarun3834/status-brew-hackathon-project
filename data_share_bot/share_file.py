import requests
import os

def send_file(baseurl, token, chat_id, file_path) -> None:

    if os.path.exists(file_path):
        print(f"File {file_path} exists.")
        url = baseurl+token+"sendDocument"
        try:
            with open(file_path, 'rb') as file:
                files = {'document': file}
                parameters = {"chat_id": chat_id}
                res = requests.post(url, files=files, data=parameters)
            
                if res.status_code == 200:
                    print(f"File {file_path} sent successfully")
                else:
                    print(f"Failed to send file {file_path}. Status code: {res.status_code}, Response: {res.text}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"File {file_path} does not exist.")

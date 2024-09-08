# this file will get updates from the bot 
import requests
def get_updates(baseurl,TOKEN,offset=None, limit=15 )-> list:      
    # THESE UPDATES RESET AFTER DAY ENDS BE SURE TO SAVE
    url=baseurl+TOKEN+"getupdates"
    
    parameters={
            "offset":offset,
            "limit":limit
                }
    run=0
    try:
        out=requests.get(url,data=parameters)
        print(out.status_code)
        print("Status Code:", out.status_code)
    except Exception as e:
        print(f'error occured {e}')
        if run<5:
            get_updates(baseurl,TOKEN,offset)
            run+=1
    if out.status_code == 200:
        import dataview
        lst=dataview.data_view(out)
        return lst
    else:
        print("Error fetching updates")
        return []
    
# from data import *
# while True:
#     lst =get_updates(baseurl,TOKEN,offset=0,limit=None)
#     for i in lst:
#         print(i)

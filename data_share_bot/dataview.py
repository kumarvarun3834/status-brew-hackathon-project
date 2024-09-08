# this is only to beautify data and make it readable for debug
# this file creates data to readable format
def data_view(result) -> list:
    import json
    data=json.loads(result.text)
    lst=data["result"]
    if lst!=[]:
        for i in lst:
            print(i)
    if lst==[] :
        print("no data yet")
    return lst

import requests

url = "https://api.ciscospark.com/v1/messages"
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vOGE1YzcyNmItNTU2ZC0zMzlkLWEyZGMtNzQxMDhkMGRiZDU5"
bearer = "Yzg2ZjE4NjAtYWI1MC00NmExLWEzMDUtOGFkYjQxMGRjZDJiMDc0MTkxZjYtOGQ1_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

message =  "### Test message in **markdown**\n\nThis is just to show that markdown is also supported",



payload = {
    "roomId": room_id, 
    "markdown" : message
    }

headers = {
    "Authorization": "Bearer %s " % bearer
    }

response = requests.post(url, headers=headers, data = payload).json()
print(response)
   
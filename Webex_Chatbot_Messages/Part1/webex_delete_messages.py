import requests

url = "https://api.ciscospark.com/v1/messages"

room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vOGE1YzcyNmItNTU2ZC0zMzlkLWEyZGMtNzQxMDhkMGRiZDU5"
bearer = "Yzg2ZjE4NjAtYWI1MC00NmExLWEzMDUtOGFkYjQxMGRjZDJiMDc0MTkxZjYtOGQ1_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

message_url = f"?roomId={room_id}"

headers = {
    "Authorization": "Bearer %s " % bearer
    }

response = requests.get(url + message_url, headers=headers).json()
messages = response['items']
   
for message in messages:
    delete_url = f"/{message['id']}"
    response = requests.delete(url + delete_url, headers=headers)
    if response.status_code == "403":
        print("Message could not be deleted")
        continue
    else:
        print(f"Deleted message with id {message['id']}")
  
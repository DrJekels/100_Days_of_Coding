import requests

from datetime import date, datetime

pixela_url = "https://pixe.la/v1/users"
pixela_token = "8M9F$yHP"
pixela_username = "drjekels"

user_creds = {
    "token": "8M9F$yHP",
    "username": "drjekels",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_url, json=user_creds)
# print(response.text)

pixela_graph_url = f"{pixela_url}/{pixela_username}/graphs"
pixela_graph_id = "testing1"

graph_request = {
    "id": "testing1",
    "name": "reading",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": pixela_token
}

# response = requests.post(url=pixela_graph_url, json=graph_request, headers=headers)
# print(response.text)

today = datetime.now()

pixela_graph_update_url = f"{pixela_url}/{pixela_username}/graphs/{pixela_graph_id}"

graph_post = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50",
}

# response = requests.post(url=pixela_graph_update_url, json=graph_post, headers=headers)
# print(response.text)

pixela_date = today.strftime("%Y%m%d")

pixela_graph_change_url = f"{pixela_url}/{pixela_username}/graphs/{pixela_graph_id}/{pixela_date}"

graph_update = {
    "quantity": "53"
}

# response = requests.put(url=pixela_graph_change_url, json=graph_update, headers=headers)
# print(response.text)

response = requests.delete(url=pixela_graph_change_url, headers=headers)
print(response.text)
import requests
from datetime import datetime
USERNAME = "name"  # your pixe.la username
TOKEN = "your token"  # your pixe.la token
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much time did you put in? "),
}
response = requests.post(url=pixel_creation_endpoint,
                         json=pixel_data, headers=headers)

update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "50",
}

delete_endpoint = f"{update_endpoint}"

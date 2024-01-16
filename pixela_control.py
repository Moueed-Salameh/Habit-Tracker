import requests
import os
from datetime import datetime

# -----------------------CREATE ACCOUNT -------------------------------- #
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_API_TOKEN")
HEADER = {"X-USER-TOKEN": TOKEN}
HEADER_NO_BODY = {"X-USER-TOKEN": TOKEN, "Content_Length": "0"}
# -----------------------CREATE PIXEL -------------------------------- #
def post_pixel(hours):
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

    today = datetime.now()
    pixel_params = {
        "date": today.strftime(f"%Y%m%d"),
        "quantity": hours,
        "optionalData": "{\"testing\":\"Testing first pixela graph\"}"
    }

    response = requests.post(url=pixel_endpoint, headers=HEADER, json=pixel_params)
    print(response.text)

# -----------------------CREATE USER ---------------------------------- #
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# -----------------------CREATE GRAPH ---------------------------------- #
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_params = {
#     "id": "graph1",
#     "name": "Coding: Python",
#     "unit": "Hours",
#     "type": "float",
#     "color": "shibafu",
#     "timezone": "Asia/Riyadh"
# }
#
# response = requests.post(url=graph_endpoint, headers=HEADER, json=graph_params)
# print(response.text)

# -----------------------PIN GRAPH ---------------------------------- #
# pin_endpoint = f"https://pixe.la/@{USERNAME}"
# pin_params = {
#     # "displayName": "USERNAME",
#     # "gravatarIconEmail": "some-gravatar-email",
#     "title": "your-title",
#     "timezone": "your timezone",
#     # "aboutURL": "Some-url",
#     # "contributeURLs": "some-url",
#     # "pinnedGraphID": "graph1",
# }
# response = requests.put(url=pin_endpoint, headers=HEADER, json=pin_params)
# print(response.text)
